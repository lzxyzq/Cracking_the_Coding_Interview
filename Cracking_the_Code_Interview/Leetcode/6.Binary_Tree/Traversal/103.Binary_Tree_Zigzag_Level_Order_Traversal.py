'''
@Author: your name
@Date: 2020-05-27 23:41:00
@LastEditTime: 2020-05-27 23:57:48
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/103.Binary_Tree_Zigzag_Level_Order_Traversal.py
'''
#Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

''' For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
 '''
class Node: 
    # Constructor to create a new node 
    def __init__(self, data): 
        self.val = data 
        self.left = self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        ans = {}
        queue = [(root, 0)]
        while(queue):
            root, level = queue.pop(0)
            if root:
                if level not in ans:
                    ans[level] = [root.val]
                else:
                    if level&1:
                        ans[level] = [root.val] + ans[level]
                    else:
                        ans[level] += [root.val]
                queue.append((root.left, level+1))
                queue.append((root.right, level+1))
        return ans.values()
if __name__ == '__main__':
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(7) 
    root.left.right = Node(6) 
    root.right.left = Node(5) 
    root.right.right = Node(4) 
    print(Solution().zigzagLevelOrder(root))