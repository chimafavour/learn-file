
file_handle = open("demofile2.txt", "a")
file_handle.write(" woops! i have deleted the content! " )
file_handle.close()


f_handle = open("demofile2.txt", "r")
print (f_handle.read())
f_handle.close()
