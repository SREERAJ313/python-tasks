import random
def second_smal (a):
    random_numbers = [random.randint(1, 100) for _ in range(a)]
    r_sort=sorted(random_numbers)
    smallest=r_sort[1]
    print(f"the array is :{random_numbers} \n the smallest is : {smallest}")
second_smal(5)


