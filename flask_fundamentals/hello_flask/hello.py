from flask import Flask, render_template
app = Flask(__name__)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/cat')
def cat():
    return render_template('cat.html')



app.run(debug=True)