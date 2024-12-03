def removeduplicates(list1):
    removedlst=[]
    updatedlst=[]
    
    for item in list1:
        if item not in removedlst:
            updatedlst.append(item)
            removedlst.append(item)
    return updatedlst
list1=[1,2,1,3,1,4,1,5]

print(removeduplicates(list1))
