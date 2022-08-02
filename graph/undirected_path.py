from platform import node

edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]
def undirected_path(edges, node_A, node_B):
    graph = graph_builder(edges)
    return has_path(graph, node_A, node_B, set())

def has_path(graph, node_A, node_B, visited):
    if node_A == node_B: return True
    if node_A in visited:
        return False 
    visited.add(node_A)
    for neighbor in graph[node_A]:
        if has_path(graph, neighbor, node_B, visited): return True

    return False

def graph_builder(edges):
    graph = {}
    for nodes in edges:
        a, b = nodes
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

print(undirected_path(edges, 'j', 'm'))  # -> True
