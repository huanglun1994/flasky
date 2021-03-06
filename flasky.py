from flask.ext.bootstrap import Bootstrap
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def uesr(name):
    return  render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()
