def has_cycle(graph):
    visiting = set()
    visited = set()
    for node in graph:
        if cycle_detect(graph, node, visiting, visited):
            return True

    return False 

def cycle_detect(graph, node, visiting, visited):
    if node in visited: return False
    if node in visiting: return True 
    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited): 
            return True 

    visiting.remove(node)
    visited.add(node)
    return False


print(has_cycle({
    "a": ["b"],
    "b": ["c"],
    "c": ["a"],
}))  # -> True
