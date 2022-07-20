numCourses = 6
prereqs = [
    (0, 1),
    (2, 3),
    (0, 2),
    (1, 3),
    (4, 5),
]

def prereqs_possible(numCourses, prereqs):
    graph = build_graph(numCourses, prereqs)
    visiting = set()
    visited = set()
    for node in graph:
        if cycle_detect(graph, node, visiting, visited):
            return False 

    return True

def cycle_detect(graph, node, visiting, visited):
    if node in visiting: return True 
    if node in visited: return False
    
    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    return False 

def build_graph(numCourses, prereqs):
    graph = {}
    for n in range(numCourses):
        graph[n] = []
    
    for pre in prereqs:
        a, b = pre 
        graph[a].append(b)

    return graph


print(prereqs_possible(numCourses, prereqs))  # -> True
