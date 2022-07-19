num_courses = 7
prereqs = [
    (4, 3),
    (3, 2),
    (2, 1),
    (1, 0),
    (5, 2),
    (5, 6),
]

def semesters_required(num_courses, prereqs):
    graph = build_graph(prereqs, num_courses)
    semesters = {}
    for course in graph:
        if graph[course] == []: semesters[course] = 1

    for course in graph:
        traverse(graph, course, semesters)

    return max(semesters.values())

def traverse(graph, course, semesters):
    if course in semesters: return semesters[course]
    count = 0
    for neighbor in graph[course]:
        attempt = traverse(graph, neighbor, semesters)
        count = max(attempt, count)

    semesters[course] = 1 + count 
    return semesters[course]

def build_graph(prereqs, num_courses):
    graph = {}

    for num in range(num_courses):
        graph[num] = []
    
    for courses in prereqs:
        a, b = courses 
        graph[a].append(b)

    return graph
print(semesters_required(num_courses, prereqs))  # -> 5
