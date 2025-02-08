def disnum(a):
    digit_list = [int(digit) for digit in str(a)]
    pwr=0
    total=0

    for i in range (len(digit_list)):
        
        pwr=pwr+1
        x=digit_list[i]
        result=x**pwr
        total=total+result
    if total==a:
        print("is a disarium =",a)
    else:
        print(a,"is not disarium")

        
   

   
   
    



a = 135
disnum(a)

