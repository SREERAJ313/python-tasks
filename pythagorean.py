a=[3,4,5]
num1=a[0]
num2=a[1]
num3=a[2]
sqnum3=num3*num3
print("third number square: ",sqnum3)
def twovaluesq():
    sqnum1=num1*num1
    sqnum2=num2*num2
    sum=sqnum1+sqnum2
    print('first two value square sum: ',sum)
    return sum
    
def equalcheck():
    sumoffirsttwosq=twovaluesq()
    if(sumoffirsttwosq==sqnum3):
        {
            print("is pythogorian")
        }
    else:
        {
           print('IS NOT')
        }

equalcheck()