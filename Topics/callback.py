# Callback function is a function that is passed as an argument of another function and it is called when needed .

def click_button(callback): # show function is passed as an argument
    print("Button clicked")
    callback() # and the function is called when needed

def show():
    print("Welcome to the page......!")

click_button(show) # show func is passsed as an argument of click_button func