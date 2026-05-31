'''from function import add
result=add(1,2)
print(result)''' # for two num

from functionargs import add
numbers=list(map(int,input("enter number").split()))
result=add(*numbers)
print(result)
