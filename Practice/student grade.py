def student_results():

    try :
     name=input("Enter student name: ")
     roll_no=input("Enter roll no: ")
     print("Enter  five subject marks")
     marks=[]
     for i in range(5):
        mark=int(input(f"{i+1}."))
        marks.append(mark)
     total=sum(marks)
     avg=total/5


     if avg>=90:
           grade="A"
     elif avg>=80:
           grade="B"
     elif avg>=70:
           grade="C"
     elif avg>=50:
           grade="D"
     else:
           grade="Fail"
     with open("expenses.csv", "a") as file:
         file.write(f"{roll_no},{name},{avg},{grade}\n")
     print("Student result saved succcessfully  ✅")

    except:
        print("Enter your input correctly ❌")



while True:
    print("1.Add Students Result")
    print("2.Exit")
    try:
     choice=int(input("Enter your choice: "))
     if choice==1:
        student_results()
     elif choice==2:
        break
     else:
        print("Your choice is not exits ❌")
    except:
        print("Enter your choice in number only👍")
