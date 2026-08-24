# It is a special function it uses yeild keyword .
# it is used to return the value one by one , instead os returning everthing at once .
"""def numbers(n):
    numbers=[]
    for i in range(n):
       numbers.append(i)
    return numbers

print(numbers(5))"""

def numbeers(n):
    for i in range(n):
        yield i # pause and produce value one by one

for i in numbeers(10):
   print(i)
# for yield keyword we must iterate the value using for loop