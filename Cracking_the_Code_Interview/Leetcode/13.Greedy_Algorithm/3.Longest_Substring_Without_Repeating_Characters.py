# Given a string, find the length of the longest substring without repeating characters.

# Analysis
# Scanning from left to right, when encountering repeated letters, the index+1 of the previous repeated letter is used as the new search starting position until the last letter, the complexity is O(n).

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        usedChar = {}
        start = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[s[i]] = i
        return maxLength    