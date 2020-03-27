# Implement a function to check if a binary tree is a binary search tree.

class Node():
    def __init__(self, data, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def checkBST(binary_tree):
    return checkBST_Node(binary_tree,-float("inf"),float("inf"))

def checkBST_Node(node,left_bound,right_bound):
    if not node:
        return True
    return node.data >= left_bound and node.data <= right_bound and \
        checkBST_Node(node.left,left_bound,node.data) and checkBST_Node(node.right,node.data,right_bound)

def preOrder(node): 
    if not node: 
        return
    print(node.data)
    preOrder(node.left) 
    preOrder(node.right)

import unittest

class Test(unittest.TestCase):
  def test_validate_tree(self):
    self.assertEqual(checkBST(Node(3,Node(1),Node(8))), True)
    tree1 = Node(5,Node(3,Node(1),Node(4)),Node(7,Node(6),Node(8,None,Node(9))))
    self.assertEqual(checkBST(tree1), True)
    tree2 = Node(7,Node(3,Node(1),Node(8)),Node(9,Node(8),Node(11)))
    self.assertEqual(checkBST(tree2), False)

if __name__ == "__main__":
  unittest.main()