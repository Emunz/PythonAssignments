from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/users/<username>')
def show_user_profile(username):
    print username
    return render_template("user.html")

@app.route('/users/<username>/<id>')
def user_id(username, id):
    print "Username:", username
    print "User ID:", id
    return render_template("user.html", name = username, user_id = id)


app.run(debug=True)
