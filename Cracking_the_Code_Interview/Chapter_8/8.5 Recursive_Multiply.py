# Write a recursive function to multiply two positive integers without using the * operator.You can use addition,subtraction,and bit shifting,but you should minimize the number of those operations.

def multiply(x,y): 
    # 0 multiplied with anything 
    # gives 0  
    if(y == 0): 
        return 0
    # Add x one by one  
    if(y > 0 ): 
        return (x + multiply(x, y - 1)) 
    # The case where y is negative 
    if(y < 0 ): 
        return -multiply(x, -y)  
# Driver code 
print(multiply(5, -11)) 

#-----------------------------------------
# The value of a*b is same as (a*2)*(b/2) if b is even, otherwise the value is same as ((a*2)*(b/2) + a). In the while loop, we keep multiplying ‘a’ with 2 and keep dividing ‘b’ by 2. If ‘b’ becomes odd in loop, we add ‘a’ to ‘res’. When value of ‘b’ becomes 1, the value of ‘res’ + ‘a’, gives us the result.

def russianPeasant(a, b): 
    res = 0 
    # While second number doesn't become 1 
    while (b > 0): 
        # If second number becomes odd, add the first number to result 
        if (b & 1): 
            res = res + a 
        a = a << 1 # double 
        b = b >> 1 # divide by 2
    return res 
print(russianPeasant(18, 1)) 
print(russianPeasant(20, 12)) 