s = raw_input()
count={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        count["DIGITS"]+=1
    elif c.isalpha():
        count["LETTERS"]+=1
    else:
        pass
print "LETTERS", count["LETTERS"]
print "DIGITS", count["DIGITS"]
