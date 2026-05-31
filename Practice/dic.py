students = {}

while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":

        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        students[name] = marks

        print("Student added successfully!")

    # View Students
    elif choice == "2":

        if len(students) == 0:
            print("No students found")

        else:
            print("\nStudent Records")

            for name, marks in students.items():
                print(name, ":", marks)

    # Update Marks
    elif choice == "3":

        name = input("Enter student name: ")

        if name in students:

            new_marks = int(input("Enter new marks: "))
            students[name] = new_marks

            print("Marks updated!")

        else:
            print("Student not found")

    # Delete Student
    elif choice == "4":

        name = input("Enter student name: ")

        if name in students:

            del students[name]

            print("Student deleted!")

        else:
            print("Student not found")

    # Exit
    elif choice == "5":

        print("Program exited")
        break

    else:
        print("Invalid choice")
print (students)

