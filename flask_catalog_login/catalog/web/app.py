import os
import json
from flask import Flask, redirect, url_for, request, render_template, jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

#app.config['SECRET_KEY']='secret'
#app.config[CORS_HEADERS]='Content-Type'
#CORS(app,resources={r"/test/endpoint":{"origins":"*"}})

client = MongoClient(os.environ['FLASKCATALOGLOGIN_CATALOG_DB_1_PORT_27017_TCP_ADDR'], 27017)
db = client.myflix

@app.route('/')
def todo():

	_video_items = db.videos.find()
	video_items = [item for item in _video_items]

	_category_items = db.categories.find()
	category_items = [item for item in _category_items]

	return render_template('todo.html', items=(category_items,video_items))

#@app.route('/test/endpoint',methods=['POST'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization'])
#def my_test_endpoint():
#	input_json=request.get_json(force=True)
#	# Force= True may not be necessary
#	dictToReturn = {'answer':42}
#	return jsonify(dictToReturn)


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
