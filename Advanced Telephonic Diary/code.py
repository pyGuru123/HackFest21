# coded by Tejas Srivastava

import datetime
from os import system

class data:
    def __init__(self, contact, name, address, note):
        self.contact = contact
        self.name = name
        self.address = address
        self.note = note
        
    def getDetails(self):
        return f"{timeStamp()}\nName: {self.name}\nContact: {self.contact}\nAddress: {self.address}\nNote: {self.note}\n\n"

def makeBorderSupreme(text):
    print("\n\n+ +-" + "-"*len(text) + "-+ +")
    print("+ +-" + "-"*len(text) + "-+ +")
    print(f"| | {text} | |")
    print("+ +-" + "-"*len(text) + "-+ +")
    print("+ +-" + "-"*len(text) + "-+ +\n")
def makeBorder(text):
    print("\n\n+-" + "-"*len(text) + "-+")
    print(f"| {text} |")
    print("+-" + "-"*len(text) + "-+\n")

def timeStamp():
    """Adds time stamp to every query"""
    dd = datetime.datetime.today().day
    mm = datetime.datetime.today().month
    yy = datetime.datetime.today().year
    
    t = datetime.datetime.now().strftime("[%H:%M:%S]")
    return f"{t}  {dd:02d}.{mm:02d}.{yy:02d}"

def getRecordNo():
    """reads all previous Record No and give +1 from last"""
    newNo = 0
    with open("Diary.txt") as f:
        for i in f:
            if "Record No.:" in i:
                newNo += 1
    return newNo+1 

def searchByName(name):
    # surf through lines and find line no of "name" then gives rest of line by another loop.
    
    lineNo = 0
    with open("Diary.txt") as f:
        # enumerates iterates through line number 
        for l, d in enumerate(f, 1):
            if name.lower() in d.lower():
                lineNo += l
                break
    
    if lineNo:
        makeBorder("DATA FETCHED: ")
        with open("Diary.txt") as f:
            for line, data in enumerate(f, 1):
                # name starts from 0 out of 6 
                for i in range(-2, 4):
                    if line == lineNo + i:
                        print(f"{data}", end = "")
                        
         # del lines = -2,-1,0,1,2,3,4
        delete([lineNo - 2,lineNo - 1,lineNo,lineNo + 1,lineNo + 2, lineNo + 3, lineNo + 4])
    else: makeBorder("Sorry No data available for this search.")
    print("\n")
                                    
def searchByContact(contact):
    lineNo = 0
    with open("Diary.txt") as f:
        for l, d in enumerate(f, 1):
            if contact in d:
                lineNo += l
    
    if lineNo:
        makeBorder("DATA FETCHED: ")
        with open("Diary.txt") as f:
            for search, data in enumerate(f, 1):
                # if search is lying between range -3 3
                for i in range(-3, 3):
                    if search == lineNo + i:
                        print(f"{data}", end ="")
                        
         # del lines = -3,-2,-1,0,1,2,3
        delete([lineNo - 3,lineNo - 2,lineNo - 1,lineNo,lineNo + 1,lineNo + 2, lineNo + 3])
    
    else : makeBorder("Sorry No data available for this search.")
    print("\n")
                                      
def searchByRecordNo(recordNo):
    find = f"Record No.: {recordNo}"
    lineNo = 0
    cross = False
    with open("Diary.txt") as f:
        for l, d in enumerate(f, 1):
            if find in d:
                lineNo += l
                cross = True

    if cross:
        makeBorder("DATA FETCHED: ")
        with open("Diary.txt") as f:
            for searchline, data in enumerate(f, 1):
                for i in range(0, 6):
                    if searchline == lineNo + i:
                        print(f"{data}", end = "")
        # del lines = 0,1,2,3,4,5
        delete([lineNo + 0,lineNo + 1,lineNo + 2,lineNo + 3,lineNo + 4,lineNo + 5, lineNo + 6])
        
    else:  makeBorder("Sorry No data available for this search.")
    print("\n")
            
def delete(skip):
    choice = int(input("\n1. Delete this record\n2. Go back to menu\nSelect any option: "))
    if choice != 1: return;
    
    # store every line in "all"
    with open("Diary.txt") as f:
        all = f.readlines()
    # clears the whole file and then put data from "all" except deletion data
        with open("Diary.txt", 'w') as f2:
            No = 1
            for line, data in enumerate(all, 1):
                if line not in skip:
                    if "Record No.:" in data:
                        f2.write(f"Record No.: {No}\n")
                        No += 1
                    else: f2.write(data)
    makeBorder("Data has been deleted Successfully.")


# driver code
system('cls')
makeBorderSupreme("PhoneBook Diary".upper())
while True:
    option = int(input("1. Add\n2. Open\n3. Exit\nSelect any option: "))

    if option == 1:
        no_of_records = int(input("Enter the number of records to be added = "))
        # system('cls')
        for i in range(0, no_of_records):
            if no_of_records > 1:
                print(f"\nEnter details of Record {i+1}")
            
            contact = input("Enter the Contact number = ")
            while len(contact) != 10:
                print("ERROR: PLEASE ENTER A VALID NUMBER")
                contact = input("Enter the Contact number = ")
                
            name = input("Enter Name = ")
            address = input("Enter address = ")
            note = input("Enter note if any = ")
            record = data(contact, name, address, note)
            
            with open("Diary.txt",'a') as f:
                f.write(f"Record No.: {getRecordNo()}\n")
                f.write(record.getDetails())
                makeBorder("Data Successfully added".upper())
                
    if option == 2:
        choice = int(input("\n1. Show All records\n2. Search\n3. Exit\nSelect any option: "))
        system('cls')
        if choice == 1:
            makeBorder("Available Records: ".upper())
            with open("Diary.txt", 'r') as f:
                f.seek(0)
                print(f.read())
        elif choice == 2:
            searchby = int(input("\nSearch by:\n1. Name\n2. Contact\n3. Record Number\nSelect any option: "))
            if searchby == 1:
                name = input("\nEnter Name of the record you want to search = ")
                searchByName(name)
            elif searchby == 2:
                contact = input("\nEnter Contact of the record you want to search = ")
                # checks if contact is valid
                while len(contact) != 10:
                    print("ERROR: PLEASE ENTER A VALID NUMBER")
                    contact = input("Enter Contact of the record you want to search = ")
                
                searchByContact(contact)
            elif searchby == 3:
                recordNo = int(input("\nEnter the record No. = "))
                searchByRecordNo(recordNo)

            else: print("Choose a valid option\n")
        elif choice == 3:
            print("Exiting...")
            exit()
                
    if option == 3:
        makeBorder("Exited".upper())
        exit()
        