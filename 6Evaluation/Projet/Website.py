from flask import Flask
from IPython.display import HTML

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' # A modifier

@app.route('/hello/<username>')
def hello_user(username):
    return 'Hello {}!'.format(username)

@app.route('/hello/<int:user_id>')
def hello_userid(user_id):
    return 'Hello user n°{}!'.format(user_id)

if __name__ == '__main__':
    app.run(debug=True, port=2745) 
