<div align="center">
      <img width="100%" src="https://github.com/jm83-database/Playdata-H.AI/blob/main/cat_alert.png"></a>
      <h1>Hey kitty! That is dangerous!</h1>
</div>

<div align="center">
      <a href="https://github.com/jm83-database/Playdata-H.AI/blob/main/README.md"><img alt="lang_KR" src="https://img.shields.io/badge/lang-KR-orange"></a>
      <a href="https://github.com/jm83-database/Playdata-H.AI/blob/main/README.en.md"><img alt="lang_EN" src="https://img.shields.io/badge/lang-EN-orange"></a>
      <h3>Technologies Used</h3>
      <a><img src="https://img.shields.io/badge/python-%233776AB.svg?&style=for-the-badge&logo=python&logoColor=white" /></a>
      <a><img src="https://img.shields.io/badge/jupyter-%23F37626.svg?&style=for-the-badge&logo=jupyter&logoColor=white" /></a>
      <a><img src="https://img.shields.io/badge/google%20colab-%23F9AB00.svg?&style=for-the-badge&logo=google%20colab&logoColor=black" /></a>
      <a><img src="https://img.shields.io/badge/slack-%234A154B.svg?&style=for-the-badge&logo=slack&logoColor=white" /></a>
      <a><img src="https://img.shields.io/badge/notion-%23000000.svg?&style=for-the-badge&logo=notion&logoColor=white" /></a>
      <a><img src="https://img.shields.io/badge/html5-%23E34F26.svg?&style=for-the-badge&logo=html5&logoColor=white" /></a>
      <a><img src="https://img.shields.io/badge/javascript-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black" /></a>
      <a><img src="https://img.shields.io/badge/css3-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white" /></a>
      <a><img src="https://img.shields.io/badge/flask-%23000000.svg?&style=for-the-badge&logo=flask&logoColor=white" /></a>
      <a><img src="https://img.shields.io/badge/kakao-%23FFCD00.svg?&style=for-the-badge&logo=kakao&logoColor=black" /></a>
      <a><img src="https://img.shields.io/badge/google-%234285F4.svg?&style=for-the-badge&logo=google&logoColor=white" /></a>
</div>

# Outline
- [Project Name](#project-name)
- [Description](#description)
- [Objective](#objective)
- [Contributors](#contributors)
- [Branch](#branch)
- [Settings](#settings)
  - [Virtual Environment](#venv)
  - [Werkzeug issue](#issue)
  - [Kakao Login](#login)
  - [Make json file to save login data](#database)
  - [E-mail](#email)
  - [Make directory to save captured images](#capture)
  - [Install Pretendard font](#font)
- [Folder information](#folder-info)
  - [preprocessing & training](#preprocessing-training)
  - [uploads](#upload)
  - [web/src](#web-src)
    - [static](#static)
    - [templates](#templates)
    - [yolo_assets](#yolo-assets)
      - [Training version](#train-version)
      - [Problem & Improvements](#problem-improvements)
  - [File information](#file-info)
- [Reference](#reference)

# Project Name : Hey kitty! That is dangerous!<a id="project-name"></a>

# Description<a id="description"></a>
In order to relieve the anxiety of 2030 single-person household owners who have to leave their cats alone for a long time at school, work and to protect their cats from danger, when a cat approaches a dangerous object, it plays a warning sound, send notifications, and captures dangerous situations.

# Objective<a id="objective"></a>
1. User's free registration of dangerous objects
2. When a cat approaches the dangerous object, it plays an alarm sound, send notifications, and capture the dangerous situation.

# Contributors<a id="contributors"></a>
- Model
  + Sunhwa Bae : Image proprocessing & Data collect
  + Jinmyung Choi : Team leader, YOLOv8 training & upgrade performance
- Web
  + Gio Kim : Implement dropdown box
  + Seohyun Jang : Implement social login
  + Youngeun Yu : Integrate web pages & main page production
  + Yebin Yu : Implement dangerous object upload page and upload function

# Branch<a id="branch"></a>
- YOLO-FLASK : Execute YOLO in flask server
- web-dev : Integrated branch about web development
- dangerous-list : Dangerous object upload page implemented
- dropdown : Dropdown Menu page implemented
- header-main-page : Main & Header page implemented
- notification : Email notification page implemented
- upload_delete : User image upload and delete function implemented

# Settings<a id="settings"></a>
## 1) Virtual environment<a id="venv"></a>
Install `Python 3.10.10`
```python
# Setting virtual environment(.venv)
py -3.10 -m venv .venv

# activate .venv
./.venv/Scripts/activate

# upgrade pip
python -m pip install --upgrade pip

# install packages
pip install -r ./requirements.txt

# execute
python app.py
```

## 2) Werkzeug issue<a id="issue"></a>
You need to modify `.venv/Lib/site-packages/flask_uploads.py`
  
```python
# Before
from werkzeug import secure_filename, FileStorage
# After
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
```

## 3) Kakao Login<a id="login"></a>
- `config.py` : Registrate your application on Kakao Developers, and write your issued Client_id, Client_Secret, Redirect_URI
  
```python
# config.py example
CLIENT_ID = "9gjx2p4m6a1e5c8q7h0f3k2b1d4w6z8r9t7y"
CLIENT_SECRET = "s2d8f9a4j6l0p3r5e7t1y6x4z8c2v0b"
REDIRECT_URI = "http://localhost:5000/oauth" # Login Redirect URL
SIGNOUT_REDIRECT_URI = "http://localhost:5000/logout" 
```

Save `config.py` in `web/src` folder

## 4) Make json file to save login data<a id="database"></a>
Make `db.json` in default path

## 5) E-mail<a id="email"></a>

1. In the setting_email.py file make the necessary changes wherever mentioned.

2. Go to [My Google Account -> Security](https://myaccount.google.com/security).

3. Enable 2-Step verification and complete the process.

4. Go to [App Passwords](https://myaccount.google.com/apppasswords) and create custom app name and then click on generate. 

5. Copy the generated password and paste it in the variable "password" in the setting_email.py file.

## 6) Make directory to save captured images<a id="capture"></a>
Make `warnings` folder in `web/src/static`

## 7) Install Pretendard font<a id="font"></a>
Make `fonts` folder in `web/src/static` and save [Pretend fonts](https://cactus.tistory.com/306) inside `fonts`

# Folder information<a id="folder-info"></a>
1. preprocessing & training<a id="preprocessing-training"></a>
- `image_preprocessing.ipynb` ← Image preprocessing(Increase images)
- `cat_alertv7.ipynb` ← YOLOv8 custom data training  

2. uploads<a id="upload"></a>
- Images that are uploaded by user saved

3. web/src</br><a id="web-src"></a>
3-1. static<a id="static"></a>
- Images and fonts required for web page are stored
- Save images captured while alerting

3-2. templates<a id="templates"></a>
- Service page templates

3-3. yolo_assets<a id="yolo-assets"></a>
- `Classes` : List of object's to detect
- `Models` : Save YOLOv8 weights
- `alarm2.mp3` : alert sound


3-3-1. Training version<a id="train-version"></a>
- v1 : `stove, display, dresser, cat, closet, sofa` detection(4,444 Images)
- v2 : `stove, cat` detection(3,091 Images)
- v3 : `stove, cat` detection(6,097 Images)
- v4 : `stove, cat` detection(5,415 Images)
- v5 : `stove, cat` detection(9,953 Images)
- v6 : `stove, cat` detection(7,370 Images)
- v7 : `stove, cat` detection(7,370 Images), epoch 200

3-3-2. Problem & Improvements<a id="problem-improvements"></a>
- v1 : `stove, display` class is confused</br>  `dresser, closet` class is unbalanced than other classes(Not enough images)
- v2 : `stove` class data is not enough → Increase `stove` class data
- v3 : gas stove image is confused with steel dishes → train with induction(black & 2 plates)
- v4 : Model is confused with rear and side view of cats → train side and rear view of cats(1,873 cat, 3,542 stove)
- v5 : Model is confused with reflected light in stoves → delete images that are disturbing training
- v6 : Model easily loses detection → Increase train epoch 100 to 200(loss value was decreasing while 100 epochs)

4. File information<a id="file-info"></a>
- `app.py` : Execute flask and show web pages
- `controller.py` : Module to communicate with Kakao Auth, API server
- `infer.py` : Execut YOLOv8
- `model.py` : Generate user data and check
- `setting_email.py` : Setting email to send and receive
- `README.md` : Explain project information and user guide
- `requirements.txt` : Python pakages required for service

# Reference<a id="reference"></a>
- YOLOv8 : https://github.com/ultralytics/ultralytics
- yolo-flask : https://github.com/FaresElmenshawi/flask-yolov8-object-detection
- mail : https://github.com/AKLucifer666/Theft_Alert/tree/main
- alert : https://github.com/NadavIs56/YOLOv8-Dog-Couch-RealTimeDetection
