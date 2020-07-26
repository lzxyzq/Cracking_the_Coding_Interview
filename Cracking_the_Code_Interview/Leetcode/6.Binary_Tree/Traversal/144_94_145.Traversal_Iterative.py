'''
@Author: your name
@Date: 2020-05-23 21:42:04
@LastEditTime: 2020-05-23 22:14:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/144.Preorder_Traversal.py
'''
# Given a binary tree, return the preorder traversal of its nodes' values.
''' Example:
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3] '''


# Pre, In, Post Iteratively Summarization

''' In preorder, the order should be

root -> left -> right

But when we use stack, the order should be reversed:

right -> left -> root
'''
# Pre
class Solution:
    def preorderTraversal(self, root) :
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:  
                    res.append(node.val)
                else:  # preorder: root -> left -> right
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                    stack.append((node, True))
        return res

''' In inorder, the order should be
left -> root -> right

But when we use stack, the order should be reversed:

right -> root -> left

'''
# In 
class Solution:
    def inorderTraversal(self, root):
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res

''' In postorder, the order should be
left -> right -> root

But when we use stack, the order should be reversed:

root -> right -> left
'''
# Post
class Solution:
    def postorderTraversal(self, root: TreeNode):
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                if visited:
                    res.append(node.val)
                else:  # postorder: left -> right -> root
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res