#passing value to class
class government:
    def __init__(self,name,id):
        self.x=name
        self.y=id

    def display(self):
        print(f"Name :  {self.x},ID : {self.y}")


s1=government("rahul","1234")
s1.display() 