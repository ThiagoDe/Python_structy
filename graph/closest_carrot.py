from collections import deque

grid = [
    ['O', 'O', 'O', 'O', 'O'],
    ['O', 'X', 'O', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['O', 'X', 'C', 'O', 'O'],
    ['O', 'X', 'X', 'O', 'O'],
    ['C', 'O', 'O', 'O', 'O'],
]

def closest_carrot(grid, starting_row, starting_col):
    visited = set([ (starting_row, starting_col) ])
    queue = deque([ (starting_row, starting_col, 0)])
    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == 'C': return distance 
        
        deltas = [ (1, 0), (-1, 0), (0, 1), (0, -1)]
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col 
            row_inbounds = 0 <= neighbor_row < len(grid)
            col_inbounds = 0 <= neighbor_col < len(grid[0])
            pos = (neighbor_row, neighbor_col)
            if row_inbounds and col_inbounds and grid[neighbor_row][neighbor_col] != 'X' and pos not in visited:
                visited.add(pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))


    return - 1


print(closest_carrot(grid, 1, 2))  # -> 4
