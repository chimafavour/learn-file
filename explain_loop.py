for index in range(400 + 1):
	if index % 3 == 0:
		print("Fizz")
	elif index % 5 == 0:
		print ("bizz")
		continue
	print(index)