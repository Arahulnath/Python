
class government: #parent
    def job(self):
        print("job")
class staff(government): #child
    def position(self):
        print("Iam in clurk")
    def job(self): # overwrite the government class
        print("Position of job")
x=staff()
x.job()
x.position()
