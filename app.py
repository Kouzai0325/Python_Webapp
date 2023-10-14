from flask import Flask, request
from flask import Flask, request, render_template
from flask import Flask, request, jsonify



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

import requests

headers = {
    'Content-Type': 'application/json',
}

name = '{"name:dummy": "age:21", "friends:[dummy1,dummy2,dummy3], "is man:false": "value2"}'

response = requests.post('https://127.0.0.1:5000/try_rest', headers=headers, name=name)

 
 def param_func():
    print('引数関数の中')

def body_func(param_func):
	 param_func()

 body_func(param_func)

 def body_func():
	 def return_func():
		 print('戻り値関数の中')
	 return return_func

 return_func = body_func()
 return_func() 

def body_func(param_func):
def return_func():
    param_func()
print('引数関数実行後に文字列を出力')
return return_func
return_func = body_func(param_func)
return_func() 

@body_func
def test_func():
	print('これはテスト関数です')
test_func()
