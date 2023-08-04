#TestRequest.py // 파일명

from flask import Flask , render_template ,request

app=Flask(__name__)

@app.route('/')
def main():                                  #1
    return render_template('main.html')

@app.route('/state/<button>')
def state(button):                           #2
    return render_template('state.html',btn_state=button)

if __name__ == "__main__":
    app.run()





