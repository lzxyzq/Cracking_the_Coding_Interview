# You are given an undirected connected graph. An articulation point (or cut vertex) is defined as a vertex which, when removed along with associated edges, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). The task is to find all articulation points in the given graph.

''' 
Input:
The input to the function/method consists of three arguments:

numNodes, an integer representing the number of nodes in the graph.
numEdges, an integer representing the number of edges in the graph.
edges, the list of pair of integers - A, B representing an edge between the nodes A and B.

Output:
Return a list of integers representing the critical nodes.
'''

''' Example:
Input: numNodes = 7, numEdges = 7, edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
Output: [2, 3, 5] 
'''
# https://www.youtube.com/watch?v=aZXi1unBdJA

from collections import defaultdict
def get_critical_nodes(num_nodes, num_edges, edges):
    # Build the graph first 
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    # Required for book keeping 
    # Regular DFS visited set   
    visited = set()
    # Lowest link needed to find backedges
    low = {}
    discovered = defaultdict(int)
    # Edges that will break the connected components
    bridges = []

    def dfs(vertex, parent, time):
        visited.add(vertex)
        low[vertex] = time
        discovered[vertex] = time
        for child in graph[vertex]:
            if child == parent:
                continue
            if child not in visited:
                dfs(child, vertex, time+1)
                # Update the lowest link value
                # The lowest link of a node, is either its own value or the lowest link of all its neighbors
                # that are not the parent node
                low[vertex] = min(low[vertex], low[child])
                if discovered[vertex] < low[child]: 
                    bridges.append(vertex)
            else:
                low[vertex] = min(low[vertex], discovered[child])


    # Run DFS on the nodes at the top level
    for i in range(num_nodes):
        if i not in visited:
            dfs(i, None, 0)

    return bridges


num_nodes = 7
num_edges = 7
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

if __name__ == '__main__':
    print(get_critical_nodes(num_nodes, num_edges, edges))
    