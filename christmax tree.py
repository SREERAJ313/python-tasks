def starsq(x):
    size=x*2
    for i in range(1,size,2):
        for j in range(i,i+5,2):
            for l in range(size-j+x):
                print(" ", end="")
            for k in range(j):
               print("*",end=" ")
            print()
def leg():
    x=3
    for i in range(x):
        for l in range(1,x+1):
            print("  ", end="  ")
        for j in range(x):
            print("*",end=" ")
        print()        
starsq(6)
leg()




# def triapttn(x):
#    print("      *")
#    lst=[]

#    for row in range(x):
#         for i in range(2):
#            print('   ' * (2 - i - 1), end=' ') 
#            print(' *' *lst[i])  
# triapttn(3)
# print("    * * *")
# print("    * * *")