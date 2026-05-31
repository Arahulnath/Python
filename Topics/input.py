
import sys


'''fullname=" ".join(sys.argv[1:])
print (fullname)
email = fullname.lower().replace(" ",".") +"@gmail.com"
print(email)'''


fullname = sys.argv[1]
lastname=sys.argv[2]
email=fullname.lower()+lastname.lower()+"@gmail.com"
print(email)

'''x=int(input("Enter a number : "))
y=int(input("Enter another number : "))
print(x+y)'''


