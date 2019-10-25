from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/xd')
def x_d():
    return 'Hello again'


if __name__ == '__main__':
    app.run()
