graph = {
    'a': ['c', 'b'],
    'b': ['c'],
    'c': [],
    'q': ['r'],
    'r': ['s', 'u', 't'],
    's': ['t'],
    't': ['u'],
    'u': []
}
def longest_path(graph):
    distances = {}
    for node in graph:
        if graph[node] == []: distances[node] = 0

    for node in graph:
        traverse_distance(graph, node, distances)

    return max(distances.values())

    
def traverse_distance(graph, node, distances):
    if node in distances: return distances[node]
    largest = 0
    for neighbor in graph[node]:
        attempt = traverse_distance(graph, neighbor, distances)
        largest = max(attempt, largest)

    distances[node] = 1 + largest
    return distances[node]

print(longest_path(graph))  # -> 4
