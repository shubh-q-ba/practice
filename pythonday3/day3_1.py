def add(x,y):
    return x+y
def subs(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y

print ("Select the operation you want to use - \n1.Addition \n2.Substraction \n3.Multiplication \n4.Division")
choice = input ("Your choice is (Eg: 1 or 2 etc) - ")

num1 = raw_input("First number - ")
while num1.isalpha():
    print "Only numbers can be used."
    print "Enter first number: "
    return float(num1)
num2 = raw_input("Second number - ")
while num2.isalpha():
    print "Only numbers can be used."
    print "Enter first number: "
    return float(num2)



if choice == 1:
    print "The sum of ",num1, " and",num2, " is", add(num1,num2)
elif choice == 2:
    print "The difference of ",num1, " and",num2, " is", subs(num1,num2)
elif choice == 3:
    print "The multiplication of ",num1, " and",num2, " is", mult(num1,num2)
elif choice == 4:
    print "The division of ",num1, " and",num2, " is", div(num1,num2)
else:
    print ("Invalid Input")

    
    

