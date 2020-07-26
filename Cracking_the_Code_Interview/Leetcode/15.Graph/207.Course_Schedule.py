# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

""" 
Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible. 

"""

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) :
        
        # BFS 
        edges = [[] for i in range(numCourses)]
        inDegree = [0 for i in range(numCourses)]
        
        for edge in prerequisites:
            inDegree[edge[0]] += 1         # 计算入度
            edges[edge[1]].append(edge[0])     # 依赖此课程的课程
            
        q, count = deque(), 0
        
        for node in range(numCourses):
            if inDegree[node] == 0:       # 将入度为0的课程依次入队列
                q.append(node)
        
        while q:
            node = q.popleft()
            count += 1
            for neigh in edges[node]:
                inDegree[neigh] -= 1 
                if inDegree[neigh] == 0:
                    q.append(neigh)
                    
        return count == numCourses