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
            adjacent = adjacent[0]
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
                adjacent = adjacent[0]
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
    # len(heap) must be > 1 beause of the flawed implementation of heap I wrote, that relies on having a sentinel None at index 0 in heap.dataset
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
A*
"""
# A* is an optimization of Dijkstra's algorithm. If the latter must traverse all the graph to return the most efficient path between two vertices, A* makes local
# optimal choice based on a heuristic, which is the estimated distance between the adjacent node which the algorith may traverse and the target vertex.
# The heuristic chosen is the Euclidean, because we suppose that we can move diagonally into a bidimensional space where the vertices lie upon.
# A* works best with widely branched graph which have small to none connection between each branch. If there are more connections, A* will chose the shortest path
# instead of the more efficient, if the difference between the estimated distances is significant.
# The runtime of A* is O(b**d), where b is the branching factor (the mean quantity of branch that departs from a vertex) and d is the target's depth from the origin
# vertex.

# This class allows to pin some elements at the heap's root so they can't be heapified down. This is needed in order to prevent a bug provoked by very close vertices.
# It tracks the minimum element of the heap
class ForcedHeap:

    def __init__(self, root=None):

        self.dataset = []
        if root:
            self.dataset = [root]
        self.root_pointer = 0 # this will keep track of forced root elements

    def push(self, element):

        self.dataset.append(element)
        self.heapify_up()

    def get_parent_index(self, child_index):

        retouched_child_index = child_index - self.root_pointer

        if retouched_child_index == 1 or retouched_child_index == 2:
            return 0 + self.root_pointer

        if retouched_child_index % 2 == 1:
            return retouched_child_index // 2 + self.root_pointer

        else:
            return (retouched_child_index - 1) // 2 + self.root_pointer

    def get_lesser_child_index(self, parent_index):

        if parent_index == 0:
            possible_left_child_index = 1
            possible_right_child_index = 2

        else:
            possible_left_child_index = parent_index * 2 + 1
            possible_right_child_index = possible_left_child_index + 1

        acceptable_threshold = len(self.dataset) - 1

        if possible_left_child_index <= acceptable_threshold:
            left_child = self.dataset[possible_left_child_index]
        else:
            return

        if possible_right_child_index <= acceptable_threshold:
            right_child = self.dataset[possible_right_child_index]
            if right_child < left_child:
                return possible_right_child_index
        
        return possible_left_child_index

 
    def heapify_up(self, child_index=None):

        if child_index is None:
            child_index = len(self.dataset) - 1

        # base case
        if child_index == self.root_pointer:
            return

        child = self.dataset[child_index]
        parent_index = self.get_parent_index(child_index)
        parent = self.dataset[parent_index]
        if child < parent:
            self.dataset[child_index], self.dataset[parent_index] = self.dataset[parent_index], self.dataset[child_index]
            self.heapify_up(parent_index)    

    # shift every element in list forward by one and make the last element be the first
    def shift(self, lst):

        pointer = 0
        for i in range(len(lst)):
            lst[pointer], lst[-1] = lst[-1], lst[pointer]
            pointer += 1
    
    # force the element added to be on top of the heap
    def force_push(self, element):

        self.dataset.append(element)
        self.shift(self.dataset)
        self.root_pointer += 1

    def pop(self):

        # if the element popped was one forced, pop it and update the pointer
        if self.root_pointer:
            self.root_pointer -= 1
            return self.dataset.pop(0)
        
        # if there aren't any forced element, act like a normal heap
        self.dataset[0], self.dataset[-1] = self.dataset[-1], self.dataset[0]
        element_to_return = self.dataset.pop()
        self.heapify_down()
        return element_to_return

    def heapify_down(self, parent_index=None):
        
        if parent_index is None:
            parent_index = 0

        child_index = self.get_lesser_child_index(parent_index)

        if child_index is None:
            return

        parent = self.dataset[parent_index]
        child = self.dataset[child_index]
        if child < parent:
            self.dataset[parent_index], self.dataset[child_index] = self.dataset[child_index], self.dataset[parent_index]
            self.heapify_down(child_index)

def heuristic(current_vertex, target, map):
    
    current_vertex_x, current_vertex_y = map[current_vertex]
    target_x, target_y = map[target]
    heuristic = ((current_vertex_x - target_x)**2 + (current_vertex_y - target_y)**2) ** (1/2)
    return heuristic

def a_star(graph, origin, target, map):

    # set up
    current_distances = {key: inf for key in graph}
    current_distances[origin] = 0
    heap = ForcedHeap((current_distances[origin], origin))
    paths = {origin: [origin]}
    visited = []
    
    # search routine
    while heap.dataset:
        current_distance, current_vertex = heap.pop()
        visited.append(current_vertex)
        if current_vertex == target:
            return paths[current_vertex], len(visited)
        for adjacent, weight in graph[current_vertex]:
            if adjacent not in visited:
                distance = current_distance + weight + heuristic(adjacent, target, map)
                if distance < current_distances[adjacent]:
                    current_distances[adjacent] = distance
                    heap.push((distance, adjacent))
                    paths[adjacent] = paths[current_vertex] + [adjacent]
        
        # if the estimated distances from target are almost the same, treat them as equidistant. This will prevent the algorithm to discard too easily paths that may
        # be better than the shortest. An example of this behaviour is given by the return path between 'A' and 'AD' in the very_complicate_graph. If you call the
        # function passing those vertices and without this patch, the returned value will be [A, E, M, D], which indeed is slightly shorter than the correct path
        # [A, D, L, AD], but on the other hand is slightly more expensive (5 against 4)
        for vertex in current_distances:
            if 0 < current_distances[vertex] - heap.dataset[0][0] < 2:
                try:
                    heap.dataset.remove((current_distances[vertex], vertex))
                    heap.heapify_up()
                except ValueError:
                    pass
                current_distances[vertex] = heap.dataset[0][0]
                heap.force_push((current_distances[vertex], vertex))
                
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
    'AD': (16, 0),
    'AE': (12, 2),
    'AF': (10, 4),
    'AG': (6, 4),
    'AH': (4, 9),
    'AI': (7, 12),
    'AJ': (4, 18)
}

print(dfs(very_complicate_graph, 'I', 'O'))