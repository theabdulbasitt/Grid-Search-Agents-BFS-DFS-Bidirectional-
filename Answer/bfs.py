import random
from collections import deque
from grid_file import grid
 
def bffs(x, row, coloumn):

    # x[0][0] = 'v'
    visited = []
    qu = deque()
    if x[0][0] == 0:
        qu.append( (0,0))
    else:
        return "No starting point"

    while qu:
        
        i,j = qu[0]
        if i == ( row - 1 ) and j == (coloumn -1):
            visited.append((i,j))
            print("Reached goal state!") 
            break
        if (i,j) not in visited:  
            visited.append((i,j))
        #qu.append((i,j))
        if j < coloumn - 1:  
            if grid[i][j+1] == 0:
                qu.append((i,j+1))
        if i < row - 1:    
            if grid[i+1][j] == 0:
                qu.append((i+1,j))
                 
        qu.popleft()
        
    print("")
    print(visited)
 




# ----------------------------------------------------------------------------------------------------------------------


n = len(grid)
m = len(grid[0])



for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()


print("Calling function")
x = bffs(grid, n, m)
