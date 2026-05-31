class iphone:
    def phone(self):
        print("This is i phone")
class model(iphone):
    def pro(self):
        print("This is pro version")
class user(model):
    def model(self):
        print("This is a iphone 15pro max")
s1=user()

s1.phone()
s1.pro()
s1.model()