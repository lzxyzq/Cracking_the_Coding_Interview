
# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
# Return all critical connections in the network in any order.


# https://www.youtube.com/watch?v=aZXi1unBdJA

from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        bridge = []
        lowest = {}
        visited = set()
        discovered = defaultdict(int)
        
        def dfs(vertex,parent,time):
            visited.add(vertex)
            discovered[vertex] = time
            lowest[vertex] =time
            for child in graph[vertex]:
                if child == parent:
                    continue
                if child not in visited:
                    dfs(child,vertex,time+1)
                    lowest[vertex] = min(lowest[vertex], lowest[child])
                    if discovered[vertex] < lowest[child]: 
                        bridge.append([vertex,child])
                else:
                    lowest[vertex] = min(lowest[vertex],discovered[child])
                    
        for i in range(n):
            if i not in visited:
                dfs(i,None,0)
        return bridge
            