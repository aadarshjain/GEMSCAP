from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, DateField, validators, ValidationError
from wtforms.fields.html5 import EmailField

class userform(FlaskForm):
    EmployeeID = StringField('Employee ID' , validators=[validators.DataRequired()])
    FirstName = StringField('First Name' , validators=[validators.DataRequired()])
    MiddleName = StringField('Middle Name' , validators=[validators.DataRequired()])
    LastName = StringField('Last Name' , validators=[validators.DataRequired()])
    FatherName = StringField('Father Name' , validators=[validators.DataRequired()])
    MotherName = StringField('Mother Name' , validators=[validators.DataRequired()])
    DOB = DateField('Date of Birth', format="%Y-%m-%d", validators=(validators.Optional(),))
    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female'),('O','Other')])
    MaritialStatus = RadioField('Maritial Status', choices = [('M','Married'),('U','Unmarried'),('O','Other') ] )
    
    PermanentAddress = StringField('Permanent Address' , validators=[validators.DataRequired()])
    LocalAddress = StringField('Local Address' , validators=[validators.DataRequired()])
    EmailAddress = EmailField('Email address', [validators.DataRequired(), validators.Email()])

    ContactNumber1 = StringField('Contact Number 1',validators=[validators.DataRequired(),validators.Regexp(regex=r'^(\+91){1}[1-9]{1}[0-9]{9}$', message="MOBILE NO STARTING WITH +91")])
    ContactNumber2 = StringField('Contact Number 2',validators=[validators.DataRequired(),validators.Regexp(regex=r'^(\+91){1}[1-9]{1}[0-9]{9}$', message="MOBILE NO STARTING WITH +91")])
    FamilyPersonsName1 = StringField('Family Person Name 1' , validators=[validators.DataRequired()])
    FamilyPersonsContactNumber1 = StringField('Family Persons Contact Number' , validators=[validators.DataRequired()])
    FamilyPersonsRelationWithEmployee1 = StringField('Family Persons Relation With Employee' , validators=[validators.DataRequired()])
    FamilyPersonsName2 = StringField('Family Person Name 2' , validators=[validators.DataRequired()])
    FamilyPersonsContactNumber2 = StringField('Family Persons Contact Number 2' , validators=[validators.DataRequired()])
    FamilyPersonsRelationWithEmployee2 = StringField('Family Persons Relation With Employee 2' , validators=[validators.DataRequired()])
    AadharCard=StringField('Aadhar Card No',validators=[validators.DataRequired(),validators.Regexp(regex=r'^([0-9]){12}$', message="12 DIGIT AADHAR NUMBER IS MUST")])
    PanCard=StringField('Pan Card No',validators=[validators.DataRequired(),validators.Regexp(regex=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$', message="Pan No should be 5LETTERS + 4NUMS + 1LETTER")])
    EductionalCourseDetail=StringField('Eductional Course Detail' , validators=[validators.DataRequired()])
    PassingYear=StringField('Passing Year' , validators=[validators.DataRequired()])
    PassingStatus=StringField('Passing Status' , validators=[validators.DataRequired()])
    PFNomineeName=StringField('PF Nominee Name' , validators=[validators.DataRequired()])
    PFNomineeRelation=StringField('PF Nominee Relation' , validators=[validators.DataRequired()])
    PFNomineeDOB=StringField('PF Nominee DOB' , validators=[validators.DataRequired()])
    DateOfJoining=StringField('Date Of Joining' , validators=[validators.DataRequired()])
    DateOfResigning=StringField('Date Of Resigning' , validators=[validators.DataRequired()])
    AccountNumber1 = StringField('Account Number 1',validators=[validators.DataRequired(),validators.Regexp(regex=r'^[0-9]{9,18}$', message="")])
    IFSCcode1 = StringField('IFSC Code' , validators=[validators.DataRequired()])
    BankName1 = StringField('Bank Name' , validators=[validators.DataRequired()])
    AccountType1 = StringField('Account Type' , validators=[validators.DataRequired()])
    AccountHolderName1 = StringField('Account Holder Name' , validators=[validators.DataRequired()])
    AccountNumber2 = StringField('Account Number 2',validators=[validators.DataRequired(),validators.Regexp(regex=r'^[0-9]{9,18}$', message="")])
    IFSCcode2 = StringField('IFSC Code' , validators=[validators.DataRequired()])
    BankName2 = StringField('Bank Name' , validators=[validators.DataRequired()])
    AccountType2 = StringField('Account Type' , validators=[validators.DataRequired()]) 
    AccountHolderName2 = StringField('Account Holder Name' , validators=[validators.DataRequired()])


###############################submit
    submit = SubmitField('Submit')