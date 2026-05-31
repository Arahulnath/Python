class father :
    def house(self):
        print("House of father")
class mother:
    def shop(self):
        print("Shop of mother")
class son(father,mother):
    def factory(self):
        print("Factory of son")
s1=son()
s1.factory()
s1.house()
s1.shop()
