
class person():
    def __init__(self,a,b,c,):
        self.name=a
        self.age=b
        self.phonenumber=c
    def details(self):
        x=open("hello.txt","w")
        x.write(f" Name : {self.name}\n Age : {self.age}\n Phone number : {self.phonenumber}")
        x.close()
       
name=input("enter your name : ")
age=int(input("enter your age : "))
ph=int(input("enter your phone number : "))

object=person(name,age,ph)
object.details()
        
