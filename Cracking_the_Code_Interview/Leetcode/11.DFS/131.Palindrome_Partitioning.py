# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

""" 
Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
] 
"""

class Solution:
    def partition(self, s: str) :
        res = []
        self.dfs(s,[],res)
        return res
    def dfs(self,s,path,res):
        if not s:
            res.append(path)
        for i in range(len(s)):
            if self.isPalindrom(s[:i+1]):
                self.dfs(s[i+1:],path+[s[:i+1]],res)
    def isPalindrom(self,s):
        return s == s[::-1]

if __name__ == '__main__':
    print(Solution().partition("aab"))
    