user_input = input ("What is your score ? ")

stud_score = int(user_input)

if stud_score > 100:
	print("Very excellent A+++")
elif stud_score > 90:
	print("Very excellent A+")
elif stud_score > 80:
	print ("Excellent")
elif stud_score > 70:
	print("Awesome")	
elif stud_score > 60:
	print("Wonderful")
elif stud_score > 50:
    print("Average")
else:
	print("Student failed")