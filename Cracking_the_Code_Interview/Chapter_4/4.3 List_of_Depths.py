# Given a binary tree,design an algorithm which create a linked list of all the nodes at each depth(e.g.,if you have a tree with depth D,you'll D linked lists).

from collections import defaultdict 

class TreeNode:
    def __init__(self,data,left=None,right=None):
        self.data, self.left, self.right = data, left, right

def tree_to_linked_lists(root):
    result = []
    current = []
    if root != None :
        current.append(root)
    while len(current) > 0 :
        result.append(current)
        parent = current
        current = []
        for data in parent:
            if(data.left != None):
                current.append(data.left)
            if(data.right != None):
                current.append(data.right)
    return result 

def preOrder(node): 
    if not node: 
        return
    print(node.data)
    preOrder(node.left) 
    preOrder(node.right)

def output(result):
    temp = []
    for i in result:
        temp.append(i.data)
    return temp

if __name__ == '__main__':
    node_h = TreeNode('H')
    node_g = TreeNode('G')
    node_f = TreeNode('F')
    node_e = TreeNode('E', node_g)
    node_d = TreeNode('D', node_h)
    node_c = TreeNode('C', None, node_f)
    node_b = TreeNode('B', node_d, node_e)
    node_a = TreeNode('A', node_b, node_c)

    print(preOrder(node_a))
    result = tree_to_linked_lists(node_a)
    print(result[1])
    # print(output(result[3]))
    