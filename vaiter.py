# -*- coding: utf-8 -*-

from flask import Flask, render_template
from frases import frases
from random import shuffle

app = Flask(__name__)


@app.route('/')
def home():
    shuffle(frases)
    return render_template('home.html', frase=frases[0])


if __name__ == '__main__':
    app.run()
