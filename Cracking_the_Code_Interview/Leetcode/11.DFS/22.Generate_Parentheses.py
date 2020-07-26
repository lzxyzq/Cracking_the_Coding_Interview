# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

""" 
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
] 
"""
# Method 1
class Solution:
    def generateParenthesis(self,n):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return
            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

# Method 2 
class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return []
        res = []
        self.dfs(n,n,'',res)
        return res
    def dfs(self,l,r,path,res):
        if r < l : # l should always larger than r .but this is the residual num so is r< l 
            return 
        if l == 0 and r == 0 :
            res.append(path)
        if l > 0 :
            self.dfs(l-1,r,path+'(',res)
        if r > 0 :
            self.dfs(l,r-1,path+')',res) 