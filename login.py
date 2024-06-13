import mysql.connector

def getBTSDatabase():
    db = mysql.connector.connect(host='localhost', database='BTSDatabase', user='root', password='password')
    return db

def employeeLogin():
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = " select * from employee where empName= '%s' and empPassword= '%s' "
    name = input("Enter Employee Name: ")
    password = input("Enter your password: ")
    values = (name, password)
    complete_sql = sql % values
    mycursor.execute(complete_sql)

    for row in mycursor:
        print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} {6:<10s} ".format(str(row[0]), str(row[1]),
                                                                                       str(row[2]), str(row[3]),
                                                                                       str(row[4]), str(row[5]),
                                                                                       str(row[6])))
        print("\n")

    db.commit()
    db.close()

def customerLogin():
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = " select * from customer where custName= '%s' and custPassword= '%s' "
    name = input("Enter Customer Name: ")
    password = input("Enter your password: ")
    values = (name, password)

    mycursor.execute(sql % values)

    for row in mycursor:
        print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} ".format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]) ) )
        print("\n")
    db.commit()
    db.close()

def customersignup():
    db = getBTSDatabase()
    mycursor = db.cursor()

    sql = "insert into customer(custLoginId, custPassword, custName, custAge, custPhone, custEmail)" "values('%s', '%s', '%s', %d, %d, '%s')"
    loginid = input("enter customer login id: ")
    password = input("enter customer password: ")
    name = input("enter customer name: ")
    age = int(input("enter customer age: "))
    phone = int(input("enter customer phone number: "))
    custmail = input("enter customer mail: ")
    values = (loginid, password, name, age, phone, custmail)

    complete_sql = sql % values
    print("sql=", complete_sql)

    mycursor.execute(complete_sql)
    if mycursor.rowcount == 1:
        print("record inserted successfully")
    else:
        print("record insertion failed")
    db.commit()

    db.close()


def mainMenu():
    print("\n\n Bug Tracking System ")
    while(True):
        print("\t1. Employee Login")
        print("\t2. Customer Login")
        print("\t3. Customer Signup")
        print("\t4. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            employeeLogin()
        elif choice == 2:
            customerLogin()
        elif choice == 3:
            print("Create new customer registration")
            customersignup()
        elif choice == 4:
            break

mainMenu()

