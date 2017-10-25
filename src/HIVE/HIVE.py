from flask import Flask, redirect, request, session, g, url_for, abort, render_template, flash
import numpy as np
import random
import matplotlib.pyplot as plt
#import room
import device

app = Flask(__name__)


def readFile(file):
    for w in file:
        print(w)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)