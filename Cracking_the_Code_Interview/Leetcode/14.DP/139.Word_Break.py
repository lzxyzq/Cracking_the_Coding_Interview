# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.

''' 
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false 
'''

# Method 1 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n+1)]
        s = ' ' + s
        dp[0] = True 
        for i in range(1,n+1):
            for j in range(i):
                if dp[j] == True :
                    if s[j+1:i+1] in wordDict:
                        dp[i] = True
                        break
        return dp[-1]

# Method 2 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def canBreak(s,m,wordDict):
            if s in m:
                return m[s]
            if s in wordDict:
                m[s] = True
                return True
            for i in range(1,len(s)):
                r = s[i:]
                if r in wordDict and canBreak(s[0:i],m,wordDict):
                    m[s] = True
                    return True
            m[s] = False
            return False
        return canBreak(s,{},wordDict)