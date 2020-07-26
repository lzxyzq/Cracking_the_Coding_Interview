'''
@Author: your name
@Date: 2020-05-23 17:35:38
@LastEditTime: 2020-05-23 17:37:47
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Recursive/129.Sum Root to Leaf Numbers.py
'''
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
# Find the total sum of all root-to-leaf numbers.
''' Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
Example 2:

Input: [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
 '''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(root, n):
            if not root:
                return 0
            n = n*10 + root.val
            if not root.left and not root.right:
                return n
            else:
                return dfs(root.left, n) + dfs(root.right, n)
        return dfs(root, 0)