a=[(1,2),(3,1),(2,3)]
index=1
def sort_tuple(lst,index):
    return sorted(lst,key=lambda x : x[index])
result=sort_tuple(a,index)
print(result)
