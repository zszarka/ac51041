import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ['CATALOG_DB_1_PORT_27017_TCP_ADDR'], 27017)
db = client.tododb


@app.route('/')
def todo():

	_items = db.tododb.find()
	items = [item for item in _items]
#	results = request.post("http://127.0.0.1:8080")
	return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():

	f=request.files['img']
	fname=f.filename
#	save not working	
#	path_and_file = url_for('static', filename=fname)
#	fullname = f.save(path_and_file)
#	print(fullname)

	item_doc = {
		'name': request.form['title'],
		'description': request.form['description'],
		'source' : "Flask App",
		'thumb' : fname
	}
	db.tododb.insert_one(item_doc)
	return redirect(url_for('todo'))

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
