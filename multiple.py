from flask import Flask

app = Flask(__name__)

# Multiple URLs for same function
@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    return "This is Home Page"

# Another route
@app.route('/about')
def about():
    return "About Page"

# Multiple routes with variable
@app.route('/user/')
@app.route('/user/<name>')
def user(name=None):
    if name:
        return f"Hello, {name}"
    return "Hello Guest"

if __name__ == '__main__':
    app.run(debug=True)