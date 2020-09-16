import sqlite3

def createMONTHLYTABLE():
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor() 
    cur.execute('DROP TABLE MONTHLYTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS MONTHLYTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO MONTHLYTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key canstraint")
    
    cur.execute('UPDATE MONTHLYTABLE SET (Jan,Feb) = ({},{}) where TAKIONID=12324'.format(100,200))

    con.commit()
    con.close()


def createPaidtable():
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    cur.execute('DROP TABLE PAIDTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS PAIDTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO PAIDTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key constraint")
    con.commit()
    con.close()

def createQuantitytable():
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    cur.execute('DROP TABLE QUANTITYTABLE')
    cur.execute('''CREATE TABLE IF NOT EXISTS QUANTITYTABLE (TAKIONID INT PRIMARY KEY, Jan FLOAT DEFAULT 0, Feb FLOAT DEFAULT 0, Mar FLOAT DEFAULT 0, Apr FLOAT DEFAULT 0
    , May FLOAT DEFAULT 0, Jun FLOAT DEFAULT 0, Jul FLOAT DEFAULT 0, Aug FLOAT DEFAULT 0, Sep FLOAT DEFAULT 0, Oct FLOAT DEFAULT 0,
     Nov FLOAT DEFAULT 0, Dec FLOAT DEFAULT 0)''')
    try:
        cur.execute('''INSERT INTO QUANTITYTABLE (TAKIONID) SELECT TakionID FROM gemscap_table ''')
    except:
        print("Takionid primary key constraint")
    con.commit()
    con.close()

def updateQuantitytable(month):
    print("inside updateQuantitytable")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()
    cur.execute(''' UPDATE QUANTITYTABLE
                    SET
                    {} = {} + (SELECT EXCELTABLE.QUANTITY 
                               FROM EXCELTABLE
                               WHERE EXCELTABLE.TAKIONID = QUANTITYTABLE.TAKIONID)
                    WHERE
                    EXISTS (
                    SELECT *
                    FROM EXCELTABLE
                    WHERE EXCELTABLE.TAKIONID = QUANTITYTABLE.TAKIONID)'''.format(month,month))
    cur.execute(''' UPDATE gemscap_table
                    SET
                    Qty = Qty + (SELECT EXCELTABLE.QUANTITY 
                               FROM EXCELTABLE
                               WHERE EXCELTABLE.TAKIONID = gemscap_table.TAKIONID)
                    WHERE
                    EXISTS (
                    SELECT *
                    FROM EXCELTABLE
                    WHERE EXCELTABLE.TAKIONID = gemscap_table.TAKIONID)''')
    con.commit()
    con.close()

def updateMONTHLYTABLE(month):
    month = str(month)
    print("inside updateMONTHLYTABLE")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()

    cur.execute('''UPDATE MONTHLYTABLE 
                    SET
      {} = {} + (SELECT EXCELTABLE.NetPay 
                            FROM EXCELTABLE
                            WHERE EXCELTABLE.TAKIONID = MONTHLYTABLE.TAKIONID )
    WHERE
        EXISTS (
            SELECT *
            FROM EXCELTABLE
            WHERE EXCELTABLE.TAKIONID = MONTHLYTABLE.TAKIONID)'''.format(month,month))

    con.commit()
    con.close()

def updatePAIDTABLE(month,payment,tk):
    month = str(month)
    payment=float(payment)
    tk=int(tk)
    print("inside updatePAIDTABLE")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()

    cur.execute('UPDATE PAIDTABLE SET {} = {} where TAKIONID = {}'.format(month,payment,tk) )        #payment works once only + not working
    cur.execute('UPDATE gemscap_table SET CarryForwardBalance = CarryForwardBalance - {} WHERE TakionID = {}'.format(payment,tk) )

    con.commit()
    con.close()

##########    15 september for adjusting cfb of a takionid
def adjustcfbingemscap_adjustmonthlytable(tk,amount,month):
    print('INSIDE adjustcfbingemscap_adjustmonthlytable')
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor()

    cur.execute('UPDATE gemscap_table SET CarryForwardBalance = CarryForwardBalance + {} WHERE Takionid = {}'.format(amount,tk))
    cur.execute('UPDATE MONTHLYTABLE SET {} = {} + {} WHERE TAKIONID = {}'.format(month,month,amount,tk))

    con.commit()
    con.close()


# createMONTHLYTABLE()   figure out how to call this func once
# createPaidtable()
# createQuantitytable()


# updateMONTHLYTABLE('Feb')
# updatePAIDTABLE('Feb',200,12324)

