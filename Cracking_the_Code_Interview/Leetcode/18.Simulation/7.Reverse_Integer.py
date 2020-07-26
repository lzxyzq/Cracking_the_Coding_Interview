# Given a 32-bit signed integer, reverse digits of an integer.
''' 
Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21 
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = True
        else:
            sign = False
        
        max_int = pow(2, 31)-1
        min_int = pow(-2, 31)
        
        res = 0 
        x = abs(x)
        while (x!=0):
            temp = x % 10
            x //= 10
            res = 10*res + temp
            
        if res > max_int or res < min_int:
            return 0
            
        if(sign):
            return -res
        else:
            return res
        
# Time Complexity: O(log(x))  
# Space Complexity: O(1)
