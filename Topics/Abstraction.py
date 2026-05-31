from abc  import ABC, abstractmethod

class webpage(ABC):
    @abstractmethod  # mandatory use in child class
    def login(self):
        pass
    @abstractmethod # mandatory use in child class
    def logout(self):
        pass
    def display(self): #it is an non abstract class
        pass
class feature(webpage):
    def login(self):
        print("login")
    def logout(self):
        print("logout")
s1=feature()
s1.login()
s1.logout()