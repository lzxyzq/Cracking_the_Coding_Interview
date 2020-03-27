# Given a directed graph, design an algrithm to find out whether there is a route between two nodes.

from collections import defaultdict 
class Graph: 

    def __init__(self,vertices): 
        self.V= vertices #No. of vertices 
        self.graph = defaultdict(list) # default dictionary to store graph 
    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    # Use BFS to check path between s and d 
    def isReachable(self, s, d): 
        # Mark all the vertices as not visited
        visited = [False]*(self.V)
        #Create a queue for BFS
        queue = []
        #Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            n = queue.pop(0)
            if n == d:
                return True 
            
            for i in self.graph[n]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return False

if __name__ == '__main__':
    g = Graph(4) 
    g.addEdge(0,1) 
    g.addEdge(0,2) 
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)
    print(g.graph)
    u = 1 
    v = 3 
    if g.isReachable(u,v):
        print("There is a path from %d to %d" % (u,v))
    else:
        print("There is no path from %d to %d" % (u,v))