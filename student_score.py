user_input = input("What score did you get? ")

student_score = int(user_input)

if student_score > 100:
	print("Very excellent A++")
elif student_score > 75:
	print("Excellent A")
elif student_score > 60:
	print("Very good B")
elif student_score > 50:
	print("Average C")
elif student_score > 40:
	print("Poor D")
else:
	print("Fail F")

