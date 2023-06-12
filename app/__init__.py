from flask import Flask,json,request
from flask_cors import CORS

from utils.openai import create_openai

app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/ps_api')
def index():
    data1 = request.get_data()
    data = json.loads(data1)
    content = data.get('content')

    res = create_openai(content)
    return 'Hello %s!' % res

