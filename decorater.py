
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

