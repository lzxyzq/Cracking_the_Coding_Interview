'''
@Author: your name
@Date: 2020-05-23 22:47:59
@LastEditTime: 2020-05-23 22:48:00
@LastEditors: your name
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Tree/113.Path_Sum_II.py
'''
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

class Solution:
    def pathSum(self, root, S) :
        A = []
        if root == None: 
            return []
        def dfs(node,path):
            if(node.left,node.right) == (None,None) and sum(path) == S: 
                A.append(path)
                return 
            if node.left: dfs(node.left,path+[node.left.val])
            if node.right: dfs(node.right,path+[node.right.val])  
        dfs(root,[root.val])
        return A
    
    