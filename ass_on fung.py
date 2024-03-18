def substract_nmmbers(first_number, second_number):
	result = first_number - second_number
	return result
num1 = int(input("enter a numbers"))
num2 = int(input("enter a numbers"))
num3 = 343
num4 = 77
sum = substract_nmmbers(num1, num2)
sum2 = substract_nmmbers(num2, num3)
sun3 = substract_nmmbers(num3, num4)
print(sum)
print("the second sum is ", sum2)
print("the third sum is ", sum3)
print("the fourth sum is ", sum4)