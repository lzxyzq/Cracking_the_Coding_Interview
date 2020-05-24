'''
@Author: your name
@Date: 2020-05-23 21:18:27
@LastEditTime: 2020-05-23 21:25:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/Same_Tree.py
'''
# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

''' 
Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
 '''
class Solution:
    def isSameTree(self, p, q) :
        if p and q:
            # both p and q exist
            return (p.val == q.val) and self.isSameTree( p.left, q.left) and self.isSameTree( p.right, q.right )
        
        elif not p and not q:
			# both p and q are empty node ( i.e., None )
            return True
        
        else:
			# either p or q is empty, the other is non-empty.
            return False