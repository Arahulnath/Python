#Student task manager
tasks=[]

while True:
    choice=int(input("Enter choice 1.ADD , 2.View 3.Exit"))
    if choice==1:
        items=input("Enter What task to add")
        tasks.append(items)
    elif choice==2:
        for i,t in enumerate(tasks,1):
            print(i,t)
    else:
        break

