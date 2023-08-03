"""
Flask Kakao OAuth Application Sample
"""
from flask import Flask, render_template, request, jsonify, make_response, url_for
import os
from flask_jwt_extended import (
    JWTManager, create_access_token, 
    get_jwt_identity, jwt_required,
    set_access_cookies, set_refresh_cookies, 
    unset_jwt_cookies, create_refresh_token,
    jwt_refresh_token_required,
)
from config import CLIENT_ID, REDIRECT_URI
from controller import Oauth
from model import UserModel, UserData
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "I'M IML."
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_SECURE'] = False
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 30
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = 100
jwt = JWTManager(app)

# 업로드 세트 설정
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'
configure_uploads(app, photos)

@app.route('/fileupload', methods=['POST'])
def upload_file():
    files = request.files.getlist('photo')

    if len(files) == 0:
        return '선택된 이미지 파일이 없습니다.'

    success_count = 0
    for file in files:
        if file.filename == '':
            continue
        if file and file.filename.endswith(photos.extensions):
            filename = photos.save(file)
            success_count += 1
    if success_count > 0:
        return f'{success_count}개의 파일을 성공적으로 업로드되었습니다!'
    else:
        return '잘못된 파일 형식입니다. 이미지 파일을 업로드하세요.'
    
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/delete', methods=['POST'])
def delete_file():
    data = request.get_json()
    filename = data.get('filename')

    if filename:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],"127.0.0.1:port number" ,filename) ### 로그인 유지에 대한 상태값 -> 고유값 파라미터로 가져와서 폴더명으로 활용(서비스로서) -> IP값 그냥 받기(현재)
        try:
            os.remove(file_path)
            return jsonify({'message': f'File {filename} deleted successfully!'})
        except FileNotFoundError:
            return jsonify({'error': 'File not found.'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Filename not provided.'}), 400
    
    # 파일 삭제를 위한 엔드포인트 추가
#@app.route('/delete', methods=['POST'])
#def delete_file():
#    filename = request.form.get('filename')

#    if filename:
#        try:
#            photos.delete(filename)  # 업로드된 파일 삭제
#            return jsonify({'message': f'File {filename} deleted successfully!'})
#        except FileNotFoundError:
#            return jsonify({'error': 'File not found.'}), 404
#        except Exception as e:
#            return jsonify({'error': str(e)}), 500
#    else:
#        return jsonify({'error': 'Filename not provided.'}), 400

@app.route('/photo_upload')
def photo_upload():
    return render_template('pages/photo_upload.html')
    

# 사용자는 "/" Route를 통해 먼저 서비스 페이지에 접근한 후, 
# 아래와 같은 카카오 로그인 버튼을 만나게 됨
@app.route('/logout')
@app.route("/")
def index():
    return render_template('pages/index.html')

@app.route("/intro")
def intro():
    return render_template('pages/intro.html')

@app.route("/main03")
def main03():
    return render_template('pages/main03.html')

@app.route("/Dangerous_List")
def dangerous_list():
    return render_template('pages/Dangerous_List.html')

@app.route("/oauth")
def oauth_api():
    
    # 사용자로부터 authorization code를 인자로 받음
    code = str(request.args.get('code'))
    
    # 전달받은 authorization code를 통해서
    # access_token, refresh_token을 발급
    oauth = Oauth()
    auth_info = oauth.auth(code)

    # access_token을 이용해서, Kakao에서 사용자 식별 정보 획득
    user = oauth.userinfo("Bearer " + auth_info['access_token'])
    
    # 해당 식별 정보를 서비스 DB에 저장 (회원가입)
    # 만약 이미 있을 경우, 과정 스킵
    user = UserData(user)
    UserModel().upsert_user(user)

    # 사용자 식별 id를 바탕으로 서비스 전용 access_token, refresh_token 발급
    resp = make_response(render_template('index.html'))
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    resp.set_cookie("logined", "true")
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)

    return resp


@app.route('/token/refresh')
@jwt_refresh_token_required
def token_refresh_api():
    """
    Refresh Token을 이용한 Access Token 재발급
    """
    user_id = get_jwt_identity()
    resp = jsonify({'result': True})
    access_token = create_access_token(identity=user_id)
    set_access_cookies(resp, access_token)
    return resp


@app.route('/token/remove')
def token_remove_api():
    """
    Cookie에 등록된 Token 제거
    """
    resp = jsonify({'result': True})
    unset_jwt_cookies(resp)
    resp.delete_cookie('logined')
    return resp


@app.route("/userinfo")
@jwt_required
def userinfo():
    """
    Access Token을 이용한 DB에 저장된 사용자 정보 가져오기
    """
    user_id = get_jwt_identity()
    userinfo = UserModel().get_user(user_id).serialize()
    return jsonify(userinfo)


@app.route('/oauth/url')
def oauth_url_api():
    """
    Kakao OAuth URL 가져오기
    """
    return jsonify(
        kakao_oauth_url="https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code" \
        % (CLIENT_ID, REDIRECT_URI)
    )


@app.route("/oauth/refresh", methods=['POST'])
def oauth_refesh_api():
    """
    # OAuth Refresh API
    refresh token을 인자로 받은 후,
    kakao에서 access_token 및 refresh_token을 재발급.
    (% refresh token의 경우, 
    유효기간이 1달 이상일 경우 결과에서 제외됨)
    """
    refresh_token = request.get_json()['refresh_token']
    result = Oauth().refresh(refresh_token)
    return jsonify(result)


@app.route("/oauth/userinfo", methods=['POST'])
def oauth_userinfo_api():
    """
    # OAuth Userinfo API
    kakao access token을 인자로 받은 후,
    kakao에서 해당 유저의 실제 Userinfo를 가져옴
    """
    access_token = request.get_json()['access_token']
    result = Oauth().userinfo("Bearer " + access_token)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)