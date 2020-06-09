'''
@Author: your name
@Date: 2020-06-08 19:22:59
@LastEditTime: 2020-06-08 19:22:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/8.String_to_Integer.py
'''
# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

class Solution:
    def myAtoi(self, str: str) -> int:
        min_int , max_int = -2147483648, 2147483648
        str = str.lstrip()
        if not str:
            return 0 
        sign = ''
        if str[0] == '-' :
            sign = '-'
            str = str[1:len(str)]
        elif str[0] == '+' :
            str = str[1:len(str)]
        if not str or not str[0].isnumeric():
            return 0
        num = ""
        for c in str:
            if c.isnumeric():
                num += c
                continue
            break
        num = int(sign + num)
        num = max(num, min_int)
        num = min(num, max_int)
        return num