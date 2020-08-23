from flask import Flask,render_template,request
from flaskwebgui import FlaskUI
from form import userform

app = Flask(__name__)
app.secret_key = 'gemscap'
ui = FlaskUI(app)

@app.route('/')
def login():
    return render_template('login_page.html')

@app.route('/home.html',methods=['POST'])
def home():
    return render_template('home.html')

#@app.route('/user_profile.html',methods=['GET','POST'])
#def user_profile():
#    return render_template('user_profile.html')

@app.route('/user_profile.html',methods=['GET','POST'])
def user_profile():
    form = userform()
    if form.is_submitted():
        result = request.form
        print(result)
    return render_template('user_profile.html',form = form)

@app.route('/after_user.html', methods = ['POST', 'GET'])
def after_user():
	return render_template('after_user.html')

if __name__ == "__main__":
    #app.run()
    ui.run() 