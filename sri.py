from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    message = ""

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        gender = request.form.get('gender')
        course = request.form.get('course')

        # Validation
        if not name or not email:
            message = "Please fill all required fields!"
        else:
            message = f"Hello {name}, you registered successfully!"

    return render_template('form.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)