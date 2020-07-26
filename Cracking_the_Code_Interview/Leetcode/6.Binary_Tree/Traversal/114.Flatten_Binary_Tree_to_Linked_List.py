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
# Method 1 
# Space:O(n) 
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        self.preOrder(root, res)
        for i in range(len(res) - 1):
            res[i].left = None
            res[i].right = res[i + 1]
    
    def preOrder(self, root, res):
        if not root: return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)


# Method 2 
# in-place
# 把左右子树分别flatten形成两个链表，然后把根节点的左孩子放到根节点的右孩子上。把原先的根节点的右孩子拼到当前根节点链表的结尾。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        left = root.left
        right = root.right
        root.left = None

        self.flatten(left)
        self.flatten(right)

        root.right = left
        while root.right:
            root = root.right
        root.right = right

# Method 3 
# 从后往前写

def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    
    def flat(node):
        if not node:
            return None
        flat(node.right)
        flat(node.left)
        
        # In-place conversion
        
        node.right = self.prev
        node.left = None
        self.prev = node
        
    self.prev=None
    flat(root)

if __name__ == '__main__':
    flatten()
    