from flask import Flask
import room

app = Flask(__name__)


def readFile(file):
    for w in file:
        print(w)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
    f = open('1-3-2005-RAW.data', 'r')

