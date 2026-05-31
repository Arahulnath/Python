#Online Shoping discount system
def no_discount(total):
    return total
def festival_discount(total):
    return total*0.90
def student_discount(total):
    return total*0.80
def premium_discount(total):
    return total-200
def applying_discount(total,discount_fun):
    print("------Applying Discount------")
    final_dis=discount_fun(total)
    return final_dis

def shopping_cart():

    print("----Welcome to our Discount System---- ")
    total = 0
    while True:
      try:

        item=input("Enter item for discount : ")
        price=float(input("Enter price of item : "))
        quantity=int(input("Enter quantity of item : "))

        total+=price*quantity
        print(f"{item} added to cart")
        # Choose discount
        print("\nAvailable Discounts:")
        print("1. No Discount")
        print("2. Festival Discount (10%)")
        print("3. Student Discount (15%)")
        print("4. Premium Member Discount (Flat ₹200)")
        print("5.Exit")

        choice = int(input("Choose discount option (1-4): "))
        if choice==1:
            discount=no_discount
        elif choice==2:
            discount=festival_discount
        elif choice==3:
            discount=student_discount
        elif choice==4:
            discount=premium_discount
        elif choice==5:
            break
        else:
            print("Invalid option")
        final=applying_discount(total,discount)
        print(f"Final bill : {final}")
      except Exception :
          print("❌❌❌❌❌❌")
shopping_cart()




