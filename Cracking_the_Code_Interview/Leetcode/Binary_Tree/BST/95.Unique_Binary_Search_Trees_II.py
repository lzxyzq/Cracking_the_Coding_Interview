'''
@Author: your name
@Date: 2020-05-27 01:22:16
@LastEditTime: 2020-05-30 12:03:39
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/BST/95.Unique_Binary_Search_Tree_II.py
'''
# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

''' Example:            
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def generateTrees(self, n):
        def generate(l, r):   # split between [l, r)
            if l == r:
                return [None]
            nodes = []
            for i in range(l, r):
                for lchild in generate(l, i):
                    for rchild in generate(i+1, r):
                        node = TreeNode(i)   # +1 to convert the index to the actual value
                        node.left = lchild
                        node.right = rchild
                        nodes.append(node)
            return nodes
        return generate(1, n+1) if n else []
if __name__ == '__main__':
    print(Solution().generateTrees(3))
    