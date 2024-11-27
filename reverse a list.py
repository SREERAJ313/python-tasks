list1=[1,2,3,4,5,6,7]
def revoflist(x):
    reversed_lst = []
    for item in x:
        reversed_lst.insert(0, item)
    return reversed_lst
revList=revoflist(list1)
print("the orginal list: ",list1)
print("the rev list: ",revList)
    