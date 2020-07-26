# Given a binary tree, find its maximum depth.The maximum depth is the number of nodes along the longest path from the root node down to thefarthest leaf node.

# Maximum Depth of Binary Tree
# Recursive 
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        else: return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

# Iteration
class Solution:
# Time complexityO(n)，Space complexityO(logn)
    def maxDepth(self,root):
        if root is None:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            for i in range(len(queue)):
                cur_root = queue.pop(0)
                if cur_root.left:
                    queue.append(cur_root.left)
                if cur_root.right:
                    queue.append(cur_root.right)
        return depth
