def add(*num):
    total = 0
    for i in num:
        total+=i
    return total
y=list(map(int,input("Enter a numbers to print").split()))
x=add(*y)
print(x)