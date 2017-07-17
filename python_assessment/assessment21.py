filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
#reversed function uses for loop and rstrip removes all the spaces at end of lines
