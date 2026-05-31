import random
random=random.randint(1,10)
while True:
    num=int(input("Enter a number:"))
    if num==random:
        print("Correct guessing")
        break
    else:
        print("Choose correct number")