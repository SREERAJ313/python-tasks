class person():
    def __init__(x,a,b):
        x.name=a
        x.age=b
class son(person):
    def __init__(x,a,b,c):
        person.__init__(x,a,b)
        x.dob=c

    def displays(x):
        print("name :",x.name)
        print("age :",x.age)
        print("DOB :",x.dob)
       

    
        
per=son("hari",30,"21-01-2003")
per.displays()