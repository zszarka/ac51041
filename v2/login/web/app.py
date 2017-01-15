import os
import json
import uuid
from flask import Flask, redirect, url_for, request, render_template, session, escape,jsonify
from pymongo import MongoClient
#from flask_cors import CORS, cross_origin
from redis import StrictRedis

#V2_
REDIS_HOST = os.environ['V2_SESSION_DB_1_PORT_6379_TCP_ADDR']
REDIS_PORT = 6379

app = Flask(__name__)
#CORS(app)
app.secret_key="kjhdsa89s9dx34"

redis_db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

client = MongoClient(os.environ['V2_LOGIN_DB_1_PORT_27017_TCP_ADDR'], 27017)
db = client.login


@app.route('/logout', methods=['POST'])
def logout():
	session_id = request.form['session_id']
	redis_db.delete(session_id)
	return json.dumps({'session_id':session_id})

@app.route('/register',methods=['POST'])
def register():
	email=request.form['email']		
	item_doc = {
		'email': request.form['email'],
		'pw': request.form['pw'],
		'name' : request.form['user_name'],
		'dob_d' : request.form['dob_d'],
		'dob_m' : request.form['dob_m'],
		'dob_y' : request.form['dob_y']
	}
#	save to mongo
	db.users.insert_one(item_doc)
#	retrieve from mongo
	user = db.users.find_one({"email":email})
#	setup session dict and save to redis
	session['email'] = email
	session['id'] = uuid.uuid4()
	redis_db.hmset(session['id'],session )
	session_id = redis_db.hget(session['id'],'id')
	d = {'success':'ok','name':user['name'],'email':user['email'],'session_id':session_id}
	add_key_if_exist(user, d, 'dob_d')
	add_key_if_exist(user, d, 'dob_m')
	add_key_if_exist(user, d, 'dob_y')
	return jsonify(**d)

@app.route('/login', methods=['GET','POST'])
def login():
	email = request.form['email']
	pw=request.form['pw']
	user = db.users.find_one({"email":email})
#	if there is no result, set user to null
	try:
		user
	except NameError:
		user = None		
	if user == None:
#		user does not exist. Back to login
		return json.dumps({'login':'fail'})
	else:
		if user['pw'] == pw:
#			correct password. insert session into redis. Show account
			session['email'] = email
			session['id'] = uuid.uuid4()
#			redis_db.set("email", email)
			redis_db.hmset(session['id'],session )
#			set expiry using expire
#			redis_db.expire(session['id'],60)
#			test session id by retrieving
			session_id = redis_db.hget(session['id'],'id')
#			prepare return json
			d = {'login':'pass','name':user['name'],'email':user['email'],'session_id':session_id}
			add_key_if_exist(user, d, 'dob_d')
			add_key_if_exist(user, d, 'dob_m')
			add_key_if_exist(user, d, 'dob_y')
#			user['login'] = 'pass'
			return jsonify(**d)
		else:
#			incorrect password. Back to login
			return json.dumps({'login':'fail'})
	
def add_key_if_exist(src, dest, key):
	if src.has_key(key):
		dest[key] = src[key]

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
