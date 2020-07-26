# Find the sum of all left leaves in a given binary tree.
''' 
Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24. 
'''

# Method 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode):
        def traverse(node, left):
            ret_val = 0
            if not node.left and not node.right and left:
                ret_val = node.val
            else: 
                if node.left:
                    ret_val += traverse(node.left, True)
                if node.right:
                    ret_val += traverse(node.right, False)
            return ret_val
        if root is None:
            return 0
        return traverse(root, False)
    
# Method 2 

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode):
        result = 0
        stack = [(root, False)]
        while stack:
            curr, is_left = stack.pop()
            if not curr:
                continue
            if not curr.left and not curr.right:
                if is_left:
                    result += curr.val
            else:
                stack.append((curr.left, True))
                stack.append((curr.right, False))
        return result
