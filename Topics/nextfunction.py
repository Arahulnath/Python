 # next() function
"""
values = ["Apple","Orange","Banana"]
ans=iter(values)
print(next(ans))
print(next(ans))"""

def numbers():
    print("Start")
    yield 1
    print ("Middle")
    yield 2
    print("End")
    yield 3

gen=numbers()
print(next(gen))
