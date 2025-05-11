from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/") # route == 디코더가 Flask에거 어떤 url을 쓸지 알려준다
def hello_world():
    return "<p>Hello, World!</p>"

name = "안동건"
@app.route("/ahn") 
def hello_world():
    return f"Hello, {name}"





# return f"Hello, {escape(name)}!"
# 이 방식을 하여 악의적으로 정보를 캐가려는 코드를 막는다


# 실행 방법
# flask --app coding/main run