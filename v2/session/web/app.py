import os
from flask import Flask, redirect, url_for, request, render_template
from flask_cors import CORS, cross_origin
from redis import StrictRedis

REDIS_HOST = os.environ['V2_SESSION_DB_1_PORT_6379_TCP_ADDR']
REDIS_PORT = 6379


app = Flask(__name__)
CORS(app)

redis_db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

@app.route('/')
def todo():

	redis_db.set("name", "zsolt")
	var = redis_db.get("name")
#	_video_items = 
#	video_items = [item for item in _video_items]
#
#	_category_items = db.categories.find()
#	category_items = [item for item in _category_items]

	return render_template('todo.html', item=var)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)