from flask import Flask,json,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/ps_api')
def index():
    data1 = request.get_data()
    data = json.loads(data1)
    uuid = data.get('uuid')
    current_id = data.get('current_id')
    return 'Hello %s and %s!' % (uuid,current_id)

