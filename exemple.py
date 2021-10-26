#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, render_template
app = Flask(__name__)  
# __name__ contient "__main__" mais si ce code est importé par un autre fichier avec import, alors __name__ contiendra le nom de ce fichier
# (c'est pas spécifique à flask)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    text = request.form['text']
    processed_text = text.upper()
    return render_template("bienvenue.html" , message = processed_text )

@app.route("/next")
def suite():
    return render_template("page_suivante.html")

@app.route('/text')
def show_text():
    return "Page en erreur"

if __name__ == '__main__':
    app.run()