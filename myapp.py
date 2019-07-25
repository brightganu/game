from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'

@app.route('/whereami')
def whereami():
    return 'Ghana'

@app.route('/yes')
def foo():
    return 'workiing'

if __name__ == '_main_':
    app.run()
    