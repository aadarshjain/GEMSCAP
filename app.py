from flask import Flask, render_template, request, redirect, url_for
from form import userform
#from flaskwebgui import FlaskUI
from flask import abort
import os

app = Flask(__name__)
app.secret_key = 'gemscap'
#ui = FlaskUI(app)

imgFolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = imgFolder

@app.route('/')
def default():
    login_img = os.path.join(app.config['UPLOAD_FOLDER'], 'bglogin.jpg')
    return render_template('login_page.html', first_img = login_img)

database={'admin':'admin'}

@app.route('/login_page.html', methods = ['GET', 'POST'])
def login1():
	login_img = os.path.join(app.config['UPLOAD_FOLDER'], 'bglogin.jpg')
	return render_template('login_page.html', first_img = login_img)

@app.route('/form_login',methods=['GET' , 'POST'])
def login():
	home_img = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
	email = request.form['email']
	password = request.form['password']
	if email not in database:
		return render_template('login_page.html' , info="Invalid Username")
	if database[email] != password:
		return render_template('login_page.html' , info="Invalid Password")
	else:
		return render_template('home.html', second_img = home_img)

@app.route('/home.html',methods=['GET' , 'POST'])
def home():
    return render_template('home.html')

#@app.route('/user_profile.html',methods=['GET','POST'])
#def user_profile():
#	return render_template('user_profile.html')

@app.route('/user_profile.html',methods=['GET','POST'])
####at end change tryform to user_profile 
def userprofile():
    form = userform()
    
    if form.is_submitted():
    	result = request.form
    	print(result)
    ####code for saving too db
    return render_template('user_profile.html',form = form)

@app.route('/after_user.html', methods = ['GET', 'POST'])
def afteruser():
	home_img = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
	return render_template('after_user.html', second_img = home_img)



if __name__ == "__main__":
    app.run(debug = True)
    #ui.run()