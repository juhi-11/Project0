import mysql.connector

def getBTSDatabase():
    db = mysql.connector.connect(host='localhost', database='BTSDatabase', user='root', password='password')
    return db

def viewbug():
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = " select * from bug where expertLoginId='%s' "
    expId = input("enter expert login id to view assigned bugs: ")
    mycursor.execute(sql%expId)

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

def filterbug():
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = " select * from bug where bugStatus='%s' "
    status = input("enter bug status to be searched(New Bug/Old Bug): ")
    mycursor.execute(sql % status)

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

def solvebug():
    db = getBTSDatabase()
    mycursor = db.cursor()
    bugid = int(input("enter bug id: "))

    sql = "select * from bug where bugId= '%s'"
    mycursor.execute(sql % bugid)

    for row in mycursor:
        print(
            "{0:<10s} {1:<10s} {2:<10s} {3:<10s} {4:<10s} {5:<10s} {6:<10s} {7:<10s} {8:<10s} {9:<10s}  ".format(
                str(row[0]), str(row[1]),
                str(row[2]), str(row[3]),
                str(row[4]), str(row[5]),
                str(row[6]), str(row[7]), str(row[8]),
                str(row[9])))


    sql = "update bug set solution= '%s', bugSolvedDate='%s' where bugId=%d"
    solution = input("enter solution for bug")
    date= input("enter bug solved date: ")
    bugId = int(input("enter bug id: "))
    value = (solution, date, bugId)

    complete_sql = sql % value
    print("sql=", complete_sql)

    mycursor.execute(sql % value)
    if mycursor.rowcount == 1:
        print("record inserted successfully")
    else:
        print("record insertion failed")
    db.commit()
    db.commit()

    db.close()

def changepassowrd():
    db = getBTSDatabase()
    mycursor = db.cursor()
    sql = "update employee set EmpPassword= '%s' where empLoginID= '%s' "

    empID = input("enter employee ID for password updation: ")
    password = input("enter new password: ")

    values = (password, empID)
    mycursor.execute(sql % values)
    db.commit()

    if mycursor.rowcount == 1:
        print("updation successful")
    else:
        print("record updation failed")

def main():
    while(True):
        print("\t1. View assigned bug")
        print("\t2. Filter assigned bug based on status")
        print("\t3. Solve the bug")
        print("\t4. Change password")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            viewbug()
        elif choice == 2:
            filterbug()
        elif choice == 3:
            solvebug()
        elif choice == 4:
            changepassowrd()

main()


