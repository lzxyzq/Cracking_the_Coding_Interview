'''
@Author: your name
@Date: 2020-06-08 21:46:10
@LastEditTime: 2020-06-08 23:48:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/38.Count_and_Say.py
'''
# The count-and-say sequence is the sequence of integers with the first five terms as following:
''' 
1.     1
2.     11
3.     21
4.     1211
5.     111221 
'''
class Solution:
    def countAndSay(self, n) :
        output = '1'
        for i in range(2, n+1):
            res = ''
            cur = output[0]
            count = 1
            for x in output[1:]:
                if x == cur:
                    count += 1
                else:
                    res += str(count) + cur
                    count = 1
                    cur = x
                
            res += str(count) + cur
            output = res
            
        return output