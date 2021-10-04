# Python-MySQL based Hotel Reservation System.
import mysql.connector as sql

# Creating some variables.
mydb = sql.connect(host="localhost", user="root", passwd="", db="python")
mycursor = mydb.cursor()

# MySQL Structure:
# DB : python
# Table Name: hotel
# cust_id
# cust_name
# address
# roomno
# mobileno
# check_in
# check_out
# adv_payment
# room_type


def add(cust_id, cust_name, address, roomno, mobileno, check_in, check_out, adv_payment, room_type):
    query = "INSERT INTO Hotel values({},'{}','{}',{},'{}','{}','{}',{},'{}')".format(
        cust_id, cust_name, address, roomno, mobileno, check_in, check_out, adv_payment, room_type)
    try:
        mycursor.execute(query)
        mydb.commit()
        return "Data inserted sucessfully."
    except:
        return "Error occured while inserting values in database."


def display(cust_id):
    query = f"SELECT * FROM Hotel WHERE cust_id={cust_id}"
    data = mycursor.execute(query)
    data = mycursor.fetchall()
    if data:
        for i in data:
            cust_name=i[1]
            address =i[2] 
            roomno = i[3]
            mobileno =i[4] 
            check_in = i[5]
            check_out =i[6]
            adv_payment = i[7]
            room_type=i[8]
        string = f"""Customer ID: {cust_id}
        Customer Name: {cust_name}
        Address: {address}
        Room Number: {roomno}
        Customer Mobile Number: {mobileno}
        Check In: {check_in}
        Check Out: {check_out}
        Advance Payment: {adv_payment}
        Room Type: {room_type}"""
        return string
    else:
        return "No user found"


def update(cust_id, cust_name, address, roomno, mobileno, check_in, check_out, adv_payment, room_type):
    query = f"UPDATE Hotel set cust_name='{cust_name}',address='{address}',roomno='{roomno}',mobileno={mobileno},check_in='{check_in}',check_out='{check_out}',adv_payment={adv_payment},room_type={room_type} WHERE cust_id={cust_id}"
    try:
        mycursor.execute(query)
        mydb.commit
        return "Data sucessfully updated."
    except:
        return "Error occured while updating values in database."


def delete(cust_id):
    query = f"DELETE FROM Hotel WHERE cust_id={cust_id}"
    try:
        mycursor.execute(query)
        mydb.commit()
        return "Data deleted sucessfully"
    except:
        return "Error ocurred while deleting data."


def generate(cust_id):
    query = f"SELECT * FROM Hotel WHERE cust_id={cust_id}"
    data = mycursor.execute(query)
    data = mycursor.fetchall()
    for i in data:
        cust_name=i[1]
        address =i[2] 
        roomno = i[3]
        mobileno =i[4] 
        check_in = i[5]
        check_out =i[6]
        adv_payment = i[7]
        room_type=i[8]
    
    time = int(input("For how many days did he/she stayed: "))
    if room_type=="suite":
        amount = 1500*time
    elif room_type=="delux":
        amount = 1000*time
    else:
        amount = 500*time
    
    price = amount-adv_payment
    string = f"""=====LaKhWaN's Hotel======
    ==========================
    Automated generated Innovoice.
    ==========================
    
    Customer ID: {cust_id}
    Customer Name: {cust_name}
    Customer Address: {address}
    Room No.: {roomno}
    Customer Mobile No.: {mobileno}
    Check In: {check_in}
    Check Out: {check_out}
    Advance Payment: {adv_payment}
    Room Type: {room_type}
    
    ==========================
    Total Price: {price}
    ==========================
    Thanks for visiting LaKhWaN's Hotel
    Hoping to see you soon.
    """
    return string


def main():
    print("===============================================")
    print("")
    print("Welcome to Hotel Reservation Program.")
    print("What would you like to do?\n")
    print("")
    print("===============================================")
    print("1. Insert data.")
    print("2. Update data.")
    print("3. Display data.")
    print("4. Delete data.")
    print("5. Generate Innovoice.")
    print("===============================================")
    print("Enter here: ", end="")

    todo = int(input())

    if todo == 1:
        cust_id = int(input("Enter customer id here: "))
        cust_name = input("Enter customer name here: ")
        address = input("Enter customer address here: ")
        roomno = int(input("Enter room number here: "))
        mobileno = int(input("Enter customer mobile number here: "))
        check_in = input("Enter check in date here (YYYY-MM-DD): ")
        check_out = input("Enter check out date here (YYYY-MM-DD): ")
        adv_payment = int(input("Enter advance payment here: "))
        while True:
            print("Enter room type here: ")
            room_type = int(
                input("1. Suite(1500/day)\n2. Delux (1000/day)\n3. Standard (500/day)\nEnter: "))
            if room_type == 1:
                room_type = "suite"
                break
            elif room_type == 2:
                room_type = "delux"
                break
            elif room_type == 3:
                room_type = "standard"
                break
            else:
                print("Invalid.")

        print(add(cust_id, cust_name, address, roomno, mobileno,
                  check_in, check_out, adv_payment, room_type))

    elif todo == 2:
        cust_id = int(input("Enter the customer id here: "))
        print("Current data:")
        print(display(cust_id))
        cust_name = input("Enter updated customer name here: ")
        address = input("Enter updated customer address here: ")
        roomno = int(input("Enter updated room number here: "))
        mobileno = int(input("Enter updated customer mobile number here: "))
        check_in = input("Enter updated check in date here (YYYY-MM-DD): ")
        check_out = input("Enter updated check out date here (YYYY-MM-DD): ")
        adv_payment = int(input("Enter updated advance payment here: "))
        while True:
            print("Enter updated room type here: ")
            room_type = int(
                input("1. Suite(1500/day)\n2. Delux (1000/day)\n3. Standard (500/day)\nEnter: "))
            if room_type == 1:
                room_type = "suite"
                break
            elif room_type == 2:
                room_type = "delux"
                break
            elif room_type == 3:
                room_type = "standard"
                break
            else:
                print("Invalid.")

        print(update(cust_id, cust_name, address, roomno, mobileno,check_in, check_out, adv_payment, room_type))
    elif todo==3:
        cust_id = int(input("Enter the customer id here: "))
        print(display(cust_id))
    elif todo==4:
        cust_id = int(input("Enter the customer id here: "))
        print(delete(cust_id))
    elif todo==5:
        cust_id = int(input("Enter the customer id here: "))
        print(generate(cust_id))

if __name__ == "__main__":
    main()