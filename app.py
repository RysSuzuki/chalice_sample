import os
from chalice import Chalice
from controller.controller import api
from chalicelib import env

app = Chalice(app_name='handson')
app.register_blueprint(api)

# print(env.get_parameters(os.environ['testuser']))
# print(env.get_parameters(os.environ['testpassword']))

print(env.TESTUSER)
print(env.TESTPASSWORD)

@app.route('/')
def index():
    return {'hello': 'world'}

@app.lambda_function()
def custom_lambda_function001(event, context):
    # Anything you want here.
    return {'body': 'lambda_faction001'}

@app.lambda_function(name='MyFunction')
def other_lambda_function(event, context):
    # Anything you want here.
    return {'body': 'lambda_MyFunction'}

#testコード

#テストコードだよー


def test001():
    # コード追加ブランチ１
    return

def test002():
    # ブランチ２だよー
    return

