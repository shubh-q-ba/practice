def sequence_new(x):
    num_seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       num_seq.append(x)    
    return num_seq
a = int(raw_input())
print "Sequence for integer -", a
print(sequence_new(a))
