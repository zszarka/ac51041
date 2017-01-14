import os
import json
import uuid
from flask import Flask, redirect, url_for, request, render_template, session, escape,jsonify
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
from redis import StrictRedis

#V2_
REDIS_HOST = os.environ['V2_SESSION_DB_1_PORT_6379_TCP_ADDR']
REDIS_PORT = 6379

app = Flask(__name__)
CORS(app)
app.secret_key="kjhdsa89s9dx34"

redis_db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)

client = MongoClient(os.environ['V2_LOGIN_DB_1_PORT_27017_TCP_ADDR'], 27017)
db = client.login


@app.route('/')
def todo():

	_user_items = db.users.find()
	user_items = [item for item in _user_items]

	return render_template('login.html', msg = 'none')

@app.route('/filter_cat', methods=['POST'])
def filter_cat():

	if request.form['cat']=="all":
		_user_items =  db.users.find()
	else:
		_user_items = db.users.find({"video.category":request.form['cat']})
	user_items = [item for item in _user_items]

	return render_template('todo.html', items=(user_items))

@app.route('/logout')
def logout():
	session_id = session['id']
	redis_db.delete(session_id)
	return render_template('login.html', msg = 'logout')

@app.route('/register')
def register():	
	return render_template('register.html')
#	return redirect(url_for('todo'))

@app.route('/new_user',methods=['POST'])
def new_user():
	email=request.form['email']		
	item_doc = {
		'email': request.form['email'],
		'pw': request.form['pw'],
		'name' : request.form['user_name'],
		'dob' : request.form['dob']
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
	return render_template('account.html', user = [user,session_id])

@app.route('/login', methods=['POST'])
def login():
	email=request.form['email']
	pw=request.form['pw']
	user = db.users.find_one({"email":email})
#	if there is no result, set user to null
	try:
		user
	except NameError:
		user = None		
	if user == None:
#		user does not exist. Back to login
		return render_template('login.html',msg = "not_exist")
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
			return render_template('account.html', user = [user,session_id])
		else:
#			incorrect password. Back to login
			return render_template('login.html',msg = "wrong_password")
#	return json.dumps({'status':'OK','user':email,'pass':pw,'service':'login'});

@app.route('/test', methods=['GET','POST'])
def test():
	email = request.form['email']
	pw=request.form['pw']
#	email = "sam"
#	pw="pass"
	user = db.users.find_one({"email":email})
#	if there is no result, set user to null
	try:
		user
	except NameError:
		user = None		
	if user == None:
#		user does not exist. Back to login
#		return render_template('login.html',msg = "not_exist")
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
#			return render_template('account.html', user = [user,session_id])
#			return json.dumps({'login':'fail'})
			d = {'login':'pass','name':user['name'],'email':user['email'],'session_id':session_id}
			return jsonify(**d)
		else:
#			incorrect password. Back to login
#			return render_template('login.html',msg = "wrong_password")
			return json.dumps({'login':'fail'})
	


if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
