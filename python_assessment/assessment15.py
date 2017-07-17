def last(n):
    return n[-1]

def sort(tuples):
    return sorted (tuples, key=last)

a=input ("Enter a list of tuples -")
print("sorted:")
print(sort(a))
#use of key like the class assignment and application of tuples
