'''
@Author: your name
@Date: 2020-05-23 17:28:57
@LastEditTime: 2020-05-23 17:34:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Recursive/Maximum_Path_Sum.py
'''
# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

''' Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42 '''

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.global_max_path = float("-inf")
        def get_max_gain(node):
            # nonlocal global_max_path
            if node is None:
                return 0
            # Discard negative value by max( ..., 0 )
            gain_on_left = max(get_max_gain(node.left), 0) 
            gain_on_right = max(get_max_gain(node.right), 0)
            # update local max, either left node + current node, or right node + current node
            local_max = node.val + max(gain_on_left, gain_on_right)
            # use current node as bridge, update if path sum of connection is bigger than global_max
            self.global_max_path = max(self.global_max_path, node.val + gain_on_left + gain_on_right)
            return local_max
        
        get_max_gain(root)
        return self.global_max_path	

# Method 2 
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float("-inf")
        self.dfs(root)
        return self.max_sum
    def dfs (self,root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        Sum = root.val
        if l > 0:
            Sum+= l
        if r > 0:
            Sum+= r
        self.max_sum = max(self.max_sum, Sum)
        return max(r, l) + root.val if max(r, l) > 0 else root.val
            
                           