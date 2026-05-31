delivery_app='amazon' #global scope
def quantity():
    items=2 #enclosing scope , nested function
    def order():
           name='iphone' #local scope
           print(f"I have ordered {items} {name} using {delivery_app}")
    order()
quantity()


