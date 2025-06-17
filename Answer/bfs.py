import random
from collections import deque
 
def bffs(x, size):

    # x[0][0] = 'v'
    visited = []
    qu = deque()
    if x[0][0] == 0:
        qu.append( (0,0))
    else:
        return "No starting point"

    while qu:
        
        i,j = qu[0]
        if i == ( size - 1 ) and j == (size -1):
            print("Reached goal state!") 
        if (i,j) not in visited:  
            visited.append((i,j))
        #qu.append((i,j))
        if j != size - 1:  
            if grid[i][j+1] == 0:
                qu.append((i,j+1))
        if i != size-1:    
            if grid[i+1][j] == 0:
                qu.append((i+1,j))
                 
        qu.popleft()
        
    print("")
    print(visited)
    print(qu)




# ----------------------------------------------------------------------------------------------------------------------
n=5
grid = []
for i in range(n):
    row = []
    for j in range(n):
        if i==0 and j==0:
            row.append(0) 
        elif (i==4 and j == 4):
            row.append(0)
        elif ( i==1 and j ==0 ) and grid[0][1] == 1:
            row.append(0)
        elif (i == 4 and j ==3) and grid[3][4] == 1:
            row.append(0)
        else:
            row.append(random.randint(0,1)) 
    grid.append(row)


for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()


print("Calling function")
x = bffs(grid, n)
