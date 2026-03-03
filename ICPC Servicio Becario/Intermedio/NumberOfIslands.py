def numIslands(grid):
    # Edge case: If the grid is completely empty, there are 0 islands.
    if not grid:
        return 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    # This is our helper function to explore and "sink" the island
    def dfs(r, c):
        # 1. BASE CASE: Stop exploring if we go out of bounds
        # OR if we hit water ('0'). 
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        
        # 2. MARK AS VISITED: Change the '1' to a '0' so we don't visit it again.
        grid[r][c] = '0'
        
        # 3. RECURSION: Explore all 4 adjacent directions
        dfs(r - 1, c) # Go Up
        dfs(r + 1, c) # Go Down
        dfs(r, c - 1) # Go Left
        dfs(r, c + 1) # Go Right

    # Start the double for-loop to scan every cell in the matrix
    for r in range(rows):
        for c in range(cols):
            # If we find land...
            if grid[r][c] == '1':
                islands += 1  # We found a new island!
                dfs(r, c)     # Trigger DFS to explore and sink this entire island

    return islands

# --- Example Usage ---
example_grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","1","1"]
]

print(f"Number of islands: {numIslands(example_grid)}") 
# Output should be 3