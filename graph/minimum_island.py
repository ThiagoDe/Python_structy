grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]
def minimum_island(grid):
    visited = set()
    min_num = float('inf')
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            count = explore(grid, r, c, visited)
            if count > 0:
                min_num = min(count, min_num)

    return min_num

def explore(grid, r, c, visited):
    row_inbound = 0 <= r < len(grid)
    col_inbound = 0 <= c < len(grid[0])

    if not row_inbound or not col_inbound: return 0
    if grid[r][c] == 'W': return 0
    pos = (r, c)
    if pos in visited: return 0
    visited.add(pos)
    count = 1
    count += explore(grid, r + 1, c, visited)
    count += explore(grid, r - 1, c, visited)
    count += explore(grid, r, c + 1, visited)
    count += explore(grid, r, c - 1, visited)
    return count 

print(minimum_island(grid))  # -> 2
