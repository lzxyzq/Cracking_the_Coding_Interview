'''
@Author: your name
@Date: 2020-06-10 13:35:24
@LastEditTime: 2020-06-10 14:22:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/String/49.Group_Anagrams.py
'''
# Given an array of strings, group anagrams together.
''' 
Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
] 
'''

''' Note:
All inputs will be in lowercase.
The order of your output does not matter. 
'''
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

# Complexity Analysis
# Time Complexity: O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
# Space Complexity: O(NK), the total information content stored in ans.
