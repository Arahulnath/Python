name = "rahulNAth "
correct=name.lower()
print(correct)
print(name.upper())
print(name.capitalize())

name2= "iam the king of my world"
print(name2.title())
print(name2.capitalize())

phone = "9600945875"
masked=phone[:2]+"******"+phone[-2:]
print(masked)

uber="your uber id is : UB1234.please dont share with anyone "
ub_id=uber.split(":")[1].split(".")[0].strip()
print(ub_id)

print(uber.find("please") )

name2="rahul nath"
now="".join([word[0] .upper() for word in name2.split()])
print(now)

dis="use zomato25 to get disount 10%"
if "zomato25" in dis:
    print("You get discount")

word="Python is the Powerfull language in the World "
len=len(word.split())
print(len)