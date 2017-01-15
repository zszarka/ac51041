import os
import json
import requests
from flask import Flask, redirect, url_for, request, render_template, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = os.urandom(24)



# test logged in
session_url ="http://" + os.environ['V2_SESSION_1_PORT_5000_TCP_ADDR'] + ":5000/get_user"
@app.route('/test_login')
def test_login():
	sess_id = session['ids']
	dic = {'session_id': sess_id}
	r = requests.post(logout_url, data = dic)	
	return render_template('debug.html', res = r.json() )
#######################################################################################
#CATALOGUE AND PLAY
#######################################################################################

catalog_url ="http://" + os.environ['V2_CATALOG_1_PORT_5000_TCP_ADDR'] + ":5000/filter_cat"

@app.route('/catalog')
def catalog():
	qry = {'cat':'all'}
	res = requests.post(catalog_url, data = qry)
	r = res.json()
	cat = r['cat']
	vid = r['vid']
	return render_template('catalog.html', cat = cat, vid = vid)

@app.route('/filter_cat',methods = ['POST'])
def filter_cat():
	f = request.form['cat']
	qry = {'cat': f }
	res = requests.post(catalog_url, data = qry)
	r = res.json()
	cat = r['cat']
	vid = r['vid']
	return render_template('catalog.html', cat = cat, vid = vid)

@app.route('/player', methods = ['POST'])
def player():
	vid_src = request.form['vid_file_name']	
	img_src = request.form['img_file_name']
	title = request.form['title']		
	return render_template('player.html', vid_src = vid_src, img_src =img_src, title = title )

#######################################################################################
#LOGIN AND ACCOUNT ####################################################################
#######################################################################################

login_url ="http://" + os.environ['V2_LOGIN_1_PORT_5000_TCP_ADDR'] + ":5000/login"
register_url ="http://" + os.environ['V2_LOGIN_1_PORT_5000_TCP_ADDR'] + ":5000/register"
logout_url ="http://" + os.environ['V2_LOGIN_1_PORT_5000_TCP_ADDR'] + ":5000/logout"

@app.route('/logout')
def logout():
	dic = {'session_id': session['ids']}
	r = requests.post(logout_url, data = dic)
	session.pop('ids', None)
	return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
	cred = {
		'email': request.form['email'],
		'pw': request.form['pw'],
		'user_name':request.form['user_name'],
		'dob_d':request.form['dob_d'],
		'dob_m':request.form['dob_m'],
		'dob_y':request.form['dob_y']
	}	
	res = requests.post(register_url, data = cred)
	r = res.json()
	if r['success'] == "ok":
		session['ids'] = r['session_id']	
		return render_template('account.html', user = r )
	else:
		return redirect(url_for('register_form'))

@app.route('/login', methods=['POST'])
def login():
	cred = {
		'email': request.form['email'],
		'pw': request.form['pw']
	}	
	res = requests.post(login_url, data = cred)
	r = res.json()
	if r['login'] == "pass":
		session['ids'] = r['session_id']	
		return render_template('account.html', user = r  )
	else:
		return redirect(url_for('index'))
#	return render_template('account.html', user = r.text )

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/register_form')
def register_form():
	return render_template('register.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
