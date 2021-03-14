from flask import Flask,jsonify,request
from flask_cors import CORS
from services import loginService
import json
from flask_socketio import SocketIO


#configuration
DEBUG = True

#instantiate app
app =  Flask(__name__)
app.config['SECRET_KEY'] = 'myKey!'
app.config.from_object(__name__)
socketio = SocketIO(app,cors_allowed_origins='http://localhost:8080')

#enable CORS
CORS(app, resources={r'/*':{'origins':'*'}})

#sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/login' , methods=['GET','POST'])
def login():
    try:
        resultObj = {}
        postParams = request.json
        resultObj["data"] = loginService.login(postParams)
        resultObj["status"] = "success"
        return jsonify(resultObj)
    except Exception as e:
        resultObj["status"] = "error"
        resultObj["message"] = str(e)
        return jsonify(resultObj)


@socketio.on('pingServer')
def pingServer(json,methods=['GET','POST']):
    print(json)

if __name__ == '__main__':
    socketio.run(app)