# Remember variable from outer function
# Used in nested function
def outer(msg):
    def inner():
        print(msg)
    return inner
result=outer("Hello")
result()