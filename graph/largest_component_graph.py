def largest_component(graph):
    visited = set()
    largest = 0

    for node in graph:
        count = explorer(graph, node, visited)
        largest = max(largest, count)

    return largest

def explorer(graph, node, visited):
    if node in visited: return 0
    visited.add(node)
    count = 0
    for neighbor in graph[node]:
        count += explorer(graph, neighbor, visited)

    return count + 1

print(largest_component({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))  # -> 4
