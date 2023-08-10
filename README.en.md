<div align="center">
      <a href="https://github.com/jm83-database/Playdata-H.AI/blob/main/README.md"><img alt="lang_KR" src="https://img.shields.io/badge/lang-KR-orange"></a>
      <a href="https://github.com/jm83-database/Playdata-H.AI/blob/main/README.en.md"><img alt="lang_EN" src="https://img.shields.io/badge/lang-EN-orange"></a>
</div>

# Project Name : Hey kitty! That is dangerous!!


# Description


# Objective


# Branch
- YOLO-FLASK : Execute YOLO in flask server
- web-dev : Integrated branch about web development
- dangerous-list : Dangerous object upload page implemented
- dropdown : Dropdown Menu page implemented
- header-main-page : Main & Header page implemented
- notification : Email notification page implemented
- upload_delete : User image upload and delete function implemented

# Version
- `Python 3.10.10`
- **Werkzeug issue**: You need to modify `.venv/Lib/site-packages/flask_uploads.py`
  
```python
# Before
from werkzeug import secure_filename, FileStorage
# After
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
```

# Settings
## 1) Kakao Login
- `config.py` : Registrate your application on Kakao Developers, and write your issued Client_id, Client_Secret, Redirect_URI
  
```python
# config.py example
CLIENT_ID = "9gjx2p4m6a1e5c8q7h0f3k2b1d4w6z8r9t7y"
CLIENT_SECRET = "s2d8f9a4j6l0p3r5e7t1y6x4z8c2v0b"
REDIRECT_URI = "http://localhost:5000/oauth" # Login Redirect URL
SIGNOUT_REDIRECT_URI = "http://localhost:5000/logout" 
```

Save `config.py` in `web/src` folder

## 2) Make json file to save login data
Make `db.json` in default path

## 3) E-mail

1. In the setting_email.py file make the necessary changes wherever mentioned.

2. Go to [My Google Account -> Security](https://myaccount.google.com/security).

3. Enable 2-Step verification and complete the process.

4. Go to [App Passwords](https://myaccount.google.com/apppasswords) and create custom app name and then click on generate. 

5. Copy the generated password and paste it in the variable "password" in the setting_email.py file.

## 4) Make directory to save captured images
Make `warnings` folder in `web/src/static`

# Folder information
1. preprocessing & training
- `image_preprocessing.ipynb` ← Image preprocessing(Increase images)
- `cat_alertv7.ipynb` ← YOLOv8 custom data training  

2. uploads
- Images that are uploaded by user saved

3. web/src</br>
3-1. static
- Images and fonts required for web page are stored
- Save images captured while alerting

3-2. templates
- Service page templates

3-3. yolo_assets
- `Classes` : List of object's to detect
- `Models` : Save YOLOv8 weights
- `alarm2.mp3` : alert sound


3-3-1. Training version
- v1 : `stove, display, dresser, cat, closet, sofa` detection(4,444 Images)
- v2 : `stove, cat` detection(3,091 Images)
- v3 : `stove, cat` detection(6,097 Images)
- v4 : `stove, cat` detection(5,415 Images)
- v5 : `stove, cat` detection(9,953 Images)
- v6 : `stove, cat` detection(7,370 Images)
- v7 : `stove, cat` detection(7,370 Images), epoch 200

3-3-2. Problem & Improvements
- v1 : `stove, display` class is confused</br>  `dresser, closet` class is unbalanced than other classes(Not enough images)
- v2 : `stove` class data is not enough → Increase `stove` class data
- v3 : gas stove image is confused with steel dishes → train with induction(black & 2 plates)
- v4 : Model is confused with rear and side view of cats → train side and rear view of cats(1,873 cat, 3,542 stove)
- v5 : Model is confused with reflected light in stoves → delete images that are disturbing training
- v6 : Model easily loses detection → Increase train epoch 100 to 200(loss value was decreasing while 100 epochs)

4. File information
- `app.py` : Execute flask and show web pages
- `controller.py` : Module to communicate with Kakao Auth, API server
- `infer.py` : Execut YOLOv8
- `model.py` : Generate user data and check
- `setting_email.py` : Setting email to send and receive
- `README.md` : Explain project information and user guide
- `requirements.txt` : Python pakages required for service

# Reference
- yolo-flask : https://github.com/FaresElmenshawi/flask-yolov8-object-detection
- mail : https://github.com/AKLucifer666/Theft_Alert/tree/main
- alert : https://github.com/NadavIs56/YOLOv8-Dog-Couch-RealTimeDetection