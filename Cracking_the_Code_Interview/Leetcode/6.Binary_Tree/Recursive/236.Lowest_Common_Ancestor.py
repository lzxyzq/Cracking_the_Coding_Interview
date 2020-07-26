'''
@Author: your name
@Date: 2020-05-23 17:38:48
@LastEditTime: 2020-05-23 18:39:01
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Recursive/236.Lowest_Common_Ancestor.py
'''
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

''' Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
 '''

''' Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition. 
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root and ( root is p or root is q ):
            return root
        else:
            # common ancestor of p, q exists in left sub-tree
            left_ancestor = self.lowestCommonAncestor( root.left, p ,q)
            # common ancestor of p, q exists in right sub-tree
            right_ancestor = self.lowestCommonAncestor( root.right, p ,q)
            if left_ancestor and right_ancestor:
				# p, q reside in two sides, one in left sub-tree, the other in right sub-tree
                return root
            
            elif left_ancestor:
				# both p, q reside in left sub-tree
                return left_ancestor
            
            elif right_ancestor:
				# both p, q reside in right sub-tree
                return right_ancestor
            
            else:
				# both p, q do not exist in current binary tree
                return None