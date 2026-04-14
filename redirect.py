from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/go')
def go():
    return redirect('/')   # redirect to home

if __name__ == '__main__':
    app.run(debug=True)