'''
@Author: your name
@Date: 2020-05-27 14:57:59
@LastEditTime: 2020-05-27 14:58:52
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/107.Binary_Tree_Level_Order_Traversal_II.py
'''

# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

''' For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = [root]
        levels = []
        while queue:
            level = queue
            levels.append([leaf.val for leaf in level])
            queue = []
            for leaf in level:
                if leaf.left:
                    queue.append(leaf.left)
                if leaf.right:
                    queue.append(leaf.right)
        return levels[::-1]