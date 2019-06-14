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

    # base case
    if current_vertex == target:
        return path, len(visited)

    # inductive step
    visited.append(current_vertex)
    
    # recursive step
    for adjacent in graph[current_vertex]:
        # using ignore as blind variable let the code run even with weighted graphs
        if type(adjacent) == tuple:
            adjacent, ignore = adjacent
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
    checked_count = 0
    while q:
        current_vertex, path = q.pop(0)
        visited.append(current_vertex)
        for adjacent in graph[current_vertex]:
            # this use of ignore is the same of dfs'
            if type(adjacent) == tuple:
                adjacent, ignore = adjacent
            if adjacent not in visited:
                checked_count += 1
                if adjacent == target:
                    return path + [adjacent], checked_count
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
    return paths.get(target), len(visited)
    


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

very_complicate_graph = {
    'A': [('B', 1), ('C', 3), ('D', 2), ('E', 2), ('F', 6)],
    'B': [('A', 1), ('C', 6), ('G', 8), ('H', 3)],
    'C': [('A', 3), ('B', 6), ('I', 5), ('J', 6), ('K', 7), ('L', 7)],
    'D': [('A', 2), ('L', 1)],
    'E': [('A', 2), ('M', 2), ('N', 4)],
    'F': [('A', 6), ('O', 10)],
    'G': [('B', 8), ('P', 2)],
    'H': [('B', 3), ('Q', 1), ('R', 4)],
    'I': [('C', 5), ('S', 3), ('T', 10), ('U', 8)],
    'J': [('C', 6), ('W', 1)],
    'K': [('C', 7), ('X', 8), ('Y', 3)],
    'L': [('C', 7), ('D', 1), ('Z', 6), ('AA', 8), ('AB', 7), ('AC', 9), ('AD', 1)],
    'M': [('E', 2), ('AD', 1), ('AE', 2), ('AF', 1)],
    'N': [('E', 4), ('AG', 1), ('AH', 6), ('AI', 8)],
    'O': [('F', 10), ('AJ', 6)],
    'P': [('G', 2)],
    'Q': [('H', 1)],
    'R': [('H', 4)],
    'S': [('I', 3)],
    'T': [('I', 10)],
    'U': [('I', 8)],
    'V': [('W', 3), ('X', 9)],
    'W': [('J', 1), ('V', 3)],
    'X': [('K', 8), ('V', 9)],
    'Y': [('K', 3)],
    'Z': [('L', 6)],
    'AA': [('L', 8)],
    'AB': [('L', 7)],
    'AC': [('L', 9)],
    'AD': [('L', 1), ('M', 1)],
    'AE': [('M', 2)],
    'AF': [('M', 1)],
    'AG': [('N', 1)],
    'AH': [('N', 6)],
    'AI': [('N', 8)],
    'AJ': [('O', 6)]
}

coordinates = {
    # mapped as (x, y)
    'A': (17, 14),
    'B': (17, 18),
    'C': (22, 16),
    'D': (20, 11),
    'E': (13, 11),
    'F': (13, 17),
    'G': (14, 22),
    'H': (20, 22),
    'I': (25, 20),
    'J': (26, 17),
    'K': (24, 14),
    'L': (22, 8),
    'M': (14, 7),
    'N': (9, 8),
    'O': (9, 18),
    'P': (12, 27),
    'Q': (18, 28),
    'R': (24, 25),
    'S': (26, 24),
    'T': (28, 22),
    'U': (29, 19),
    'V': (34, 13),
    'W': (30, 15),
    'X': (29, 12),
    'Y': (25, 9),
    'Z': (26, 5),
    'AA': (22, 4),
    'AB': (19, 4),
    'AC': (16, 3),
    'AD': (0, 16),
    'AE': (12, 2),
    'AF': (10, 4),
    'AG': (6, 4),
    'AH': (4, 9),
    'AI': (7, 12),
    'AJ': (4, 18)
}

print(dfs(graph, 'A', 'E'))
print(dfs(very_complicate_graph, 'A', 'AH'))
print(bfs(graph, 'A', 'E'))
print(bfs(very_complicate_graph, 'A', 'AH'))