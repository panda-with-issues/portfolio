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

print(dfs(graph, 'I', 'F'))
print(dfs(graph, 'A', 'E'))
print(dfs(graph, 'I', 'G'))
print(dfs(graph, 'C', 'E'))
print(dfs(graph, 'B', 'D'))
print(dfs(graph, 'N', 'G'))
print(dfs(graph, 'B', 'H'))
print(dfs(graph, 'E', 'A'))
print(dfs(graph, 'E', 'H'))
print(dfs(graph, 'C', 'F'))
print(dfs(graph, 'L', 'A'))
print(dfs(graph, 'B', 'N'))