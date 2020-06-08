'''
@Author: your name
@Date: 2020-05-28 21:51:30
@LastEditTime: 2020-05-28 22:14:30
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/114.Flatten_Binary_Tree_to_Linked_List.py
'''
# Given a binary tree, flatten it to a linked list in-place.
''' For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
 '''
class Solution:
    def flatten(self, root) :
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None 
        
        def dfs(root):
            if not root:
                return None
            dfs(root.right)
            dfs(root.left)
            
            root.right = self.prev
            root.left = None 
            self.prev = root 
        dfs(root)
