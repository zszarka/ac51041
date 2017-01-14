import os
import json
import requests
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

#app.config['SECRET_KEY']='secret'
#app.config[CORS_HEADERS]='Content-Type'
#CORS(app,resources={r"/test/endpoint":{"origins":"*"}})

#client = MongoClient(os.environ['V2_CATALOG_DB_1_PORT_27017_TCP_ADDR'], 27017)
#db = client.myflix

@app.route('/')
def todo():
	var="http://" + os.environ['V2_LOGIN_1_PORT_5000_TCP_ADDR'] + ":5000/test"
	r = requests.post(var, data = {'key':'Hello HTTP'})
	return render_template('todo.html', item=r.text)

#@app.route('/test/endpoint',methods=['POST'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization'])
#def my_test_endpoint():
#	input_json=request.get_json(force=True)
#	# Force= True may not be necessary
#	dictToReturn = {'answer':42}
#	return jsonify(dictToReturn)




if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
