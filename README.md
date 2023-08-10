<div align="center">
      <a href="https://github.com/jm83-database/Playdata-H.AI/blob/main/README.md"><img alt="lang_KR" src="https://img.shields.io/badge/lang-KR-orange"></a>
      <a href="https://github.com/jm83-database/Playdata-H.AI/blob/main/README.en.md"><img alt="lang_EN" src="https://img.shields.io/badge/lang-EN-orange"></a>
</div>

- [프로젝트 이름](#project-name)
- [프로젝트 설명](#description)
- [목표](#objective)
- [브랜치](#branch)
- [환경설정](#settings)
  - [가상환경 설정](#venv)
  - [Werkzeug issue](#issue)
  - [카카오 로그인](#login)
  - [로그인한 사용자의 데이터가 저장되는 공간 생성](#database)
  - [이메일](#email)
  - [탐지 이미지가 저장될 공간 생성](#capture)
- [폴더 정보](#folder-info)
  - [preprocessing & training](#preprocessing-training)
  - [uploads](#upload)
  - [web/src](#web-src)
    - [static](#static)
    - [templates](#templates)
    - [yolo_assets](#yolo-assets)
      - [학습이력](#train-version)
      - [문제점 및 개선사항](#problem-improvements)
  - [파일 정보](#file-info)
- [참고자료](#reference)

# 프로젝트 이름 : 야옹아 거기는 위험해!<a id="project-name"></a>

# 프로젝트 설명<a id="description"></a>


# 목표<a id="objective"></a>


# 브랜치<a id="branch"></a>
- YOLO-FLASK : flask 서버에서 YOLO가 실행되는 기능 구현
- web-dev : 웹 개발 통합 브랜치
- dangerous-list : 위험물 등록 페이지 구현
- dropdown : 드롭다운 박스 기능 구현
- header-main-page : 메인 화면 및 헤더 페이지 구현
- notification : 이메일 알림 기능 구현
- upload_delete : 사용자의 업로드와 삭제 기능 구현

# 환경설정<a id="settings"></a>
## 1) 가상환경 설정<a id="venv"></a>
`Python 3.10.10` 설치
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

## 2) Werkzeug issue
해당 경로에 있는 파일 수정이 필요함 `.venv/Lib/site-packages/flask_uploads.py`<a id="issue"></a>
```python
# 이전
from werkzeug import secure_filename, FileStorage
# 이후
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
```

## 3) 카카오 로그인<a id="login"></a>
- `config.py` : Kakao Developers에서 어플리케이션 등록을 한 후, 발급받은 Client_id, Client_Secret, Redirect_URI를 입력
```python
# config.py 예시
CLIENT_ID = "9gjx2p4m6a1e5c8q7h0f3k2b1d4w6z8r9t7y"
CLIENT_SECRET = "s2d8f9a4j6l0p3r5e7t1y6x4z8c2v0b"
REDIRECT_URI = "http://localhost:5000/oauth" # 로그인 이후에 갈 URL
SIGNOUT_REDIRECT_URI = "http://localhost:5000/logout" 
```

`web/src` 폴더 안에 `config.py` 저장

## 4) 로그인한 사용자의 데이터가 저장되는 공간 생성<a id="database"></a>
기본 경로에 `db.json` 생성

## 5) 이메일<a id="email"></a>

1. setting_email.py 파일을 수정해야 함

2. [내 계정 -> 보안](https://myaccount.google.com/security)로 이동.

3. 2단계 인증 활성화

4. [앱 비밀번호](https://myaccount.google.com/apppasswords)로 이동하여 커스텀 앱 이름을 작성 후 생성

5. 생성된 암호를 복사하여 setting_email.py "password" 변수에 복사

## 6) 탐지 이미지가 저장될 공간 생성<a id="capture"></a>
`web/src/static` 폴더 안에 `warnings` 폴더 생성

# 폴더 정보<a id="folder-info"></a>
1. preprocessing & training<a id="preprocessing-training"></a>
- `image_preprocessing.ipynb` ← 이미지 전처리(이미지 데이터 증량)
- `cat_alertv7.ipynb` ← YOLOv8 커스텀 데이터 학습   

2. uploads<a id="upload"></a>
- 사용자가 업로드한 이미지가 저장되는 공간

3. web/src<a id="web-src"></a>

3-1. static<a id="static"></a>
- 웹페이지에 구성에 필요한 이미지, 폰트가 저장되어 있음
- 탐지된 이미지 저장됨

3-2. templates<a id="templates"></a>
- 서비스 페이지가 저장되어 있음

3-3. yolo_assets<a id="yolo-assets"></a>
- `Classes` : 탐지할 대상의 목록을 저장
- `Models` : YOLOv8 가중치를 저장
- `alarm2.mp3` : 경보음

3-3-1. 학습이력<a id="train-version"></a>
- v1 : `stove, display, dresser, cat, closet, sofa` 탐지(4,444장)
- v2 : `stove, cat` 탐지(3,091장)
- v3 : `stove, cat` 탐지(6,097장)
- v4 : `stove, cat` 탐지(5,415장)
- v5 : `stove, cat` 탐지(9,953장)
- v6 : `stove, cat` 탐지(7,370장)
- v7 : `stove, cat` 탐지(7,370장), epoch 200회

3-3-2. 문제점 및 개선사항<a id="problem-improvements"></a>
- v1 : `stove, display` 객체 혼동</br>  `dresser, closet` 객체는 잘 인식 못함(데이터 비중이 매우 낮음)
- v2 : `stove` 객체 데이터 부족 → `stove` 데이터 증량
- v3 : 가스렌지와 스테인리스 그릇을 잘 구분 못함 → `stove`를 2구 이하 검은색 인덕션으로 한정
- v4 : 고양이의 측면과 뒷면을 잘 인식 못함 → 고양이 측면과 뒷면 사진 증량(1,873 cat, 3,542 stove)
- v5 : 인덕션 상판에 빛이 반사될 때 인식을 잘 못함 → 학습에 방해되는 인덕션 이미지 제거
- v6 : 모델이 객체 탐지를 쉽게 놓침 → epoch를 100회에서 200회로 증가(loss값이 계속 감소하는 방향임)

4. 파일 정보<a id="file-info"></a>
- `app.py` : flask 구동하고 웹페이지를 띄움
- `controller.py` : Kakao Auth, API 서버와 통신하기 위해 필요한 모듈
- `infer.py` : YOLO 모델을 실행
- `model.py` : 로그인한 사용자의 데이터를 생성하고 조회
- `setting_email.py` : 메일을 받을 사용자를 설정
- `README.md` : 프로젝트 정보와 사용방법 설명
- `requirements.txt` : 서비스 이용에 필요한 python 패키지 리스트

# 참고자료<a id="reference"></a>
- yolo-flask : https://github.com/FaresElmenshawi/flask-yolov8-object-detection
- 메일 전송 : https://github.com/AKLucifer666/Theft_Alert/tree/main
- alert : https://github.com/NadavIs56/YOLOv8-Dog-Couch-RealTimeDetection
