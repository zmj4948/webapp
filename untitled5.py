from flask import Flask

app = Flask(__name__)


#@app.route('/')
def hello_world():
    return 'Hello World!\n'

@app.route('/')
def hello_zoe():
    return hello_world()+'\n Zoe is the best!'


if __name__ == '__main__':
    app.run()
