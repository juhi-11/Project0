import mysql.connector

def getBTSDatabase():
    db = mysql.connector.connect(host='localhost', database='BTSDatabase', user='root', password='password')
    return db


def newaccount():
    db = getBTSDatabase()
    mycursor = db.cursor()
    id = input("enter customer id: ")
    password = input("enter customer password: ")
    age = int(input("enter customer age: "))
    name = input("enter customer name: ")
    phone = int(input("enter customer phone number: "))
    custMail = input("enter customer mail: ")

    sql = "insert into customer(custLoginId, custPassword, custAge, custName, custPhone, custEmail) values('%s', '%s', %d, '%s', %d, '%s')"
    values = (id, password, age, name, phone, custMail)

    complete_sql = sql % values
    print("sql=", complete_sql)

    mycursor.execute(complete_sql)
    if mycursor.rowcount == 1:
        print("record inserted successfully")
    else:
        print("record insertion failed")
    db.commit()

    db.close()

def updateaccount():
    db = getBTSDatabase()
    mycursor = db.cursor()

    sql = "update customer set '%s' = '%s' where custLoginId= '%s' "
    update = input("what do you wish to update (custPassword/custName/custAge/custPhone/custEmail): ")
    id =  input(f"enter login id of customer for {update} updation: ")
    new = input(f"enter new {update}: ")

    values = (update, new, id)
    mycursor.execute(sql % values)
    db.commit()

    if mycursor.rowcount == 1:
        print("updation successful", ro)
    else:
        print("record updation failed")

    db.close()

def newbug():
    db= getBTSDatabase()
    mycursor = db.cursor()

    sql = "insert into bug(bugPostingDate, custLoginID, bugId, bugStatus, productName, bugDesc) " \
          "values('%s', '%s', '%d', '%s', '%s', '%s')"
    custid= input("enter customer login id: ")
    date = input("enter bug posting date: ")
    id = int(input("enter bug id: "))
    status = input("enter bug status: ")
    name = input("enter product name: ")
    desc = input("enter bug description: ")

    values = (date, custid, id,  status, name, desc)

    complete_sql = sql % values
    print("sql=", complete_sql)

    mycursor.execute(complete_sql)
    if mycursor.rowcount == 1:
        print("record inserted successfully")
    else:
        print("record insertion failed")
    db.commit()

    db.close()

def viewbug():
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = " select * from bug "
    mycursor.execute(sql)

    for row in mycursor:
        print(
            "{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} {6:<10s} {7:<10s} {8:<10s} {9:<10s}  ".format(
                str(row[0]), str(row[1]),
                str(row[2]), str(row[3]),
                str(row[4]), str(row[5]),
                str(row[6]), str(row[7]), str(row[8]),
                str(row[9])))
        print("\n")
    db.commit()
    db.close()

def searchbug():
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = f" select * from bug where bugStatus= '%s'"
    bugstatus = input("Enter bug status(New Bug/Old Bug): ")
    values = (bugstatus)
    mycursor.execute(sql % bugstatus)

    for row in mycursor:
        print(
            "{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} {6:<10s} {7:<10s} {8:<10s} {9:<10s}  ".format(
                str(row[0]), str(row[1]),
                str(row[2]), str(row[3]),
                str(row[4]), str(row[5]),
                str(row[6]), str(row[7]), str(row[8]),
                str(row[9])))
        print("\n")
    db.commit()
    db.close()

def bugsolution():

    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = " select solution from bug where bugId=%d"
    bugid= int(input("enter bug id: "))
    mycursor.execute(sql%bugid)

    for row in mycursor:
        print("{0:<10s} ".format(str(row[0])))
        print("\n")
    db.commit()
    db.close()

def changepassword():
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = "update customer set custPassword= '%s' where custLoginId= '%s' "

    custID = input("enter customer ID for password updation: ")
    password = input("enter new password: ")

    values = (password, custID)
    mycursor.execute(sql % values)
    db.commit()

    if mycursor.rowcount == 1:
        print("updation successful")
    else:
        print("record updation failed")

def main():
    while(True):
        print("\t1. Create new account")
        print("\t2. Update existing account")
        print("\t3. Post new bug")
        print("\t4. View all bug")
        print("\t5. Search bugs by status")
        print("\t6. View bug solution")
        print("\t7. Change password")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            newaccount()
        elif choice == 2:
            updateaccount()
        elif choice == 3:
            newbug()
        elif choice == 4:
            viewbug()
        elif choice == 5:
            searchbug()
        elif choice == 6:
            bugsolution()
        elif choice == 7:
            changepassword()

main()
