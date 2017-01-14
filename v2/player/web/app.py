import os
import json
import requests
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

login_url ="http://" + os.environ['V2_LOGIN_1_PORT_5000_TCP_ADDR'] + ":5000/test"

@app.route('/player')
def player():
#	dictToSend={'question':'What is the answer?'}
#	res = requests.post('http://localhost:15000/test/endpoint',json = dictToSend)
#	resText = res.text
#	dictFromServer=res.json()
	return render_template('player.html')


@app.route('/login', methods=['POST'])
def login():
	cred = {
		'email': request.form['email'],
		'pw': request.form['pw']
	}	
	res = requests.post(login_url, data = cred)
	r = res.json()
	if r['login'] == "pass":	
		return render_template('account.html', user = r['name'] )
	else:
		return redirect(url_for('index'))
#	return render_template('account.html', user = r.text )

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/filter_cat', methods=['POST'])
def filter_cat():

	if request.form['cat']=="all":
		_video_items =  db.videos.find()
	else:
		_video_items = db.videos.find({"video.category":request.form['cat']})
	video_items = [item for item in _video_items]

	_category_items = db.categories.find()
	category_items = [item for item in _category_items]

	return render_template('todo.html', items=(category_items,video_items))


@app.route('/new', methods=['POST'])
def new():

#	f=request.files['img']
#	fname=f.filename
#	save not working	
#	path_and_file = url_for('static', filename=fname)
#	fullname = f.save(path_and_file)
#	print(fullname)

#	item_doc = {
#		'name': request.form['title'],
#		'description': request.form['description'],
#		'source' : "Flask App",
#		'thumb' : fname
#	}
#	db.todo.insert_one(item_doc)
	return redirect(url_for('todo'))

@app.route('/test', methods=['POST'])
def test():
	return json.dumps({'status':'OK','user':'zsolt','pass':'password'});



if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
