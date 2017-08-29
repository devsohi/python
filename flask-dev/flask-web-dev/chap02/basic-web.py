from flask import Flask
from flask import redirect
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    browser_name = request.headers.get('User-agent')
    return '<h1>Hello Sohi %s</h1>' % browser_name


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/user/profile')
def profile():
    return '<h2>Invalid URL </h2>', 400


@app.route('/search')
def search():
    return redirect('http://www.google.com')


if __name__ == '__main__':
    app.run(debug=True)
