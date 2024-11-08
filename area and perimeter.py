radious=int(input("enter the radious :"))
def areaofcircle(x):
    pi=3.14
    rsq=x*x
    area=pi*rsq
    return area
def perimeterofcircle(x):
      pi=3.14
      peri=2*pi*x
      return peri

    



print("area of circle with rarious",radious,"=",areaofcircle(radious))
print("perimeter of circle with rarious",radious,"=",perimeterofcircle(radious))


