from flask import Flask

app = Flask(__name__)
# app.debug = True
# app.secret_key = "asdfasdf"

app.config.from_object("settings.DevelopmentConfig")

@app.route('/')
def index():
    return 'Hello World--config settings!'


if __name__ == '__main__':
    app.run()