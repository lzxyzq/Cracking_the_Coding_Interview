# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

''' 
Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa". 
'''


# Method 1 
# Brute Force 
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j + 1] == s[i:j + 1][::-1]:
                    count += 1
        return count

# Method 2 
# 当在回文串两端各加入两个相同的字符的时候，形成的新字符仍旧是回文串
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.count = 0
        for i in range(len(s)):
            self.helper(s,i,i)
            self.helper(s,i,i+1)
        return self.count
    def helper(self,s,left,right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            self.count += 1
            left -= 1
            right += 1