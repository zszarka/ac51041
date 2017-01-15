import os
import json
from flask import Flask, redirect, url_for, request, render_template, jsonify, Response
from pymongo import MongoClient
from bson import json_util

app = Flask(__name__)

client = MongoClient(os.environ['V2_CATALOG_DB_1_PORT_27017_TCP_ADDR'], 27017)
db = client.myflix



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

@app.route('/filter_cat', methods=['POST'])
def filter_cat():
	if request.form['cat']=="all":
		video_items = list(db.videos.find())
	else:
		video_items = list(db.videos.find({"video.category":request.form['cat']}))

	category_items = list(db.categories.find())
	d={'cat':category_items,'vid':video_items}
#	return toJson(_video_items)
	return json.dumps(d, default=json_util.default)
#	return jsonify(**d)


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
