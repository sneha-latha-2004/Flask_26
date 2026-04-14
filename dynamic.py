from flask import Flask

app = Flask(__name__)

# Dynamic route with string
@app.route('/user/<sri>')
def user(name):
    return f"Hello, {name}"

# Dynamic route with integer
@app.route('/post/<int:id>')
def post(id):
    return f"Post ID: {id}"

# Optional dynamic route
@app.route('/profile/')
@app.route('/profile/<name>')
def profile(name=None):
    if name:
        return f"Profile of {name}"
    return "No user provided"

if __name__ == '__main__':
    app.run(debug=True)