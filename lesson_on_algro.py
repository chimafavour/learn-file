# open the file
file_handle = open("demo_file.txt", "w")

# create the content we want to write to the file
content = "Hello! \nNice to see you today. God bless you. \nDo have a nice day."

# write the content to the file
file_handle.write(content)

# close the file
file_handle.close()




"""How to read from the 
file in python."""

# open the bottle
second_file_handle = open("demo_file.txt")

# tell me the remaining quantity
file_content = second_file_handle.read()

# print out the content of the file
print(file_content)

# close the file
second_file_handle.close()