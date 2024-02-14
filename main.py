import mysql.connector
from tabulate import  tabulate


con = mysql.connector.connect(host="localhost", user="root", password="", database="register")

res = con.cursor()
def insert():
    name = input("Enter Name:")
    age = input("Enter Your Age:")
    address = input("Enter Your Address:")
    mobile_number = input("Enter Your Number:")
    email = input("Enter Your E-mail:")
    sql = "insert into user_table (name, age, address, mobile_number, email) values (%s,%s,%s,%s,%s)"
    res.execute(sql, (name, age, address, mobile_number, email))
    con.commit()
    print("\n")
    print("Record Inserted Successfully!")


def view():
    sql = "SELECT * from user_table"
    res.execute(sql)
    result = res.fetchall()
    print("\n")
    print(tabulate(result, headers=["ID", "NAME", "AGE", "ADDRESS", "MOBILE.NO", "E-MAIL"]))

def update():
    print("1.Name\n"
          "2.Age\n"
          "3.Address\n"
          "4.Mobile number\n"
          "5.E-mail")
    option = int(input("Enter Your Option:"))
    if option == 1:
        pid = input("Enter Your ID:")
        updated_name = input("Enter Your Name:")
        sql = "UPDATE user_table set name=%s where pid=%s"
        res.execute(sql, (updated_name, pid))
        con.commit()
        view()
        print("\n")
        print("Updated Successfully!")
    elif option == 2:
        pid = input("Enter Your ID:")
        updated_age = input("Enter Your Age:")
        sql = "UPDATE user_table set age=%s where pid=%s"
        res.execute(sql, (updated_age, pid))
        con.commit()
        view()
        print("\n")
        print("Updated Successfully!")
    elif option == 3:
        pid = input("Enter Your ID:")
        updated_address = input("Enter Your Address:")
        sql = "UPDATE user_table set address=%s where pid=%s"
        res.execute(sql, (updated_address, pid))
        con.commit()
        view()
        print("\n")
        print("Updated Successfully!")
    elif option == 4:
        pid = input("Enter Your ID:")
        updated_number = input("Enter Your Mobile Number:")
        sql = "UPDATE user_table set mobile_number=%s where pid=%s"
        res.execute(sql, (updated_number, pid))
        con.commit()
        view()
        print("\n")
        print("Updated Successfully!")
    elif option == 5:
        pid = input("Enter Your ID:")
        updated_mail = input("Enter Your E-mail:")
        sql = "UPDATE user_table set email=%s where pid=%s"
        res.execute(sql, (updated_mail, pid))
        con.commit()
        view()
        print("\n")
        print("Updated Successfully!")
    else:
        print("Invalid")


def delete():
    pid = input("Enter Your ID:")
    sql = "delete from user_table where pid=%s"
    res.execute(sql, (pid,))
    con.commit()
    view()
    print("\n")
    print("Record Deleted Successfully!")


while True:
    print("\n")
    print("1.Insert Record")
    print("2.View Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Quit")
    print("\n")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        insert()
    elif choice == 2:
        view()
    elif choice == 3:
        update()
    elif choice == 4:
        delete()
    elif choice == 5:
        quit()
    else:
        print("Invalid Option!")



