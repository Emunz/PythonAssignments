from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key = 'ThisIsSecret!'


@app.route('/')
def index():
    if session.has_key('correct_number') == False:
        session['correct_number'] = random.randrange(0,101)
    return render_template("index.html")


app.run(debug=True) 