from flask import Flask, render_template, request, redirect, session
import random
import datetime
app = Flask(__name__)

app.secret_key = 'ThisIsSecret!'

@app.route('/')
def index():
    if session.has_key('total_gold') == False:
        session['total_gold'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=["POST"])
def process_money():
    if session.has_key('activities') == False:
        session['activities'] = []
    if request.form['building'] == 'farm':
        gold = random.randrange(10,21)
        session['total_gold'] += gold
        session['log'] = 'Earned ' + str(gold) + ' gold from the farm! (' + str(datetime.datetime.now()) + ')'
        session['activities'].append(session['log'])
        color = 'green'
        return redirect("/")
    if request.form['building'] == 'cave':
        gold = random.randrange(5,10)
        session['total_gold'] += gold
        session['log'] = 'Earned ' + str(gold) + ' gold from the house! (' + str(datetime.datetime.now()) + ')'
        session['activities'].append(session['log'])
        color = 'green'
        return redirect("/")
    if request.form['building'] == 'house':
        gold = random.randrange(2,6)
        session['total_gold'] += gold
        session['log'] = 'Earned ' + str(gold) + ' gold from the house! (' + str(datetime.datetime.now()) + ')'
        session['activities'].append(session['log'])
        color = 'green'
        return redirect("/")
    if request.form['building'] == 'casino':
        gold = random.randrange(-50,51)
        session['total_gold'] += gold
        if gold < 0:
            session['log'] = 'Lost ' + str(abs(gold)) + ' gold at the casino! (' + str(datetime.datetime.now()) + ')'
            session['activities'].append(session['log'])
            color = 'red'
        else: 
            session['log'] = 'Earned ' + str(gold) + ' gold from the casino! (' + str(datetime.datetime.now()) + ')'
            session['activities'].append(session['log'])
            color = 'green'
        return redirect("/")



app.run(debug=True) 