import os
import json
from flask import Flask, redirect, url_for, request, render_template
from redis import StrictRedis

REDIS_HOST = os.environ['V2_SESSION_DB_1_PORT_6379_TCP_ADDR']
REDIS_PORT = 6379


app = Flask(__name__)

redis_db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

@app.route('/get_user', methods=['POST'])
def get_user():
#	ids = "not_logged_in"
#	ids = redis_db.hget( request.form['session_id'],'email')
#	return json.dumps({'email':ids})
	email = "not_logged_in"
	session_id = request.form['session_id']
	email = redis_db.hget(session_id,'email')
	return json.dumps({'email':email})


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)