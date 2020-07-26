# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

# Note: The input string may contain letters other than the parentheses ( and ).

''' 
Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""] 
'''

# Method 1

class Solution:
    def removeInvalidParentheses(self, s: str):
        left = right = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
                    
        self.res = []
        self.dfs(s, 0, left, right)
        return self.res          
    
    def dfs(self,s ,idx ,left ,right):
        if left==0 and right==0:
            if self.isValid(s) and (s not in self.res):
                self.res.append(s)
            return
        
        for i in range(idx,len(s)):
            if s[i]=='(' and left>0:
                self.dfs(s[:i]+s[i+1:], i, left-1, right)
            elif s[i]==')' and right>0:
                self.dfs(s[:i]+s[i+1:], i, left, right-1)
        
            
    def isValid(self,s):
        cnt = 0
        for i in s: 
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0
    
    
# Method 2 

class Solution:
    def removeInvalidParentheses(self, s: str):
        left = right = 0
        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
                    
        self.res = []
        self.visited = set()
        self.dfs(s, 0, left, right)
        return self.res          
    
    def dfs(self,s ,idx ,left ,right):
        self.visited.add(s)       # pruning
        if left==0 and right==0:
            if self.isValid(s) and (s not in self.res):
                self.res.append(s)
            return
        
        for i in range(idx,len(s)):
            if s[i] not in ['(',')']:
                continue
            if (i > 0 and s[i] == s[i - 1]):
                continue
            if s[:i]+s[i+1:] not in self.visited:
                if s[i]=='(' and left>0:
                    self.dfs(s[:i]+s[i+1:], i, left-1, right)
                elif s[i]==')' and right>0:
                    self.dfs(s[:i]+s[i+1:], i, left, right-1)
        
    def isValid(self,s):
        cnt = 0
        for i in s: 
            if i == '(':
                cnt += 1
            elif i == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0
    
    


    

