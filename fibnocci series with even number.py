def fibseriesofeven(x):
    n2 = 1
    n1=0
    reslut=0

    print(n1)
    for i in range(x):
          n3 = n1 + n2
          if n3<=x:
            
            n1 = n2
            n2 = n3
        
            if n3%2==0:
             print(n3)
             
             reslut+=n3
          else:
            break
    print("the sum :",reslut)
    
fibseriesofeven(int(input("enter the limit: ")))