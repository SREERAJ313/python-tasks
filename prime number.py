a=int(input("enter the number: "))
flag=True
if a==0 or a==1:
    print(a,'is not a prime')
elif a >1:
    for i in range(2,a):
        if (a % i) == 0:
            flag=False
            break
if flag :
    print("is  prime")
else:
    print('is not  prime')