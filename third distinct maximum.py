def thirddistinctmaximum(num):
    if len(num)<3:
        return print( max(num))
    else:
        a=sorted(num)
        third_num=a[-3]
        print(third_num)
 
num=[3,2,1]
thirddistinctmaximum(num)

