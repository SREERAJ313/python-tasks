class palian():
    def value(x):
        x.a=input("enter the somthing to check it is palian drome: ")
    def check(x):
        if x.a.isalnum():
            x.b=list(x.a)
            x.reversed_lst =[]
            for item in x.b:
                x.reversed_lst.insert(0, item)
        x.c=x.reversed_lst    
    def display(x):
        if x.b==x.c:
            print(x.a,"-is a paliamdrome:")
        else:
            print("is not a paliandrome")
chk=palian()
chk.value()
chk.check()
chk.display()



  
        

        