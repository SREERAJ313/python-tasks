def pascal_tri(x):
    tri=[]
    for i in range(x):
       r=[1]*(i+1)
       for j in range(1,i):
           r[j]=tri[i-1][j-1]+tri[i-1][j]
       tri.append(r)
    return tri
def print_pascals_triangle(tri): 
    for row in tri:
        print(" ".join(map(str, row)))
       
     
tri=pascal_tri(5)
print_pascals_triangle(tri)
   

