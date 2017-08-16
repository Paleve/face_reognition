from flask import Flask, request

app = Flask(__name__)

PORT = 6066
HOST = '127.0.0.1'

@app.route('/')
def hello():
    imgbase64 = request.args.get('imgbase64')

    return 'is face %s' % imgbase64

if __name__ == '__main__':
    app.run(host=HOST,port=PORT)