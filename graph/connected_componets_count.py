def connected_components_count(graph):
    visited = set()
    count = 0
    for node in graph:
        if traverse(graph, node, visited): count += 1

    return count 

def traverse(graph, node, visited):
    if node in visited: return False
    visited.add(node)
    for neighbor in graph[node]:
        traverse(graph, neighbor, visited)

    return True 
    
print(connected_components_count({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))  # -> 2

    