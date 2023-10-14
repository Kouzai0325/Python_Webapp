from flask import Flask, request
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route('/')
def inex():
    return 'Response Data'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'

@app.route('/en_request')
def en_request():
    return f'exercise_request:{request.query_string("")}'

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise_html')
def exercise_html():
    return render_template('exercise.html')

@app.route('/exercise')
def answer_html():
    return render_template('answer.html', name=request.args.get("my_name"))