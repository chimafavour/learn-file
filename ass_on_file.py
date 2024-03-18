first_name = input("what is your first_name?")
middle_name = input("what is your middle_name?")
last_name = input("what is your last_name?")
user_age = int(input("how old are you?"))


file_handle = open("demo_file.txt" "w")
file_handle.write(f"{first_name},{middle_name},{last_name}, you are welcome \n have your sit \n God Bless You.")
if user_age > 16:
	file_handle.write("you are QAULIFIED to drive")
else:
	print("you are not QAULIFIED to drive")
file_handle.close()

file_handle.open("demo_file.txt" "r")
file_content = file_handle.read()
print(file_content)
file_handle.close()
