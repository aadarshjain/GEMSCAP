import xlrd
import sqlite3

TKID = []
total_d=[]
payable=[]
def openfile(x):
    print("INSIDE openfile()")
    loc=(r'/home/aadarsh/Desktop/GEMSCAP1/'+x+'.xls') #loc=(r'.....\downloads\ + file name + .xls')
    print(loc)
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0) 
    global TKID 
    global total_d
    TKID=sheet.col_values(0,1,sheet.nrows-4)
    total_d=sheet.col_values(31, 1, sheet.nrows-4)

    for i in range (len(TKID)):
        TKID[i]=TKID[i].replace(" ","")
    TKID=list(dict.fromkeys(TKID))

    total_d = [i for i in total_d if i != '']

    print("LENGTH OF TKID: ",len(TKID))
    print(TKID)
    print("LENGTH OF total_d: ",len(total_d))
    print(total_d)

def createexceltable():
    print("INSIDE createexceltable()")
    con = sqlite3.connect("GEMSCAP_TABLE.db")   
    cur = con.cursor() 

    cur.execute('DROP TABLE EXCELTABLE ')
    cur.execute("""CREATE TABLE IF NOT EXISTS EXCELTABLE (TAKIONID INT PRIMARY KEY ,
                TOTAL_DELTA FLOAT DEFAULT 0 , PolicyNumber INT DEFAULT 0, NetPay FLOAT DEFAULT 0 , PAID FLOAT , TOTAL FLOAT  ,
                CarryForwardBalance FLOAT DEFAULT 0, StartingBalance FLOAT DEFAULT 0)""")
    
    for i in range(len(TKID)):
        
        cur.execute('''INSERT INTO EXCELTABLE (TAKIONID, TOTAL_DELTA) VALUES (?,?)''', (TKID[i], total_d[i]) )

    cur.execute('''UPDATE EXCELTABLE SET (PolicyNumber,CarryForwardBalance,StartingBalance) = (SELECT gemscap_table.PolicyNumber, gemscap_table.CarryForwardBalance,gemscap_table.StartingBalance
                FROM gemscap_table WHERE gemscap_table.TakionID = EXCELTABLE.TAKIONID)''')

    
    cur.execute('''SELECT TAKIONID, TOTAL_DELTA, PolicyNumber , CarryForwardBalance, NetPay, StartingBalance FROM EXCELTABLE ''')
    row = cur.fetchone()
    global payable
    while(row):
        print("row is :",row)
        if row[1] >= 0 and row[3] >= 0:   #if td and cfb is positive                                          
                                                                           
            if row[2] == 1:
                payable.append(row[1]*0.85)
            elif row[2] == 0:
                payable.append(row[1]*0.70)
            #else:payable.append(-1)
        elif row[1] < 0 and row[3] > 0:    # if td is -ve and cfb is +ve
            payable.append(row[1])
        elif ((row[1] > 0 and row[3] < 0) or (row[1] < 0 and row[3] < 0)):    # if td is +ve and cfb is -ve   or -ve -ve
            #check if |cfb| is 80% or more of stb raise alert
            if  abs(row[3]) >= 0.8*(row[5]):
                payable.append(row[1])
                #print("defaulter: ",row[0])
            else:
                payable.append(row[1])
        
        row = cur.fetchone()

    print(payable)
    print("LENGTH OF PAYABLE :",len(payable))
    con.commit()
    con.close()
#########################################################################################################
def updatenetpay():
    print("INSIDE CREATE updatenetpay()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    global TKID
    global payable
    print(TKID)
    for i in range(len(TKID)):
        x=TKID[i]
        print(x)
        #script='INSERT INTO EXCELTABLE (NetPay) VALUES (?) WHERE TAKIONID=7090100' , (payable[i])
        curs.execute('UPDATE EXCELTABLE SET NetPay = {}  WHERE TAKIONID= {}'.format(payable[i], TKID[i])  )
        #curs.execute('INSERT INTO EXCELTABLE (NetPay) VALUES (?) WHERE TAKIONID={}'.format(TKID[i]), (payable[i],) )
    conn.commit()
    conn.close()

def updateCarryForwardBalance():
    print("INSIDE CREATE updateCarryForwardBalance()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    global TKID
    for i in range(len(TKID)):
        curs.execute('UPDATE EXCELTABLE SET CarryForwardBalance = CarryForwardBalance + NetPay  WHERE TAKIONID= {}'.format(TKID[i])  )
    conn.commit()
    conn.close()

def updateCarryForwardBalanceInGemscap():
    print("INSIDE CREATE updateCarryForwardBalanceInGemscap()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    #curs.execute('UPDATE gemscap_table SET CarryForwardBalance = EXCELTABLE.CarryForwardBalance FROM EXCELTABLE WHERE TakionID= EXCELTABLE.TAKIONID')
    curs.execute('''UPDATE gemscap_table
SET
      CarryForwardBalance = (SELECT EXCELTABLE.CarryForwardBalance 
                            FROM EXCELTABLE
                            WHERE EXCELTABLE.TAKIONID = gemscap_table.TakionID )
WHERE
    EXISTS (
        SELECT *
        FROM EXCELTABLE
        WHERE EXCELTABLE.TAKIONID = gemscap_table.TakionID
    )
''')
    conn.commit()
    conn.close()

def cleardata():
    print("INSIDE CREATE cleardata()")
    global TKID
    TKID.clear()
    global total_d
    total_d.clear()
    global payable
    payable.clear()

##############################################PAID#################################

def printpayabledata(a):
    print("INSIDE printpayabledatabledata()")
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    curs.execute('''SELECT * FROM gemscap_table WHERE TakionID = {}'''.format(a))
    row = curs.fetchall()
    print(row)
    print('------------------')
    print(row[0][49])
    conn.commit()
    conn.close()
    return row[0][49]

def deductamount(a,y):
    print("INSIDE Deductamount")
    print('a=',a, 'y=',y)
    conn = sqlite3.connect("GEMSCAP_TABLE.db")   
    curs = conn.cursor()
    curs.execute('''UPDATE gemscap_table SET CarryForwardBalance = CarryForwardBalance - {} WHERE TakionID = {}'''.format(float(y),a))
    conn.commit()
    conn.close()