from flask import Flask, render_template, request, redirect, url_for
from flask import *
from form import userform
#from flaskwebgui import FlaskUI
from flask import abort
import sqlite3
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

@app.route("/view")  
def view():  
    con = sqlite3.connect("GEMSCAP_TABLE.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from gemscap_table")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)

@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            EmployeeID = request.form["EmployeeID"]  
            FirstName = request.form["FirstName"]  
            MiddleName = request.form["MiddleName"]
            LastName = request.form["LastName"]
            FatherName = request.form["FatherName"]
            MotherName = request.form["MotherName"]  
            DOB = request.form["DOB"]
            Gender = request.form["Gender"]
            MaritialStatus = request.form["MaritialStatus"]
            PermanentAddress = request.form["PermanentAddress"]
            LocalAddress = request.form["LocalAddress"]
            EmailAddress = request.form["EmailAddress"]
            ContactNumber1 = request.form["ContactNumber1"]
            ContactNumber2 = request.form["ContactNumber2"]
            FamilyPersonsName1 = request.form["FamilyPersonsName1"]
            FamilyPersonsContactNumber1 = request.form["FamilyPersonsContactNumber1"]
            FamilyPersonsRelationWithEmployee1 = request.form["FamilyPersonsRelationWithEmployee1"]
            FamilyPersonsName2 = request.form["FamilyPersonsName2"]
            FamilyPersonsContactNumber2 = request.form["FamilyPersonsContactNumber2"]
            FamilyPersonsRelationWithEmployee2 = request.form["FamilyPersonsRelationWithEmployee2"]
            AadharCard = request.form["AadharCard"]
            PanCard = request.form["PanCard"]
            EductionalCourseDetail = request.form["EductionalCourseDetail"]
            PassingYear = request.form["PassingYear"]
            PassingStatus = request.form["PassingStatus"]
            PFNomineeName = request.form["PFNomineeName"]
            PFNomineeRelation = request.form["PFNomineeRelation"]
            PFNomineeDOB = request.form["PFNomineeDOB"]
            DateOfJoining = request.form["DateOfJoining"]
            DateOfResigning = request.form["DateOfResigning"]
            AccountNumber1 = request.form["AccountNumber1"]
            IFSCcode1 = request.form["IFSCcode1"]
            BankName1 = request.form["BankName1"]
            AccountType1 = request.form["AccountType1"]
            AccountHolderName1 = request.form["AccountHolderName1"]
            AccountNumber2 = request.form["AccountNumber2"]
            IFSCcode2 = request.form["IFSCcode2"]
            BankName2 = request.form["BankName2"]
            AccountType2 = request.form["AccountType2"]
            AccountHolderName2 = request.form["AccountHolderName2"]
            with sqlite3.connect("GEMSCAP_TABLE.db") as con:  
                cur = con.cursor() 
                cur.execute('''CREATE TABLE IF NOT EXISTS gemscap_table(   
				EmployeeID TEXT NOT NULL,
				FirstName TEXT NOT NULL,
				MiddleName TEXT NOT NULL,
				LastName TEXT NOT NULL,
				FatherName TEXT NOT NULL,
				MotherName TEXT NOT NULL,
				DOB TEXT NOT NULL,
				Gender TEXT NOT NULL,
				MaritialStatus TEXT NOT NULL,
				PermanentAddress TEXT NOT NULL,
				LocalAddress TEXT NOT NULL,
				EmailAddress TEXT NOT NULL,
				ContactNumber1 INTEGER,
				ContactNumber2 INTEGER,
				FamilyPersonsName1 TEXT NOT NULL,
				FamilyPersonsContactNumber1 INTEGER,
				FamilyPersonsRelationWithEmployee1 TEXT NOT NULL,
				FamilyPersonsName2 TEXT NOT NULL,
				FamilyPersonsContactNumber2 TEXT NOT NULL,
				FamilyPersonsRelationWithEmployee2 TEXT NOT NULL,
				AadharCard TEXT NOT NULL,
				PanCard TEXT NOT NULL,
				EductionalCourseDetail TEXT NOT NULL,
				PassingYear INTEGER,
				PassingStatus TEXT NOT NULL,
				PFNomineeName TEXT NOT NULL,
				PFNomineeRelation TEXT NOT NULL,
				PFNomineeDOB TEXT NOT NULL,
				DateOfJoining TEXT NOT NULL,
				DateOfResigning TEXT NOT NULL,
				AccountNumber1 TEXT NOT NULL,
				IFSCcode1 TEXT NOT NULL,
				BankName1 TEXT NOT NULL,
				AccountType1 TEXT NOT NULL,
				AccountHolderName1 TEXT NOT NULL,
				AccountNumber2 TEXT NOT NULL,
				IFSCcode2 TEXT NOT NULL,
				BankName2 TEXT NOT NULL,
				AccountType2 TEXT NOT NULL,
				AccountHolderName2 TEXT NOT NULL
				) 
				''') 
                cur.execute("INSERT INTO gemscap_table (EmployeeID,FirstName,MiddleName,LastName,FatherName,MotherName,DOB,Gender,MaritialStatus,PermanentAddress,LocalAddress,EmailAddress,ContactNumber1,ContactNumber2,FamilyPersonsName1,FamilyPersonsContactNumber1,FamilyPersonsRelationWithEmployee1,FamilyPersonsName2,FamilyPersonsContactNumber2,FamilyPersonsRelationWithEmployee2,AadharCard,PanCard,EductionalCourseDetail,PassingYear,PassingStatus,PFNomineeName,PFNomineeRelation,PFNomineeDOB,DateOfJoining,DateOfResigning,AccountNumber1,IFSCcode1,BankName1,AccountType1,AccountHolderName1,AccountNumber2,IFSCcode2,BankName2,AccountType2,AccountHolderName2) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (EmployeeID,FirstName,MiddleName,LastName,FatherName,MotherName,DOB,Gender,MaritialStatus,PermanentAddress,LocalAddress,EmailAddress,ContactNumber1,ContactNumber2,FamilyPersonsName1,FamilyPersonsContactNumber1,FamilyPersonsRelationWithEmployee1,FamilyPersonsName2,FamilyPersonsContactNumber2,FamilyPersonsRelationWithEmployee2,AadharCard,PanCard,EductionalCourseDetail,PassingYear,PassingStatus,PFNomineeName,PFNomineeRelation,PFNomineeDOB,DateOfJoining,DateOfResigning,AccountNumber1,IFSCcode1,BankName1,AccountType1,AccountHolderName1,AccountNumber2,IFSCcode2,BankName2,AccountType2,AccountHolderName2))

                con.commit()  
                msg = "Employee successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:
        	return render_template('after_user.html', msg = msg)
        	con.close()


if __name__ == "__main__":
    app.run(debug = True)
    #ui.run()