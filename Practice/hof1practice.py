def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
def result(func,x,y):
    return func(x,y)
while True:
    print("1.Add")
    print("2.Multiply")
    choice=int(input("Enter your choice"))
    x=int(input("Enter your first number"))
    y=int(input("Enter your second number"))
    if choice==1:
        print(result(add,x,y))
    elif choice==2:
        print(multiply(x,y))
    else:
        print("Invalid Choice")
