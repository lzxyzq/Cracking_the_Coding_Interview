
# The first solution's idea is only on about the fact that root.right.next = root.next.left
class Solution:
    def connect(self, root) :
        if not root or not root.left:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
# The 2nd solution is as simple as stiching nodes recursively, 3 pairs at a time

class Solution:
    def connect(self, root) :
        if not root or not root.left:
            return root
        def stich(left, right):
            if not left:
                return
            if left.next:
                # optimize, save huge time
                return
            left.next = right
            stich(left.left, left.right)
            stich(left.right, right.left)
            stich(right.left, right.right)
        stich(root.left, root.right)
        return root