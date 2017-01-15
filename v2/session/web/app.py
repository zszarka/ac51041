import os
from flask import Flask, redirect, url_for, request, render_template
from flask_cors import CORS, cross_origin
from redis import StrictRedis

REDIS_HOST = os.environ['V2_SESSION_DB_1_PORT_6379_TCP_ADDR']
REDIS_PORT = 6379


app = Flask(__name__)
CORS(app)

redis_db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

#@app.route('/')
#def todo():

#	redis_db.set("name", "zsolt")
#	var = redis_db.get("name")
#	return render_template('todo.html', item=var)

@app.route('/get_user', methods=['POST'])
def get_user():
	user_email = redis_db.hget( request.form['session_id'],'email')
	return json.dumps({'email':user_email})

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)