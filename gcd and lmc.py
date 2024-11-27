def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
num1 = 12
num2 = 18
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")
