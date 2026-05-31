# Used to combine two or more funtion so that the output of one function can be used as an input of another function .

# Discount Management

def gst(price):
    return price + ((18/100)*price)

def discount(price):
    return price - 200

def final_amt(price):
    return discount(gst(price)) #  composition function
amount=int(input("Enter the amount:"))
print(final_amt(amount))