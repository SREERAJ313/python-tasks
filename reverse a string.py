def rev(a):
    str=list(a)
    reversed_lst =[]
    for item in str:
        reversed_lst.insert(0, item)
        str2="".join(reversed_lst)
    print (str2)
a="hello"
rev(a)