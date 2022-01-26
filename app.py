from glob import escape
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome to My Watchlist'
    

@app.route('/home')
def home():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    # return 'User Page'
    return 'User : %s' % escape(name)


@app.route('/test')
def test_url():
    print(url_for('hello'))
    print(url_for('user_page', name='stevenazy'))
    print(url_for('test_url'))
    print(url_for('test_url', num=2))
    return 'Test Page'