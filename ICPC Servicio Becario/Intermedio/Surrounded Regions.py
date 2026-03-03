board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

rows = len(board)
cols = len(board[0])

def dfs(r,c):
    #Checking for limit elements
    if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
        return 
    #Converting the 0 into an X
    board[r][c] = "T"
    dfs(r, c+1)
    dfs(r, c-1)
    dfs(r+1, c)
    dfs(r-1, c)

for r in range(rows):
    for c in range(cols):
        is_limit = (r == 0 or r == rows-1 or c == 0 or c == cols-1)
        if is_limit and board[r][c] == "O":
            dfs(r,c)

#Second sweep to change from T to X
for r in range(rows):
    for c in range(cols):
        if board[r][c] == "O": #The ones who were surrounded
            board[r][c] = "X"
        elif board[r][c] == "T": #The ones who were in the border
            board[r][c] = "O"


print(board)