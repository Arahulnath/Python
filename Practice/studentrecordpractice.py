'''
Features:
Add student
View students
Search by name
Update marks
'''
from sqlalchemy import true


def add_student():

    with open ("studentrecord.csv","a") as file:
        name=input("Enter Student Name: ")
        roll_no=input("Enter Student Roll No: ")
        marks=input("Enter Student Marks: ")
        file.write(f"{roll_no},{name},{marks}\n")
        print("Student Racord Addded Sucessfully✅")
def view_students():
    try :
     with open("studentrecord.csv","r") as file:
         for line in file:
             roll_no,name,marks=line.strip().split(",")
             print(f"{roll_no},{name},{marks}")
    except FileNotFoundError:
        print("Student Records File Not Found")
def search_students():
    roll_search=input("Enter Student Roll No: ")
    name_search = input("Enter Student Name: ")
    found=False
    try:

        with open("studentrecord.csv","r") as file:
            for line in file:
                roll_no,name,marks=line.strip().split(",")
                if roll_no==roll_search:
                 if name.lower()==name_search.lower() :
                    found=True
                    print(f"{roll_no},{name},{marks}")
                    break
        if not found:
            print("Student Not Found")
    except FileNotFoundError:
        print("Student Records File Not Found")
def update_marks():
    try:
        roll_search=input("Enter Student Roll No: ")
        marks_update=input("Enter Student Marks: ")
        found=False
        updated_data=""
        with open(f"studentrecord.csv","r") as file:
            for line in file:
                roll_no,name,marks=line.strip().split(",")
                if roll_no==roll_search:
                    found=True
                    marks=marks_update
                    print("Student Racord Updated Sucessfully✔️")
                updated_data+=f"{roll_no},{name},{marks}\n"

        with open ("studentrecord.csv","w") as file:
            file.write(updated_data)


        if not found:
            print("Student Not Found")
    except FileNotFoundError:
        print("Student Records File Not Found")

def main():
    while True:
        print ("-------------------Student Records System-------------------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Students")
        print("4. Update Marks")
        print("5. Exit")
        choice=int(input("Enter Choice: "))
        if choice==1:
            add_student()
        elif choice==2:
            view_students()
        elif choice==3:
            search_students()
        elif choice==4:
            update_marks()
        elif choice==5:
            break
        else:
            print("Invalid Choice")

main()

