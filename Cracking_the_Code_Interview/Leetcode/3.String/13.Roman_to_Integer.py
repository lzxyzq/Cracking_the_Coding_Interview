'''
@Author: your name
@Date: 2020-06-10 14:25:31
@LastEditTime: 2020-06-10 15:28:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/13.Roman_to_Integer.py
'''
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
''' 
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000 
'''
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 : return 

        rom_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total=0
        prev_value = 0
        if len(s)==1: 
            total =  rom_dict[s]
        else:
            for char in s:
                cur_val = rom_dict[char]
                total += cur_val
                if (prev_value < cur_val):
                    total-= (prev_value*2)
                prev_value = cur_val
                
        return total