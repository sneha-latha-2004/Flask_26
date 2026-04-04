from flask import Flask, redirect

app = Flask(_name_)

@app.route('/')
def home():
    return "Home Page"

@app.route('/go')
def go():
    return redirect('/')   # redirect to home

if _name_ == '_main_':
    app.run(debug=True)