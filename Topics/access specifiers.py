#It is done in variables
class employee:
    def __init__(self):
        self.public="Im Public"
        self._protected="Im Protected"
        self.__private="Im Private"
    def books(self):
        print("Public :",self.public)
        print("Protected :",self._protected)
        print("Private :",self.__private)
class staff(employee):
    def students(self):
        print("Public :", self.public)
        print("Protected :", self._protected)
        try:
            print("Private:", self.__private)
        except  :
            print("Error")
class students:
    def classes(self,obj):
        print("Public :",obj.public)
        print("Protected :",obj._protected)
        try:
         print("Private :",obj.__private)
        except:
            print("Error")
x=employee()
y=staff()
z=students()

print("This is same class")
x.books()
print("This is chlid class")
y.students()
print("This is a stranger class")
z.classes(x)