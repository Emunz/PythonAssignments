from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key = 'ThisIsSecret!'


@app.route('/')
def index():
    if session.has_key('correct_number') == False:
        session['correct_number'] = random.randrange(0,101)
    return render_template("index.html")

@app.route('/guesses', methods=["POST"])
def return_answer():
    guess = request.form['guess']
    if not len(guess) > 0:
        return redirect("/")
    elif int(guess) > session['correct_number']:
        session['guess_status'] = 'high'
        print 'number too high'
        session['need_number'] = False
        return redirect("/")
    elif int(guess) < session['correct_number']:
        session['guess_status'] = 'low'
        print 'number too low'
        session['need_number'] = False
        return redirect("/")
    elif int(guess) == session['correct_number']:
        session['guess_status'] = 'right'
        print 'YOU NAILED IT, FRAN'
        session.pop('correct_number')
        session['need_number'] = True
        return redirect("/")
    else:
        print 'Please enter a number between 0 and 100'
        return redirect("/")

@app.route('/reload')
def reload():
    session['guess_status'] = 'hide_div'
    return redirect('/')
    


app.run(debug=True) 