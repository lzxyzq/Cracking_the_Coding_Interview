'''
@Author: your name
@Date: 2020-05-23 18:57:35
@LastEditTime: 2020-05-23 19:24:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/BST/98.Validate.py
'''

# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

''' Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 '''
class Solution:
    def isValidBST(self, root) :
        def rec(node, left, right):
            if node:
                if node.val <= left or node.val >= right: return False
                return rec(node.left, left, node.val) and rec(node.right, node.val, right)
            return True
        return rec(root, -float('inf'), float('inf') )