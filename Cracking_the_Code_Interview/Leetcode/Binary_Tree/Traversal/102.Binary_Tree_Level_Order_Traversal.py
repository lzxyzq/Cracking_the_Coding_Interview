'''
@Author: your name
@Date: 2020-05-27 15:04:14
@LastEditTime: 2020-05-31 16:22:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/102.Binary_Tree_Level_Order_Traversal.py
'''
#  Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
''' 
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
 '''
class Solution:
    def levelOrder(self, root):
        traversal_queue = [ root ] if root else []
        
        path = []
        
        while traversal_queue:
            
            cur_level_path, next_level_queue = [], []
            
            for node in traversal_queue:
                
                # update current level traversal path
                cur_level_path.append( node.val )
                
                if node.left:
                    next_level_queue.append( node.left )
                
                if node.right:
                    next_level_queue.append( node.right )
            
            # add current level path into path collection
            path.append( cur_level_path )
            
            # update next_level_queue as traversal_queu
            traversal_queue = next_level_queue
            
        return path