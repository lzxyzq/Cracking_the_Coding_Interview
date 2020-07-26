'''
@Author: your name
@Date: 2020-05-28 15:01:09
@LastEditTime: 2020-05-31 16:20:23
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /Cracking_the_Code_Interview/Leetcode/Binary_Tree/Traversal/117.Populating_Next_Right_Pointers_in_Each_Node_II.py
'''

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

class Solution:
    def connect(self, root):
        if not root: return root
        queue = [root]
        while queue:
            length = len(queue)
            for i in range(length):
                cur_node = queue.pop(0)
                if i == length - 1:
                    cur_node.next = None
                else:
                    cur_node.next = queue[0]
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
        return root