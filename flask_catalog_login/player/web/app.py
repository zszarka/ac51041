import os
import json
import requests
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

client = MongoClient(os.environ['FLASKCATALOGLOGIN_CATALOG_DB_1_PORT_27017_TCP_ADDR'], 27017)
db = client.myflix


@app.route('/player')
def player():
#	dictToSend={'question':'What is the answer?'}
#	res = requests.post('http://localhost:15000/test/endpoint',json = dictToSend)
#	resText = res.text
#	dictFromServer=res.json()
	return render_template('player.html')


@app.route('/')
def todo():

	_video_items = db.videos.find()
	video_items = [item for item in _video_items]

	_category_items = db.categories.find()
	category_items = [item for item in _category_items]

	return render_template('todo.html', items=(category_items,video_items))

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
