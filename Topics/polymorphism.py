'''lass dad:
    def house(self):
        print("Blue")
class son(dad):
    def factory(self):
        print("Red")
    def house(self):     #function/methods  overriding using inheritance
        print("Green")
s1=son()
s1.house()
s1.factory()'''
#same method name but different class name IS called polymorphism
class students:
    def books(self):
        print("Yellow")
class staff:
    def books(self):
        print("Red")
s1=students()
s1.books()
s2=staff()
s2.books()