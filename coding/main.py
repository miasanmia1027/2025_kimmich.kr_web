from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return 'Hello, Pybo!'

    return app
























# return f"Hello, {escape(name)}!"
# 이 방식을 하여 악의적으로 정보를 캐가려는 코드를 막는다


# 실행 방법
# flask --app coding/main run