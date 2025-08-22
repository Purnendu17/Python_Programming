def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    def dfs(r, c):
        # Boundary check and stop if we hit water ('0')
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        print(f"Visiting ({r}, {c})")  # Print the current cell being visited
        grid[r][c] = '0'  # Mark as visited

        # Visit all four adjacent cells
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':  # Found new island
                print(f"Starting new island search at ({r}, {c})")
                island_count += 1
                dfs(r, c)  # Explore the island

    return island_count

# Test input
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print("Number of islands:", numIslands(grid))
