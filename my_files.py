file_handle = open("demofile.txt","r")
file_content = file_handle.read()
# print(file_content)
for line in file_content:
	print(line)



file_handle = open("demofile2.txt","a")
fi