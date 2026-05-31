'''
1
2 3
4 5 6
7 8 9 10
'''
num = int(input("Enter a number: "))

num1=1
for i in range(1,num+1):
    for j in range(i):
      print(num1,end=" ")
      num1=num1+1
    print()
