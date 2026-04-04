from flask import Flask

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to Home Page"

# About route
@app.route('/about')
def about():
    return "This is About Page"

# Dynamic route
@app.route('/user/<name>')
def user(name):
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)