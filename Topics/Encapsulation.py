# Encapsulation
# Protect object data from direct access, Binds data and method in single class and controlling access to them.

class orders:
         def __init__(self,Customer_name,items,discount,amount):
             self.Customer_name = Customer_name
             self.items = items
             self.__discount=discount
             self.__amount=amount
         def __total_amount(self):
             return self.__amount - self.__discount
         def _admin_veiw(self):
             return {
                 "Customer":self.Customer_name,
                 "Items":self.items,
                 "Discount":self.__discount,
                 "Amount":self.__amount,
                 "Total_amount":self.__total_amount()
             }
         def _customer_view(self):
             return{
                 "Customer":self.Customer_name,
                 "Items":self.items,
                 "Total_amount":self.__total_amount()
             }
class admin_portal:
    def show_order(self,orders):
        return  orders._admin_veiw()
class customer_portal:
    def show_order(self,orders):
        return orders._customer_view()
a=orders("Rahul","[pizza,burger]",50,200)
x=admin_portal()
print("Admin veiw")
print(x.show_order(a))
y=customer_portal()
print("Customer veiw")
print(y.show_order(a))








