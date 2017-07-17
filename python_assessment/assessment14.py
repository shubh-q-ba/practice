def is_Power_of_three(n):
    while (n % 2 == 0):
         n /= 2;         
    return n == 1;
a = int(raw_input())
print "Checking whether integer given as an input is a power of 2 "
print(is_Power_of_three(a))
