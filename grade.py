def grade(x):
    if x>=0 and x<=100:
        if x>=90 and x<=100:
            print("A GRADE")
        elif x>=80 and x<=90:
            print("B GRADE")
        elif x>=70 and x<=80:
            print("C GRADE")
        elif x>=60 and x<=70:
            print("D+ GRADE")
        elif x>=50 and x<=600:
            print("D+ GRADE")
        else:
            print(" fail ")
    else:
        print("invalid entry")
grade(int(input("enter ur mark in percentage: ")))
