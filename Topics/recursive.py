# Function that call itself until the condition is met

# the stoping condition is called base case


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1) # 5 * factorial(4) => 5*4 ,  5 * 4 * factorial(3) => 5 * 4 * 3 , .....

print(factorial(5))
