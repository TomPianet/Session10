file_name = ("x-file.txt")
fd = open(file_name)         # r is implicit

print("here are the contents of the file:")
print(fd.read())

fd.close()

