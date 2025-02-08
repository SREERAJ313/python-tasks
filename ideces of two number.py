def indeces_of_(num, target):
    even=[]
    for n in range(len(num)):
        if num[n]%2 == 0:
            even.append(num[n])
    for i in range(len(even)):
        num1 = num[i]
        for j in range(i + 1, len(even)):
            num2 = num[j]
            if num1 * num2 == target:
                return [i, j]
    return "no even number"

# Example usage
num = [1,2,3,4]
target = 6
print(indeces_of_(num, target))
