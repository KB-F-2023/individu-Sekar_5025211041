import heapq

def a_star(graph, start, goal, sld):
    queue = [(0, start)]
    visited = set()

    while queue:
        (cost, current_node) = heapq.heappop(queue)
        if current_node == goal:
            return cost
        if current_node not in visited:
            visited.add(current_node)
            for nbor, distance in graph[current_node].items():
                if nbor not in visited:
                    heuristic_cost = sld[nbor]
                    heapq.heappush(queue,(cost + distance + heuristic_cost, nbor))

    return float('inf')

graph = {
    'A': {'E': 6},
    'B': {'E': 6, 'D': 7},
    'C': {'D': 6},
    'D': {'F': 6},
    'E': {'F': 4},
    'F': {'G': 3},
    'G': {0}
}

sld = {
    'A': 20,
    'B': 19,
    'C': 16,
    'D': 12,
    'E': 0,
    'F': 13,
    'G': 11,
    'H': 15,
    'I': 10,
}

start = 'A'
goal = 'F'
shortest_route = a_star(graph, start, goal, sld)
print (graph)
print(shortest_route)