from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, DateField, validators, ValidationError,SelectField
from wtforms.fields.html5 import EmailField

class userform(FlaskForm):
    EmployeeID = StringField('Employee ID' , validators = [validators.DataRequired()])
    FirstName = StringField('First Name' , validators = [validators.DataRequired()])
    MiddleName = StringField('Middle Name')
    LastName = StringField('Last Name' , validators = [validators.DataRequired()])
    FatherName = StringField('Father Name' , validators = [validators.DataRequired()])
    MotherName = StringField('Mother Name' , validators = [validators.DataRequired()])
    #DOB = DateField('Date of Birth', format = "%m/%d/%Y", validators = (validators.Optional(),))
    DOB = StringField('Date Of Birth', validators = [validators.DataRequired()])
    Gender = RadioField('Gender', choices = [('M','Male'), ('F','Female'), ('O','Other')])
    MaritialStatus = RadioField('Maritial Status', choices = [('M','Married'),('U','Unmarried'),('O','Other') ] )
    PermanentAddress = StringField('Permanent Address' , validators = [validators.DataRequired()])
    City1 = StringField('City', validators = [validators.DataRequired()])
    Pincode1 = StringField('Pin Code', validators = [validators.DataRequired()])
    Country1 = StringField('Country', validators = [validators.DataRequired()])
    LocalAddress = StringField('Local Address' , validators=[validators.DataRequired()])
    City2 = StringField('City', validators = [validators.DataRequired()])
    Pincode2 = StringField('Pin Code', validators = [validators.DataRequired()])
    Country2 = StringField('Country', validators = [validators.DataRequired()])
    EmailAddress = EmailField('Email address', [validators.DataRequired(), validators.Email()])
    ContactNumber1 = StringField('Contact Number 1',validators = [validators.DataRequired(), validators.Regexp(regex = r'^(\+91){1}[1-9]{1}[0-9]{9}$', message = "MOBILE NO STARTING WITH +91")])
    ContactNumber2 = StringField('Contact Number 2')
    FamilyPersonsName1 = StringField('Family Person Name 1', validators = [validators.DataRequired()])
    FamilyPersonsContactNumber1 = StringField('Family Persons Contact Number', validators = [validators.DataRequired()])
    FamilyPersonsRelationWithEmployee1 = StringField('Family Persons Relation With Employee', validators = [validators.DataRequired()])
    FamilyPersonsName2 = StringField('Family Person Name 2', validators = [validators.DataRequired()])
    FamilyPersonsContactNumber2 = StringField('Family Persons Contact Number 2', validators = [validators.DataRequired()])
    FamilyPersonsRelationWithEmployee2 = StringField('Family Persons Relation With Employee 2', validators = [validators.DataRequired()])
    AadharCard = StringField('Aadhar Card No',validators = [validators.DataRequired(), validators.Regexp(regex = r'^([0-9]){12}$', message = "12 DIGIT AADHAR NUMBER IS MUST")])
    PanCard = StringField('Pan Card No',validators = [validators.DataRequired(), validators.Regexp(regex = r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', message = "PAN No should be 5 LETTERS + 4 NUMS + 1 LETTER")])
    EductionalCourseDetail = StringField('Eductional Course Detail', validators = [validators.DataRequired()])
    PassingYear = StringField('Passing Year', validators = [validators.DataRequired()])
    PassingStatus = StringField('Passing Status', validators = [validators.DataRequired()])
    PFNomineeName = StringField('PF Nominee Name', validators = [validators.DataRequired()])
    PFNomineeRelation = StringField('PF Nominee Relation', validators = [validators.DataRequired()])
    PFNomineeDOB = StringField('PF Nominee DOB', validators = [validators.DataRequired()])
    DateOfJoining = StringField('Date Of Joining', validators = [validators.DataRequired()])
    DateOfResigning = StringField('Date Of Resigning')
    AccountNumber1 = StringField('Account Number 1', validators = [validators.DataRequired(), validators.Regexp(regex = r'^[0-9]{9,18}$', message = "")])
    IFSCcode1 = StringField('IFSC Code', validators = [validators.DataRequired()])
    BankName1 = StringField('Bank Name', validators = [validators.DataRequired()])
    AccountType1 = StringField('Account Type' , validators = [validators.DataRequired()])
    AccountHolderName1 = StringField('Account Holder Name', validators = [validators.DataRequired()])
    AccountNumber2 = StringField('Account Number 2', [validators.Regexp(regex = r'^[0-9]{9,18}$', message="")])
    IFSCcode2 = StringField('IFSC Code')
    BankName2 = StringField('Bank Name')
    AccountType2 = StringField('Account Type') 
    AccountHolderName2 = StringField('Account Holder Name')
    TakionID = StringField('Takion ID', validators = [validators.DataRequired()])
    StartingBalance = StringField('Starting Balance', validators = [validators.DataRequired()])
    PolicyNumber = RadioField('PolicyNumber', choices = [('0','70%'), ('1','85%')], validators = [validators.DataRequired()])
    CarryForwardBalance = StringField('Carry Forward Balance')
    RateOfDollar = StringField('Rate of Dollar', validators = [validators.DataRequired()])

    submit = SubmitField('Submit')

class printdata(FlaskForm):
    EmployeeAccNo = StringField('ENTER EMPLOYEE\'S GEMSCAP ID')

class updateExcel(FlaskForm):
    Months = [ ('Jan', 'Jan'), 
               ('Feb', 'Feb'),
               ('Mar', 'Mar'),
               ('Apr', 'Apr'),
               ('May', 'May'),
               ('Jun', 'Jun'),
               ('Jul', 'Jul'),
               ('Aug', 'Aug'),
               ('Sep', 'Sep'),
               ('Oct', 'Oct'),
               ('Nov', 'Nov'),
               ('Dec', 'Dec')
            ]
    Month = SelectField('MONTHS', choices = Months)
    Excel = StringField('ENTER FILE NAME')

class paidDetails(FlaskForm):
    Paid = StringField('ENTER TAKION ID')

class amountToPay(FlaskForm):
    Paida = StringField('RE-ENTER TAKION ID')
    PaidAmount = StringField('ENTER AMOUNT TO PAY')

class payToIndividual(FlaskForm):
    Months = [ ('Jan', 'Jan'), 
               ('Feb', 'Feb'),
               ('Mar', 'Mar'),
               ('Apr', 'Apr'),
               ('May', 'May'),
               ('Jun', 'Jun'),
               ('Jul', 'Jul'),
               ('Aug', 'Aug'),
               ('Sep', 'Sep'),
               ('Oct', 'Oct'),
               ('Nov', 'Nov'),
               ('Dec', 'Dec')
            ]
    Month = SelectField('MONTHS', choices = Months)
    PayAmount = StringField('ENTER AMOUNT TO PAY')
    submit1 = SubmitField('Submit')

class indiMonthlyView(FlaskForm):
    TakionId = StringField('ENTER EMPLOYEE\'S TAKION ID')

class indiPayView(FlaskForm):
    TakionId = StringField('ENTER EMPLOYEE\'S TAKION ID')

class adjustform(FlaskForm):
    Months = [ ('Jan', 'Jan'), 
               ('Feb', 'Feb'),
               ('Mar', 'Mar'),
               ('Apr', 'Apr'),
               ('May', 'May'),
               ('Jun', 'Jun'),
               ('Jul', 'Jul'),
               ('Aug', 'Aug'),
               ('Sep', 'Sep'),
               ('Oct', 'Oct'),
               ('Nov', 'Nov'),
               ('Dec', 'Dec')
            ]
    Month = SelectField('MONTHS', choices = Months)
    Takionid = StringField('ENTER TakionID')
    Amount = StringField('ENTER AMOUNT TO ADJUST')
    submit = SubmitField('Submit')

class updatekyc(FlaskForm):
    TakionID = StringField('Takion ID', validators = [validators.DataRequired()])
    PolicyNumber = RadioField('PolicyNumber', choices = [('0','70%'), ('1','85%')], validators = [validators.DataRequired()])
    ContactNumber2 = StringField('Contact Number 2',validators = [validators.DataRequired(), validators.Regexp(regex = r'^(\+91){1}[1-9]{1}[0-9]{9}$', message = "MOBILE NO STARTING WITH +91")])
    MaritialStatus = RadioField('Maritial Status', choices = [('M','Married'),('U','Unmarried'),('O','Other') ] )
    LocalAddress = StringField('Local Address' , validators=[validators.DataRequired()])
    City2 = StringField('City', validators = [validators.DataRequired()])
    Pincode2 = StringField('Pin Code', validators = [validators.DataRequired()])
    Country2 = StringField('Country', validators = [validators.DataRequired()])
    #PolicyNumber = RadioField('PolicyNumber', choices = [('0','70%'), ('1','85%')], validators = [validators.DataRequired()])
    PFNomineeName = StringField('PF Nominee Name', validators = [validators.DataRequired()])
    PFNomineeRelation = StringField('PF Nominee Relation', validators = [validators.DataRequired()])
    PFNomineeDOB = StringField('PF Nominee DOB', validators = [validators.DataRequired()])
    DateOfResigning = StringField('Date Of Resigning')
    AccountNumber2 = StringField('Account Number 2', [validators.Regexp(regex = r'^[0-9]{9,18}$', message="")])
    IFSCcode2 = StringField('IFSC Code')
    BankName2 = StringField('Bank Name')
    AccountType2 = StringField('Account Type') 
    AccountHolderName2 = StringField('Account Holder Name')
    submit = SubmitField('Submit')

class deleteform(FlaskForm):
    TakionID = StringField('TakionID', validators = [validators.DataRequired()])
    submit = SubmitField('Submit')