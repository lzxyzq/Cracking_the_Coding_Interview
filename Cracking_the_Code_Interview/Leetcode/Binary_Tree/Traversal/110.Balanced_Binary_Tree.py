'''
@Author: your name
@Date: 2020-05-28 18:58:52
@LastEditTime: 2020-05-31 10:56:37
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/110.Balanced_Binary_Tree.py
'''
'''
@Author: your name
@Date: 2020-05-28 18:58:52
@LastEditTime: 2020-05-28 19:00:03
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/110.Balanced_Binary_Tree.py
'''
# Given a binary tree, determine if it is height-balanced.

# For this problem, a height-balanced binary tree is defined as:

# a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

''' Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
'''

class Solution:
    def isBalanced(self, root):
        if not root :
            return True 
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        return (abs(left_height - right_height)<=1) and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def height(self,root):
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1 
        