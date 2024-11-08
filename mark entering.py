a=input('enter your name :')
print("YPUR NAME IS : ",a)

print("ENTER YOUR SUBJECT WAISE MARK ")
mark1=float(input('MATHS (OUT OF 100): '))
mark2=float(input('CHEMISTRY (OUT OF 100): '))
mark3=float(input('PHYSICS (OUT OF 100): '))
mark4=float(input('ENGLISH (OUT OF 100): '))

def total():
    tmark=mark1+mark2+mark3+mark4
    return tmark
print("the total mark: ",total())

def avrage():
    t=total()
    avg=t/4
    return avg
print("AVRAGE : ",avrage())

def percentage():
    b=avrage()
    c=b/100
    d=c*100
    return d
print("PERCENTAGE OF TOTAL MARKS: ",percentage(),'%')

