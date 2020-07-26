'''
@Author: your name
@Date: 2020-05-27 18:03:54
@LastEditTime: 2020-05-27 18:26:02
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/199.Binary_Tree_Right_Side_View.py
'''
# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
''' 
Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <--- 
'''

class Solution:
    def rightSideView(self, root) :
        self.maxHeight = float('-inf')
        self.view = []
        self.helper(root, 0)
        return self.view
    def helper(self, root, height):
        if not root:
            return 
        if self.maxHeight < height:
            self.view.append(root.val)
            self.maxHeight = height
        self.helper(root.right, height + 1)
        self.helper(root.left, height + 1)