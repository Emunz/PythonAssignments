from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", phrase = "Hello", times = 5, yells = 10, name = 'I\'m sorry your computer\'s slow')

app.run(debug=True)