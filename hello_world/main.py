from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    print('in hello /')
    return "Hello world, from Flask"


@app.route('/welcome')
def welcome():
    print('in welcome ')
    return "Thank you , from Flask"


@app.route('/get/<user>')
def get_user(user):
    return 'got user name :' + user


@app.route('/contact')
def contact_us():
    return render_template('contact.html')


if __name__ == '__main__':
    print('in main')
    app.run(debug=True)
