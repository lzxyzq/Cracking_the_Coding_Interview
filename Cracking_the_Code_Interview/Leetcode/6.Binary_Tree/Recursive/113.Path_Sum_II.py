# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

''' Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1 '''

class Solution:
    def pathSum(self, root: TreeNode, S: int) -> List[List[int]]:
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