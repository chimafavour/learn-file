user_input = input("what score did you have ?")

stud_score = int(user_input)

if stud_score > 100:  
    print ("very excellent")
elif stud_score > 95:
    print("excellent")
elif stud_score > 90:
	print("awesome")
elif stud_score > 85:
    print("wonderful")
elif stud_score > 80:
     print("very good")
elif stud_score > 75:
    print("good")
elif stud_score > 70:
    print("keep trying")
elif stud_score > 65:
    print("poor")
elif stud_score > 60:
     print("very poor")
else:
     print("student failed")
                 