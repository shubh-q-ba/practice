result_str="";
a = int(raw_input("Enter no of rows = "))
b = int(raw_input("Enter no of columns = "))
if a>b:
    for row in range(0,a):    
        for column in range(0,b):     
            if (column == 0 or (row == a-1 and column < b)):
                result_str=result_str+"*"    
            else:      
                result_str=result_str+" "    
        result_str=result_str+"\n"    
    print(result_str);
else:
    print ("the Alphabet won't be in right shape")
    
