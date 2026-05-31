#Partial function is used for fixed argument for the function, to skip the multiple argument passes to the function .


from functools import partial
def login(name,domain):
    return f"{name}@{domain}"
while True:
    print("1.Gmail")
    print("2.Ymail")
    print("3.Yahoo")
    print("4.Exit")
    choice = input("Choose your domain : ")
    name=input("Enter name of your domain : ").lower()
    if choice=="1":
      gmail=partial(login,domain="gmail.com") # partial funtion
      print(gmail(name))
      break
    elif choice=="2":
       ymail=partial(login,domain="ymail.com") # partial funtion
       print(ymail(name))
       break
    elif choice=="3":
       yahoo=partial(login,domain="yahoo.com") # partial funtion
       print(yahoo(name))
       break
    elif choice=="4":
        print ("Thank You")
        break
    else:
        print("Invalid Choice❌")

