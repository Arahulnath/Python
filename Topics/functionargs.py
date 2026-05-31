#this func is for adding multple numbers
def add(*args):
    total = 0
    for num in args:
        total=total+num
    return total
print(add(1,2, 4,5))