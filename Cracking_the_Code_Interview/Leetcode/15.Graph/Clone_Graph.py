
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node):
        if not node:
            return 
        return self.dfs(node,{})  # key: Node.val  Value:Node
    def dfs(self,node,dic):
        if node.val in dic:
            return dic[node.val]
        Copy_Node = Node(node.val)
        dic[node.val] = Copy_Node
        for neighbor in node.neighbors:
            Copy_Node.neighbors.append(self.dfs(neighbor,dic))
        return Copy_Node

    
