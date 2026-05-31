#Lambda Function
#Single line function , ananoymous function , does not have nay fun name , used only once
result=lambda a,b:a+b
print(result(3,4))

#Map function
#Used to map every single element is the list to the funtion
fruits=["Apple","Orange","Banana"]
upper=list(map(lambda fruit:fruit.upper(),fruits))
print(upper)

#Filter Function
#Filter items according to the conditon
list1=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda x:x%2==0,list1))
print(even)

#Reduce function
#Combines all element and produce single output
from functools import reduce
list1=[1,2,3,4,5,6,7,8,9]
maxi=reduce(lambda x,y:x if x>y else y,list1)
print(maxi)

