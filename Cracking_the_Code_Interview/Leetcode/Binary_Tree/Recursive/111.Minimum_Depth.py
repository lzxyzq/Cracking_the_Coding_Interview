'''
@Author: your name
@Date: 2020-05-23 17:07:38
@LastEditTime: 2020-05-23 17:26:43
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Recursive/111.Minimum_Depth.py
'''
# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

''' Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
 '''

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left and root.right:
            return min(self.minDepth(root.left),self.minDepth(root.right)) + 1
        else:
            return max(self.minDepth(root.left),self.minDepth(root.right)) + 1