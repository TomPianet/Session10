file_name = "x-file.txt"
fd = open(file_name, "w")

while True:
    line = input("Enter a line ( or just press Enter to quit) : ")
    if line:
        fd.write("Hello, World!")
    else:
        break

fd.close()

