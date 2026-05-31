class Myclass:
    company_name="Google"
    def change_name(self,name):
        self.company_name=name
    @classmethod
    def change(cls,name):
        cls.company_name=name
    @staticmethod
    def change1(name):
        company_name=name
obj=Myclass()
obj.change_name("Amazon")
print(obj.company_name)
Myclass.change("It")
print(Myclass.company_name)
Myclass.change1("Flip")
print(Myclass.company_name)