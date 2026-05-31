from add import add
y=list(map(int,input("Enter a numbers to print").split()))
x=add(*y)
print(x)