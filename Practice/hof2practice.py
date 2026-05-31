def brother(brother_name):
    def sister(sister_name):
        return f"{brother_name}🫀{sister_name}"
    return sister
brothername=input("Enter your Brother Name : ")
sister_name=input("Enter your Sister Name : ")
connect=brother(brothername)
print(connect(sister_name))