class account():
    def __init__(x,accnum,accbal):
        x.accnumber=accnum
        x.accbalance=accbal
    def withdraw(x,amount):
        withdra= x.accbalance-amount
        if withdra>0:
           x.accbalance=withdra
        else:
            x.accbalance="insufficient balance"
       
            
    def display(x):
        print(f"the account number is {x.accnumber}\n the blance current balance is : {x.accbalance} rs")
ac=account(233234424424,500)
ac.withdraw(int(input("enter the withdraw amount : ")))
ac.display()


        




       

        
        