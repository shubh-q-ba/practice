count=0
filename = input("Enter file name: ")
with open (filename,'r') as f:
    for line in f:
        count+=1

print("Number of lines:")
print count

