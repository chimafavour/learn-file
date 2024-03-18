import math

def sqrt_numbers(num):
	result = math.sqrt(num)
	return result

num1 = int(input("enter a numbers "))
num2 = int(input("enter a second_numbers "))

num3 = 1000
num4 = 50

sqrt = sqrt_numbers(num1)
sqrt1 = sqrt_numbers(num2)
sqrt2 = sqrt_numbers(num3)
sqrt3= sqrt_numbers(num4)

print(sqrt)
print("the first_numbers is, ",sqrt2)
print("the second_numbers is, ",sqrt3)