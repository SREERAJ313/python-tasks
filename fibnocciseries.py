
def fibseries(x):
    n2 = 1
    n1=0
    count = 0
    if x <= 0:
        print("Please enter a positive integer")
    elif x == 1:
        print("Fibonacci sequence upto", x, ":")
        print(n1)
    else:
  
        print("Fibonacci sequence:")
    while count < x:
        print(n1)
        n3 = n1 + n2
    
        n1 = n2
        n2 = n3
        count =count+ 1

fibseries(int(input("enter the limit: ")))





