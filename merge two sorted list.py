def sorte(a,b):
    sorted1=sorted(a)
    sorted2=sorted(b)
    print(sorted1)
    print(sorted2)
    merge(sorted1,sorted2)
    
def merge(x,y):
    result=sorted(x+y)
    print(result)
   

   
    
A=[2,5,6,7,8]
B=[10,4,5,6,1]
c=sorte(A,B)


