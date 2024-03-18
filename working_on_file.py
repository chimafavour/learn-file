username = input("what is your name?")
user_age = int(input("how old are you?"))


file_handle = open("demo_file.txt","w")
file_handle.write(f"{username}, you are welcome,\n God Bless You.")
if user_age > 17:
	file_handle.write("You are QAULIFIED to drive")
else:
	print("you are not QAULIFIED to drive")
file_handle.close()
file_handle = open("demo_file.txt","r")
file_content = file_handle.read()
print(file_content)
file_handle.close()