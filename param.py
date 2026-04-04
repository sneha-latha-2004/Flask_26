from flask import Flask

app = Flask(__name__)

# Multiple parameters
@app.route('/user/<name>/<int:age>')
def user(name, age):
    return f"Name: {name}, Age: {age}"

if __name__ == '__main__':
    app.run(debug=True)