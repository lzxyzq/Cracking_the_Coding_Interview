# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

""" 
Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned. 
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        while l <= r:
            m = l + (r - l) // 2
            if m * m <= x < (m+1)*(m+1):
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        return r