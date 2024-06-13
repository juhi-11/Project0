import mysql.connector

def getBTSDatabase():
    db = mysql.connector.connect(host='localhost', database='BTSDatabase', user='root', password='password')
    return db

def customerservices():
    while (True):
        print("\t1. View all customers")
        print("\t2. Search: by customer name")
        print("\t3. Search by customer id")
        print("\t4. Exit") 
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = " select * from customer "
            mycursor.execute(sql)

            for row in mycursor:
                print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} ".format(str(row[0]), str(row[1]),
                                                                                      str(row[2]), str(row[3]),
                                                                                      str(row[4]), str(row[5])))
                print("\n")
            db.commit()
            db.close()


        elif choice == 2:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = f" select * from customer where custName= '%s'"
            name = input("Enter customer name: ")
            values = (name)
            mycursor.execute(sql%name)

            for row in mycursor:
                print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} ".format(str(row[0]), str(row[1]),
                                                                                      str(row[2]), str(row[3]),
                                                                                      str(row[4]), str(row[5])))
                print("\n")

            db.commit()
            db.close()


        elif choice == 3:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = " select * from customer where custLoginID= '%s'"
            customerID = input("Enter customer ID: ")
            values = (customerID)
            mycursor.execute(sql % values)

            for row in mycursor:
                print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} ".format(str(row[0]), str(row[1]),
                                                                                      str(row[2]), str(row[3]),
                                                                                      str(row[4]), str(row[5])))
                print("\n")

            db.commit()
            db.close()

        elif choice == 4:
            break

def employeeservices():
    while (True):
        print("\t1. Add new Employee")
        print("\t2. View all Employees")
        print("\t3. Search by Employee name")
        print("\t4. Search by Employee ID")
        print("\t5. Search by Employee Type")
        print("\t6. Change Employee Status")
        print("\t7. Change Password")
        print("\t8. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            db = getBTSDatabase()
            mycursor = db.cursor()

            sql = "insert into employee(empLoginId, empPassword, empType, empName, empPhone, empEmail, EmpStatus) " \
                  "values('%s', '%s', '%s', '%s', %d, '%s', '%s')"
            id = input("enter employee id: ")
            password = input("enter employee password: ")
            type = input("enter employee type(admin/expert): ")
            name = input("enter employee name: ")
            phone = int(input("enter employee phone number: "))
            empMail = input("enter employee mail: ")
            status = input("enter employee status(active/deactivated): ")
            values = (id, password, type, name, phone, empMail, status)

            complete_sql = sql % values
            print("sql=", complete_sql)

            mycursor.execute(complete_sql)
            if mycursor.rowcount == 1:
                print("record inserted successfully")
            else:
                print("record insertion failed")
            db.commit()

            db.close()

        elif choice == 2:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = " select * from employee "
            mycursor.execute(sql)

            for row in mycursor:
                print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} {6:<10s} ".format(str(row[0]), str(row[1]),
                                                                                               str(row[2]), str(row[3]),
                                                                                               str(row[4]), str(row[5]),
                                                                                               str(row[6])))
                print("\n")

            db.commit()
            db.close()

        elif choice == 3:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = f" select * from employee where empName= '%s'"
            name = input("Enter employee name: ")
            values = (name)
            mycursor.execute(sql % name)

            for row in mycursor:
                print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} {6:<10s} ".format(str(row[0]), str(row[1]),
                                                                                               str(row[2]), str(row[3]),
                                                                                               str(row[4]), str(row[5]),
                                                                                               str(row[6])))
                print("\n")

            db.commit()
            db.close()

        elif choice == 4:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = f" select * from employee where empLoginId= '%s'"
            empid = input("Enter employee Id: ")
            values = (empid)
            mycursor.execute(sql % empid)

            for row in mycursor:
                print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} {6:<10s} ".format(str(row[0]), str(row[1]),
                                                                                               str(row[2]), str(row[3]),
                                                                                               str(row[4]), str(row[5]),
                                                                                               str(row[6])))
                print("\n")

            db.commit()
            db.close()

        elif choice == 5:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = f" select * from employee where empType= '%s'"
            type = input("Enter employee type(ADMIN/EXPERT): ")
            values = (type)
            mycursor.execute(sql % values)

            for row in mycursor:
                print("{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} {6:<10s} ".format(str(row[0]), str(row[1]),
                                                                                               str(row[2]), str(row[3]),
                                                                                               str(row[4]), str(row[5]),
                                                                                               str(row[6])))
                print("\n")

            db.commit()
            db.close()

        elif choice == 6:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = "update employee set empStatus= '%s' where empLoginID= '%s' "

            empID = input("enter employee id for status updation: ")
            status = input("enter new status(ACTIVE/DEACTIVATED): ")

            values = (status, empID)
            mycursor.execute(sql % values)
            db.commit()

            if mycursor.rowcount == 1:
                print("updation successful")
            else:
                print("record updation failed")

            db.close()

        elif choice == 7:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = "update employee set empPassword= '%s' where empLoginID= '%s' "

            empID = input("enter employee ID for password updation: ")
            password = input("enter new password: ")

            values = (password, empID)
            mycursor.execute(sql % values)
            db.commit()

            if mycursor.rowcount == 1:
                print("updation successful")
            else:
                print("record updation failed")

        elif choice == 8:
            break


def bugservices():
    while (True):
        print("\t1. View all bugs")
        print("\t2. Search by bug ID")
        print("\t3. Search bug by Status")
        print("\t4. Search by customer login id")
        print("\t5. Assign bug to expert")
        print("\t6. Logout")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
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

        elif choice == 2:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = f" select * from bug where bugId= '%s'"
            bugid = input("Enter bug Id: ")
            values = (bugid)
            mycursor.execute(sql % bugid)

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

        elif choice == 3:
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

        elif choice == 4:
            db = getBTSDatabase()
            mycursor = db.cursor()
            sql = f" select * from bug where custLoginId= '%s'"
            custLoginId = input("Enter customer login id: ")
            values = (custLoginId)
            mycursor.execute(sql % custLoginId)

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

        elif choice == 5:
            db = getBTSDatabase()
            mycursor = db.cursor()
            bugid = int(input("enter bug id: "))
            expdate = input("enter expert assigned date: ")
            expid = input("enter expert login id: ")

            sql = "update bug set expertLoginId= '%s', expertAssignedDate= '%s' where bugId=%d"
            values = (expid, expdate, bugid)

            complete_sql = sql % values
            print("sql=", complete_sql)

            mycursor.execute(complete_sql)
            if mycursor.rowcount == 1:
                print("record inserted successfully")
            else:
                print("record insertion failed")
            db.commit()

            db.close()

        elif choice == 6:
            break


def main():
    while(True):
        print("\t1. Customer Services")
        print("\t2. Employee Services")
        print("\t3. Bug Services")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            customerservices()
        elif choice == 2:
            employeeservices()
        elif choice == 3:
            bugservices()

main()




