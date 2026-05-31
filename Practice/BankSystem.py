#Banking System
users={}
def create_acc():
    name=input("Enter your name :")
    acc=input("Enter your acc number :")
    if acc in users:
        print("Already exits")
        return
    users[acc]={"name":name,"Balance":0,"History":[]}
    print("Account created sucessfully")
def login():
    acc=input("Enter your account number :")
    if acc in users:
        user_menu(acc)
    else:
        print("Account not exists")
def user_menu(acc):
    print("Welcome",acc)
    while True:
          print("Choose num : \n 1.Deposit \n 2.Withdrawal \n 3.Balance \n 4.History \n 5.log out" )
          ch=int(input("Enter your choice :"))
          if ch==1:
             amt=int (input("Enter your amount :"))
             users[acc]["Balance"]+=amt
             users[acc]["History"].append(f"Deposited : {amt}")
             print("Deposited Sucessfully")
          elif ch==2:
              amt=int (input("Enter  amount to withdraw :"))
              if amt<=users[acc]["Balance"]:
                users[acc]["Balance"]-=amt
                users[acc]["History"].append(f"Withdraded : {amt}")
                print("Withdraded Sucessfully")
              else:
                  print("Insufficient Balance")
          elif ch==3:
               print("Balance : ",users[acc]["Balance"])
          elif ch==4:
              print("-----History-----")
              if not users[acc]["History"]:
                  print("No transaction yet done ")
              else :
                 for h in users[acc]["History"]:
                     print(h)
          elif ch==5:
              print("Logout sucessfully")
              break
          else:
              print("Wrong choice")
while True:
    print("Welcome  to  our banking system  ")
    print("1.Create Account")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice :"))
    if ch==1:
        create_acc()
    elif ch ==2:
        login()
    elif ch==3:
         print("Thank you ")
         break

    else:
        print("Invalid choice")


