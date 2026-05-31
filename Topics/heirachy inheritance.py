class mobile: #parent
    def touch(self):
        print("This is a touch phone")
class iphone(mobile): #child
    def name(self):
        print("This is iphone")
class android(mobile): #child
    def name1(self):
        print("This is android  ")
x=iphone()
x.touch()
x.name()
y=android()
y.touch()
y.name1()