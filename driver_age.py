user_age = input("How old are you? ")

user_age = int(user_age)

if user_age < 18:
	print("You are NOT qualified to drive.")
else:
	print("You are QAULIFIED to drive.")