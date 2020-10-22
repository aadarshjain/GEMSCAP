import sqlite3

def createMONTHLYTABLE():
    print("createMONTHLYTABLE")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor() 
    #cur.execute('DROP TABLE MONTHLYTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS MONTHLYTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO MONTHLYTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key canstraint")
    
    #cur.execute('UPDATE MONTHLYTABLE SET (Jan,Feb) = ({},{}) where TAKIONID=12324'.format(100,200))

    con.commit()
    con.close()

#######################################################################################################

def createPaidtable():
    print("createPaidtable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    #cur.execute('DROP TABLE PAIDTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS PAIDTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO PAIDTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key constraint")
    con.commit()
    con.close()

#######################################################################################################

def createQuantitytable():
    print("createQuantitytable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    #cur.execute('DROP TABLE QUANTITYTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS QUANTITYTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO QUANTITYTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key constraint")
    con.commit()
    con.close()

#######################################################################################################

def createtotaltable():
    print("createtotaltable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    #cur.execute('DROP TABLE TOTALTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS TOTALTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO TOTALTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key constraint")
    con.commit()
    con.close()

#######################################################################################################


####################################    27 sept
def createdeluser():
    print("createdeluser creating")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor() 
    #cur.execute('DROP TABLE deluser')
    cur.execute('''CREATE TABLE IF NOT EXISTS deluser(   
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
				City1 TEXT NOT NULL,
				Pincode1 INTEGER NOT NULL,
				Country1 TEXT NOT NULL,
				LocalAddress TEXT NOT NULL,
				City2 TEXT NOT NULL,
				Pincode2 INTEGER NOT NULL,
				Country2 TEXT NOT NULL,
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
				AccountHolderName2 TEXT NOT NULL,
				TakionID TEXT NOT NULL,
				StartingBalance TEXT NOT NULL,
				PolicyNumber TEXT NOT NULL,
				CarryForwardBalance TEXT NOT NULL,
				RateOfDollar TEXT NOT NULL,
				Qty INT DEFAULT 0,
				Total FLOAT DEFAULT 0) ''')
    con.commit()
    con.close()


###############################################################################################


createMONTHLYTABLE()   #figure out how to call this all create func once
createPaidtable()
createQuantitytable()

# updateMONTHLYTABLE('Feb')
# updatePAIDTABLE('Feb',200,12324)

createtotaltable()

createdeluser()