from flask import Flask, request
from flask import Flask, request, render_template
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from test_model import Person

import requests


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

@app.route('/try_rest', methods=['POST'])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)


headers = {
    'Content-Type': 'application/json',
}

name = '{"name:dummy": "age:21", "friends:[dummy1,dummy2,dummy3], "is man:false": "value2"}'

response = requests.post('https://127.0.0.1:5000/try_rest', headers=headers, name=name)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)

@app.route('/show_html')
def show_html():
    return render_template('./test_html.html')


@app.route('/try_rest', methods=['POST'])
def try_rest():
    # リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json": request_json}
    return jsonify(response_json)


@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')


@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)


@app.route('/try_html')
def try_html():
    return render_template('./try_html.html')


@app.route('/show_data', methods=["GET", "POST"])
def show_data():
    return request.form


@app.route('/try_css')
def try_css():
    return render_template('./try_css.html')