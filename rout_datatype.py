@app.route('/post/<int:id>')
def post(id):
    return f"Post {id}"