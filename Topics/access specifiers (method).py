class government:
    def one(self):
        print("This is public")
    def _two(self):
        print("This is protected")
    def __three(self):
        print("This is private")
    def display(self):
        self.one()
        self._two()
        self.__three()
class employee(government):
    def display1(self):
        self.one()
        self._two()
        try:
         self.__three()
        except:
          print("Error")
class staff:
     def display2(self,obj):
        obj.one()
        obj._two()
        try:
         obj.__three()
        except:
          print("Error")
x=government()
x.display()
y=employee()
y.display1()
z=staff()
z.display2(x)