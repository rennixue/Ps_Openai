from flask import Flask,json,request
from flask_cors import CORS

from chatgpt import create_openai

app = Flask(__name__)
CORS(app, supports_credentials=True)


url = 'http://44.240.140.3:99/ps_api'
headers = {"content-type": "application/json"}
@app.route('/ps_api',methods=['GET','POST'])
def index():
    data1 = request.get_data()
    data = json.loads(data1)
    content = data.get('prompt')


    res = create_openai(content)
    return 'Hello %s!' % res

