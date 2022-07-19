from collections import deque

grid = [
    ["W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["L", "L", "W", "W", "L"],
    ["W", "L", "W", "W", "L"],
    ["W", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "W"],
]
def best_bridge(grid):
    main_island = None 
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            potential_island = traverse(grid, r, c, set())
            if len(potential_island) > 0: 
                main_island = potential_island
                break

    visited = set(main_island)
    queue = deque([])
    for pos in main_island:
        r, c = pos 
        queue.append((r, c, 0))

    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'L' and (row, col) not in main_island:
            return distance - 1

        deltas = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col 
            pos = (neighbor_row, neighbor_col)
            if inbounds(grid, neighbor_row, neighbor_col) and pos not in visited:
                visited.add(pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))


def inbounds(grid, r, c):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])

    return row_inbound and col_inbound

def traverse(grid, r, c, visited):
    if not inbounds(grid, r, c) or grid[r][c] == 'W': return visited 
    pos = (r, c)
    if pos in visited: return visited 
    visited.add(pos)

    traverse(grid, r + 1, c, visited)
    traverse(grid, r - 1, c, visited)
    traverse(grid, r, c + 1, visited)
    traverse(grid, r, c - 1, visited)
    return visited 


print(best_bridge(grid))  # -> 2
