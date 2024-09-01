# app.py
from flask import Flask, render_template, request
from gen_ai.py import generate_feedback

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    feedback = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        feedback = generate_feedback(user_input)
    return render_template('index.html', feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)
