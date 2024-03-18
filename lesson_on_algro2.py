#open the file
file_handle = open("demo_file.txt","w")

# creat the content we want to write on the file
content = "the lord is your strength \nGod bless you \nhave a nice day"

# write on the content of the file
file_handle.write(content)

# close the file
file_handle.close()

""" How to read from the 
file in python."""

# open the file
second_file_handle = open("demo_file.txt")

# tell me the remaining quantity
file_content = second_file_handle.read()

# print out the content of the file
print(file_content)

# close the file
second_file_handle.close()