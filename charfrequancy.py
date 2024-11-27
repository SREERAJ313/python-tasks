def char_frequancy(s):
    list1=list(s)
    frequancy={}
    for i in  list1:
        if i in frequancy:
            frequancy[i]+=1
        else:
            frequancy[i]=1
    return frequancy
print("char frequancy :",char_frequancy(input()))
