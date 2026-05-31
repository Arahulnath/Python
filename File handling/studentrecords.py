import time
def create_students():
    with open("studentsrecords.txt","a") as file:
        roll_no = input("Enter roll no: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        file.write(f"{roll_no},{name},{marks}\n")
        print("Students creates successfully")
def view_students():
    try:
       with open("studentsrecords.txt","r") as file:
           print("-----Students File Records-----")
           for line in file:
            roll_no,name,marks=line.strip().split(",")
            print(f"{roll_no},{name},{marks}")
    except FileNotFoundError:
        print("Students file is not found...!")
def search_students():
    roll_search = input("Enter roll no: ")
    found =False
    try:
      with open("studentsrecords.txt","r") as file:
        for line in file:
            roll_no,name,marks=line.strip().split(",")
            if roll_no==roll_search:
                found=True
                print(f"{name},{marks}")
                break

      if not found:
          print("Students file not found...!")
    except FileNotFoundError:
        print("Students file is not found...!")
while True:
    print("1. Add students")
    print("2. Veiw Students")
    print("3. Search Students")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_students()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_students()
    elif choice == 4:
        time.sleep(0.5)
        print("Existing")
        break
    else:
        print("Invalid Choice")