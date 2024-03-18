def add_numbers(first_number, second_number):
	result = first_number + second_number
	return result

num1 = int(input("Enter a number "))
num2 = int(input("Enter a second number "))

num3 = 343
num4 = 77

sum = add_numbers(num1, num2)
sum2 = add_numbers(num3, num4)
sum3 = add_numbers(num1, num4)
sum4 = add_numbers(num1, num3)

print(sum)
print("The second sum is: ", sum2)
print("The third sum is: ", sum3)
print("The fourth sum is: ", sum4)