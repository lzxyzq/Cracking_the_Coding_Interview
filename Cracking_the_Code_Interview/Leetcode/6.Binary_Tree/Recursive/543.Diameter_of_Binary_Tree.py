# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

''' 
Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3]. 
'''



# 思路1：find out the max of leftDepth & rightDepth while at each node, meanwhile update the total max.
# sum of everynode leftDepth and rightDepth is the path of this node.
# Complexity: Time O(N) Space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.path_length(root)
        return self.diameter
    def path_length(self,root):
        if root:
            left_path = self.path_length(root.left)
            right_path = self.path_length(root.right)
            path = left_path + right_path
            self.diameter = max(self.diameter,path)
            return max(left_path, right_path)+1
        return 0