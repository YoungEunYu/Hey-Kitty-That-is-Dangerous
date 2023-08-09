# 0. Project Name : 야옹아 거기는 위험해!
# 1. Description(프로젝트 설명)
# 2. Objective(목표)
# 3. Branch

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
- `config.py` : Kakao Developers에서 어플리케이션 등록을 한 후, 발급받은 Client_id, Client_Secret, Redirect_URI를 입력
  
  ```python
  # config.py 예시
  CLIENT_ID = "9gjx2p4m6a1e5c8q7h0f3k2b1d4w6z8r9t7y"
  CLIENT_SECRET = "s2d8f9a4j6l0p3r5e7t1y6x4z8c2v0b"
  REDIRECT_URI = "http://localhost:5000/oauth" # 로그인 이후에 갈 URL
  SIGNOUT_REDIRECT_URI = "http://localhost:5000/logout" 
    ```
# Folder information
1. code
    - image preprocessing
    - yolo webcam stream

2. model(customed yolov8n weight)
    - v1 : `stove, display, dresser, cat, closet, sofa` detection(4,444 Images)
    - v2 : `stove, cat` detection(3,091 Images)
    - v3 : `stove, cat` detection(6,097 Images)
    - v4 : `stove, cat` detection(5,415 Images)
    - v5 : `stove, cat` detection(9,953 Images)
    - v6 : `stove, cat` detection(7,370 Images)
    - v7 : `stove, cat` detection(7,370 Images), epoch 200

3. Problem
    - v1 : `stove, display` class is confused
           `dresser, closet` class is unbalanced than other classes(Not enough images)
    - v2 : `stove` class data is not enough
    - v3 : gas stove image is confused with steel dishes → train with induction(black & 2 plates)
    - v4 : Model is confused with rear and side view of cats → train side and rear view of cats(1,873 cat, 3,542 stove)
    - v5 : Model is confused with reflected light in stoves → delete images that are disturbing training
    - v6 : Model easily loses detection → train epoch 100 to 200
