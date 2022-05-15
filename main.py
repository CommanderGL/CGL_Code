from flask import Flask, render_template, redirect, url_for, request, session
from replit import db
import os
#import subprocess
from __modules__.console import *

app = Flask('app')
app.secret_key = "__--CGL_CommanderGL_104--__"

@app.route('/')
def Home():
    if "name" in session and "pass" in session:
        return render_template('index.html',
                               name=session["name"],
                               password=session["pass"],
                               LOGGED_IN=True)
    else:
        return render_template('index.html',
                               name="not",
                               password="not",
                               LOGGED_IN=False)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["pass"]
        for i in db["accounts"]:
            if username in i['name'] and password in i['pass']:
                LOGGED_IN = True
                session["name"] = username
                session["pass"] = password
                return redirect(url_for("Home"))
                break
            else:
                LOGGED_IN = False

        if LOGGED_IN == False:
            return render_template('login.html')

    else:
        return render_template('login.html')


@app.route('/sign_up', methods=["GET", "POST"])
def new_a():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["pass"]
        db["accounts"].append({'name': username, 'pass': password})
        session["name"] = username
        session["pass"] = password

        return redirect(url_for("Home"))
    else:
        return render_template('new_a.html')


@app.route('/html/edit/<file>', methods=["GET", "POST"])
def code(file):
    if request.method == "POST":
        code = request.form["code"]
        os.remove("users/" + session['name'] + '/' + file)
        with open("users/" + session['name'] + '/' + file, 'w') as f:
            f.write(code)
    try:
        os.mkdir("users/" + session["name"])
    except:
        pass
    try:
        open("users/" + session['name'] + '/' + file, "x")
    except:
        pass
    if open("users/" + session['name'] + '/' + file, 'r').read() == '':
        with open("users/" + session['name'] + '/' + file, 'w') as f:
            f.write("""
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>Document</title>
	</head>
	<body>
	
	</body>
</html>
			""")
    return render_template('new_h.html',
                           name=session['name'],
                           code=open("users/" +session['name'] + '/' + file, 'r').read(),
                           file=file)


@app.route('/<user>/html/<file>')
def run(user, file):
    with open("users/" + user + '/' + file, 'r') as f:
        return f.read()


@app.route('/python/edit/<file>', methods=["GET", "POST"])
def code_py(file):
    if request.method == "POST":
        code = request.form["code"]
        os.remove("users/" + session['name'] + '/' + file)
        with open("users/" + session['name'] + '/' + file, 'w') as f:
            f.write(code)
    try:
        os.mkdir("users/" + session["name"])
    except:
        pass
    try:
        open("users/" + session['name'] + '/' + file, "x")
    except:
        pass
    if open("users/" + session['name'] + '/' + file, 'r').read() == '':
        with open("users/" + session['name'] + '/' + file, 'w') as f:
            f.write("print('Hello World!')")
    return render_template('new_p.html',
                           name=session['name'],
                           code=open("users/" + session['name'] + '/' + file, 'r').read(),
                           file=file)


@app.route('/<user>/python/<file>')
def run_py(user, file):
    return run_return_py(f"users/{user}/{file}")

@app.route('/node/edit/<file>', methods=["GET", "POST"])
def code_node(file):
    if request.method == "POST":
        code = request.form["code"]
        os.remove("users/" + session['name'] + '/' + file)
        with open("users/" + session['name'] + '/' + file, 'w') as f:
            f.write(code)
    try:
        os.mkdir("users/" + session["name"])
    except:
        pass
    try:
        open("users/" + session['name'] + '/' + file, "x")
    except:
        pass
    if open("users/" + session['name'] + '/' + file, 'r').read() == '':
        with open("users/" + session['name'] + '/' + file, 'w') as f:
            f.write("console.log('Hello World!');")
    return render_template('new_n.html',
                           name=session['name'],
                           code=open("users/" + session['name'] + '/' + file, 'r').read(),
                           file=file)


@app.route('/<user>/node/<file>')
def run_node(user, file):
    return run_return_node(f"users/{user}/{file}")

@app.route('/logout')
def logout():
    session.pop('name', None)
    session.pop('pass', None)
    return redirect(url_for("Home"))

app.run(host='0.0.0.0', port=3000, debug=True)