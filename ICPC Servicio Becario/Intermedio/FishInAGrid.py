def fishGrid(grid):
    rows = len(grid)
    cols = len(grid[0])


    def dfs(r,c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
            return 0
        
        #Sum the number of goldfish found
        fish = grid[r][c]
        
        #Change the element we are just at into a 0
        grid[r][c] = 0

        #Search in adjacent elements
        fish += dfs(r+1,c)
        fish += dfs(r-1,c)
        fish += dfs(r,c+1)
        fish += dfs(r,c-1)

        return fish

    max_fish = 0

    #Start the double for loop to check all elements
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                current = dfs(r,c)

                max_fish = max(max_fish, current)

    return(max_fish)

        
