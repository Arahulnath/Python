"""file = open("note.txt","r")
file.write("This is a fle handling \n")
file.write("This is a new file ")
file.close()"""


"""file = open("note.txt","r")
content=file.read()
print("Conetnt : \n",content )
file.close()"""

"""file = open("note.txt","a")
file.write("\nThis is a appned\n")
file=open("note.txt","r")
content=file.read()
print("Conetnt : \n",content )

file.close()"""

"""with open("note.txt") as file: #this is used in real world for not typing file.close evertime 
    for line in file:
        print(line.strip())"""
"""user_input=input("Enter you feedback : ")
with open("Feedback.txt","a") as login:
    login.write(user_input+"\n")
print("Thank you for your feedback")"""
"""with open("note.txt") as file:
    for line in range(1):
     print(file.readline())"""

"""import csv
with open ("sample.csv","r") as file:
    reader= csv.DictReader(file) # make the file dictionary (it takes first row as default heading name )
    for line in reader:
        print(line["Age"])"""

with open("sample.csv","r") as file:
    lines=file.readlines()
    for line in lines[1:]:
        content=line.strip().split(",")
        print(content[2])