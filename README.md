# 한글(KR)
# 프로젝트 이름 : 야옹아 거기는 위험해!

# 프로젝트 설명


# 목표


# 브랜치
    - Jinmyung : flask 서버에서 YOLO가 실행되는 부분 담당
    -

# 버전
- `Python 3.10.10`
```python
# 가상환경 설정(.venv)
py -3.10 -m venv .venv

# 가상환경 활성화
./.venv/Scripts/activate

# pip 업그레이드
python -m pip install --upgrade pip

# 패키지 설치
pip install -r ./requirements.txt

# 실행
python app.py
```

- **Werkzeug issue**: 해당 경로에 있는 파일 수정이 필요함 `.venv/Lib/site-packages/flask_uploads.py`
  
    ```python
    # Before
    from werkzeug import secure_filename, FileStorage
    # After
    from werkzeug.utils import secure_filename
    from werkzeug.datastructures import FileStorage
    ```

# 환경설정
## 카카오 로그인
- `config.py` : Kakao Developers에서 어플리케이션 등록을 한 후, 발급받은 Client_id, Client_Secret, Redirect_URI를 입력
  
  ```python
  # config.py 예시
  CLIENT_ID = "9gjx2p4m6a1e5c8q7h0f3k2b1d4w6z8r9t7y"
  CLIENT_SECRET = "s2d8f9a4j6l0p3r5e7t1y6x4z8c2v0b"
  REDIRECT_URI = "http://localhost:5000/oauth" # 로그인 이후에 갈 URL
  SIGNOUT_REDIRECT_URI = "http://localhost:5000/logout" 
    ```

## 이메일

1. setting_email.py 파일을 수정해야 함

2. [My Google Account -> Security](https://myaccount.google.com/security)로 이동.

3. 2단계 인증 활성화

4. [App Passwords](https://myaccount.google.com/apppasswords)로 이동하여 커스텀 앱 이름을 작성 후 생성

5. 생성된 암호를 복사하여 setting_email.py "password" 변수에 복사

## 탐지 이미지가 저장될 공간 생성
web/src/static 안에 'warnings' 폴더 생성

# 폴더 정보
1. preprocessing & training
- `image_preprocessing.ipynb` ← 이미지 전처리(이미지 데이터 증량)
- `cat_alertv7.ipynb` ← YOLOv8 커스텀 데이터 학습   

2. uploads
- 사용자가 업로드한 이미지가 저장되는 공간

3. web/src
3-1. static
- 웹페이지에 구성에 필요한 이미지, 폰트가 저장되어 있음
- 탐지된 이미지 저장됨

3-2. templates
- 서비스 페이지가 저장되어 있음

3-3. yolo_assets
- `Classes` : 탐지할 대상의 목록을 저장
- `Models` : YOLOv8 가중치를 저장
- `alarm2.mp3` : 경보음

3-3-1. 학습이력
- v1 : `stove, display, dresser, cat, closet, sofa` 탐지(4,444장)
- v2 : `stove, cat` 탐지(3,091장)
- v3 : `stove, cat` 탐지(6,097장)
- v4 : `stove, cat` 탐지(5,415장)
- v5 : `stove, cat` 탐지(9,953장)
- v6 : `stove, cat` 탐지(7,370장)
- v7 : `stove, cat` 탐지(7,370장), epoch 200회

3-3-2. 문제점 및 개선사항
- v1 : `stove, display` 객체 혼동
        `dresser, closet` 객체는 잘 인식 못함(데이터 비중이 매우 낮음)
- v2 : `stove` 객체 데이터 부족 → `stove` 데이터 증량
- v3 : 가스렌지와 스테인리스 그릇을 잘 구분 못함 → `stove`를 2구 이하 검은색 인덕션으로 한정
- v4 : 고양이의 측면과 뒷면을 잘 인식 못함 → 고양이 측면과 뒷면 사진 증량(1,873 cat, 3,542 stove)
- v5 : 인덕션 상판에 빛이 반사될 때 인식을 잘 못함 → 학습에 방해되는 인덕션 이미지 제거
- v6 : 모델이 객체 탐지를 쉽게 놓침 → epoch를 100회에서 200회로 증가(loss값이 계속 감소하는 방향임)

4. 파일 정보
- `app.py` : flask 구동하고 웹페이지를 띄움
- `controller.py` : Kakao Auth, API 서버와 통신하기 위해 필요한 모듈
- `infer.py` : YOLO 모델을 실행
- `model.py` : 데이터를 생성하고 조회
- `setting_email.py` : 메일을 받을 사용자를 설정
- `TestRequest.py`
- `README.md` : 프로젝트 정보와 사용방법 설명
- `requirements.txt` : 서비스 이용에 필요한 python 패키지 리스트



# English
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

## E-mail

1. In the em.py file make the necessary changes wherever mentioned.

2. Go to [My Google Account -> Security](https://myaccount.google.com/security).

3. Enable 2-Step verification and complete the process.

4. Go to [App Passwords](https://myaccount.google.com/apppasswords) and create custom app name and then click on generate. 

5. Copy the generated password and paste it in the variable "password" in the em.py file.

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
