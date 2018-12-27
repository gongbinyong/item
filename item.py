from flask import Flask
from redis import StrictRedis
app = Flask(__name__)


class Config(object):
    pass


app.config.from_object(Config)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)