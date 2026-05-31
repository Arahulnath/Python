'''
age = int(input("Enter your age : "))
Monthly_income=int(input("Enter your monthly income : "))21
Credit_Score=int(input("Enter your credit score : "))
if age>=21 and Monthly_income>=30000 and Credit_Score>=700:
    print("Loan approved")
else:
    print("Loan not approved")
'''
#withdrawal Atm
'''  
amount=int(input("Enter your amount : "))
balance=10000
if amount>balance:
    print("Invalid Balance ")
elif amount%10!=0:
    print("Enter invalid amount")
elif amount<0:
    print("Enter amount more than 0")
else:
    print("Withdrawal Sucessfull")
    '''

amount2=1000
day="Sat"
membership="no"

if(amount2>=1000 and day in ["Sat","Sun"]) or membership=="yes":
    print("Discount approved")
else:
    print("No Discount")