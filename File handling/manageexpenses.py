def add_expenses():
    with open("expenses.csv","a") as file:
        date=input("Enter the date : ")
        name=input("Enter the name : ")
        amount=int(input("Enter the amount :  "))
        file.write(f"{date},{name},{amount}\n")
        print("Expenses added Successfully")
def show_expenses():
    try:
        print("-------Your Expenses-------")
        with open("expenses.csv","r") as file:
            lines=file.readlines()
            for line in lines:
                date,name,amount=line.strip().split(",")
                print(f"{date},{name},{amount} ")

    except FileNotFoundError:
        print("No expenses file found")

    print("---------------------------")
def total_expenses():
    total=0
    print("---------------------------")
    try :
     with open("expenses.csv","r") as file:
         lines=file.readlines()
         for line in lines[1:]:
            _,_,amount=line.strip().split(",")
            total+=float(amount)
         print(f"Your total expenses {total}")

    except FileNotFoundError:
         print("No expenses file found")

    print("---------------------------")
while True:
    print("Welcome to the Expenses App")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    num=int(input("Enter your choice : "))
    if num==1:
        add_expenses()
    elif num==2:
        show_expenses()
    elif num==3:
        total_expenses()
    elif num==4:
        break

    else:
        print("Invalid Choice")