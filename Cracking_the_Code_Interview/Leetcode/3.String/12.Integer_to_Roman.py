'''
@Author: your name
@Date: 2020-06-10 15:16:52
@LastEditTime: 2020-06-10 20:51:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/12.Integer_to_Roman.py
'''
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        s,q,m,n = '',num,1,5
        while q:
            q, r = divmod(q, 10)
            if 0 < r < 4: s = r*d[m]+s
            elif r == 4: s = d[m]+d[n]+s
            elif r == 5: s = d[n]+s
            elif 5 < r < 9: s = d[n]+(r-5)*d[m]+s
            elif r == 9: s = d[m]+d[m*10]+s
            m, n = 10*m, 10*n
        return s
