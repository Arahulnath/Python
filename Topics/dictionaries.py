

trips={
   "1": {
    "trip_id":"01234",
    "location":"chennai",
    "day":"monday",
    "time":"10pm"
     },
    "2":{
    "trip_id":"01235",
    "location":"Andhra",
     "day": "tue",
     "time": "12pm"
     },
    "3":{
     "trip_id":"01236",
    "location":"Malaysia",
     "day": "wed",
     "time": "11pm"
    }
}

print(trips["1"]["trip_id"])
print(trips.get("1")) #safest method , if the key value is not in the dic , it return none instead of error
print(trips.keys())
print(trips.values())
for key,value in trips.items():
    print(key)
    print(value["trip_id"],"-->",value["location"],"--->",value["day"])
#update({Key,":",value} it is used to updte the key ,if the key already exixts it change it ,if the key is not there is just add it .
# pop is also used to remove the particular key and value .
# if the duplicate occurs it take the previuos occurs , not the first one.
# We can multiple value for one key
# We can iterately acces the dic , using looping.
# We can create multiple dic , using list.

#It create multiple dic using using list
''' 
students = []

for i in range(3):
    name = input("Enter name: ")
    mark = int(input("Enter mark: "))

    data = {
        "name": name,
        "mark": mark
    }

    students.append(data)

print(students) 
'''
'''Dic={}
while True:
    print ("Choose Choice : ")
    print ("1. Add Student")
    print ("2. Remove Student")
    print ("3. Exit")
    choice = input("Enter your choice: ")
    if choice=="1":

      name = input("Enter Student Name: ")
      print("Enter Mark : ")
      mark=int(input("Enter Mark: "))
      Dic[name] = mark
    elif choice =="2":

      name = input("Enter Student Name: ")
      if name in Dic:
       del Dic[name]
      else :
       print ("Student Name not exist")
    elif choice =="3":
       print("Finished successfully")
       break
    else:
     print("Invalid Choice .....")
print(Dic)

'''
n=int(input("Enter count of your Dic: "))
dic={}
for _ in range (n):
    key,value=input("Enter Your key and value:").split()
    dic[key]=[value]

print(dic)
