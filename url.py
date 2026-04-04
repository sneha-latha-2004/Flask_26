from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Home Page"

@app.route('/about')
def about():
    return "About Page"

@app.route('/link')
def link():
    # generate URL using function name
    home_url = url_for('home')
    about_url = url_for('about')
    return f"Home URL: {home_url} | About URL: {about_url}"

if __name__ == '__main__':
    app.run(debug=True)