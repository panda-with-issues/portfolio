"""
Graph search algorithms in Python3
"""
# For the sake of this exrcise, graphs will be represented as adjacency lists into a dictionary

"""
DFS: Depth first search
"""
# This algorithm finds a path between two vertices following a straigth path. If at the end of the path the target isn't found, it comes back to the latest cross-road and follows another path up until the end.
# DFS will be implemented recursively.
# DFS has a runtime of O(V + E), V = vertices E = edges of the graph. It is very efficient when we want to check if a path exists between two vertices.

def dfs(graph, current_vertex, target, visited=None, path=None):
    
    if not visited:
        visited = []

    if not path:
        path = []

    path.append(current_vertex)

    #base case
    if current_vertex == target:
        return path

    #inductive step
    visited.append(current_vertex)
    
    #recursive step
    for adjacent in graph[current_vertex]:
        if adjacent not in visited:
            possible_path = dfs(graph, adjacent, target, visited, path)
            if possible_path:
                return possible_path
            else:
                path.remove(adjacent)

"""
BFS: Breadth first search
"""
# BFS proceeds breadthwise in order to find a path between an origin vertex and a target. At every step, it checks every adjacent vertex to the current one and returns when
# the target is found or every vertex in the graph has been visited.
# BFS will be implemented using a queue data structure.
# BFS has a runtime of O(V + E) (see DFS runtime) and is very efficient when we want to find the shortest path between two vertices

def bfs(graph, origin, target):

    path = [origin]
    vertex_and_path = [origin, path]
    q = [vertex_and_path]
    visited = []
    while q:
        current_vertex, path = q.pop(0)
        visited.append(current_vertex)
        for adjacent in graph[current_vertex]:
            if adjacent not in visited:
                if adjacent == target:
                    return path + [adjacent]
                if adjacent not in [vertex_and_path[0] for vertex_and_path in q]:
                    q.append([adjacent, path + [adjacent]])
                
    
"""
DEBUG
"""

graph = {
    'A': ['B', 'C', 'I'],
    'B': ['C'],
    'C': ['A', 'B', 'D', 'F', 'L'],
    'D': ['C', 'I'],
    'E': ['L'],
    'F': ['C', 'L'],
    'G': ['H', 'M'],
    'H': ['G', 'M', 'N'],
    'I': ['A', 'D'],
    'L': ['C', 'F', 'E'],
    'M': ['G', 'H'],
    'N': ['H']
}

print(bfs(graph, 'A', 'L'))
print(bfs(graph, 'E', 'I'))
print(bfs(graph, 'G', 'N'))
print(bfs(graph, 'B', 'D'))
print(bfs(graph, 'E', 'D'))
print(bfs(graph, 'N', 'D'))




