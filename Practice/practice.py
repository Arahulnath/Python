def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
print("Choice 1.Add")
print("Choice 2.Subtract")
print("Choice 3.Multiply")
choice=input("Enter choice:")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

if(choice=="1"):
    print(add(num1,num2))
elif(choice=="2"):
    print(subtract(num1,num2))
elif(choice=="3"):
    print(multiply(num1,num2))
else:
    print("Invalid Choice")