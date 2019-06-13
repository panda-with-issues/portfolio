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
Dijkstra's algorithm
"""
# Unlike the BFS, Dijkstra's algorithm find the most economic path between two vertices. To find this path Dijkstra uses an hash map, in which each vertex is mapped with its distance from origin,
# and a min heap, used to update the hash map.
# Dijkstra's runtime is O((V + E)logV).

# with this module we can assign an infinity represantation when initializing the hash map
from math import inf

# this library can be found in this very repository
from heaps_implementation import MinHeap

def dijkstra(graph, origin, target):

    # set up
    map = {vertex: inf for vertex in graph}
    map[origin] = 0
    heap = MinHeap()
    heap.add((map[origin], origin))
    path = [origin]
    paths = {origin: path}
    visited = []

    # search routine: graph must be traversed entirely in order to avoid bugs with adjacent vertices (in the given debug graph, A and C will bug the program returning
    # [A, C] instead of [A, I, D, C])
    while len(heap.dataset) > 1:
        current_distance, current_vertex = heap.retrieve()
        visited.append(current_vertex)
        for adjacent, weight in graph[current_vertex]:
            if adjacent not in visited:
                distance = current_distance + weight
                if distance < map[adjacent]:
                    map[adjacent] = distance
                    heap.add((distance, adjacent))
                    paths[adjacent] = paths[current_vertex] + [adjacent]
    
    # path restitution
    return paths.get(target)
    


"""
DEBUG
"""

graph = {
    'A': ['B', 'C', 'I'],
    'B': ['A', 'C'],
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

dijkstra_graph = {
    'A': [('B', 7), ('C', 10), ('I', 1)],
    'B': [('A', 7), ('C', 9)],
    'C': [('A', 10), ('B', 9), ('D', 3), ('F', 3), ('L', 1)],
    'D': [('C', 3), ('I', 2)],
    'E': [('L', 8)],
    'F': [('C', 3), ('L', 1)],
    'G': [('H', 9), ('M', 4)],
    'H': [('G', 9), ('M', 2), ('N', 7)],
    'I': [('A', 1), ('D', 2)],
    'L': [('C', 1), ('F', 1), ('E', 8)],
    'M': [('G', 4), ('H', 2)],
    'N': [('H', 7)]
}

print(dijkstra(dijkstra_graph, 'A', 'E'))
print(dijkstra(dijkstra_graph, 'G', 'N'))
print(dijkstra(dijkstra_graph, 'B', 'D'))
print(dijkstra(dijkstra_graph, 'A', 'C'))
print(dijkstra(dijkstra_graph, 'F', 'C'))
print(dijkstra(dijkstra_graph, 'F', 'A'))
print(dijkstra(dijkstra_graph, 'A', 'H'))
print(dijkstra(dijkstra_graph, 'B', 'C'))
print(dijkstra(dijkstra_graph, 'B', 'F'))
print(dijkstra(dijkstra_graph, 'B', 'E'))
