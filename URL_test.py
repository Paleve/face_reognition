from flask import Flask, request

app = Flask(__name__)

PORT = 6061
HOST = '0.0.0.0'

@app.route('/')
def hello():
    imgbase64 = request.args.get('img')

    return 'is face %s' % imgbase64

if __name__ == '__main__':
    app.run(host=HOST,port=PORT)