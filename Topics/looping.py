
"""for i in range (10):
    print (i+1)"""

'''data=["mobile","ipad","tablet","mouse"]
for items in data:
    print(items.upper())'''

'''correct_pass='1234'
entered_pin=''
while entered_pin!= correct_pass :
    pin=input("Enter correct pin : ")
    entered_pin=pin

print("Login sucessful")'''

'''num = [ 1,3,5,6,7,8,9,0]
for i in num:
    if i==9:
      break
    print(i)
'''

'''data=[3 , 4 , 5, -1, 2, 4, -8]
for i in data:
    if i <= 0:
        continue
    print(i)'''
items =[]
while True :# infinite loop
    items_ = input("Add items to cart . ( type done when you completed adding items) : ")
    if items_.lower()=='done':
        break
    items.append(items_)

print(items)



