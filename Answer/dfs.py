import random

def dfs(grid, row, coloumn):
    visited = []
    stack = []
    
    if grid[0][0] == 0:
        stack.append((0, 0))
        visited.append((0,0))
    else:
        return "No starting point"

    goal = 0
    while stack:
        i, j = stack[-1]

        if i == row - 1 and j == coloumn - 1:
            print("Reached goal state!")
            goal+=1
            break  # Stop if goal is reached
        
        if  j < (coloumn-1) and grid[i][j+1] == 0 and (i,j+1) not in visited:
                stack.append((i,j+1))
                visited.append((i,j+1))

        elif i < (row-1) and grid[i+1][j] == 0 and (i+1,j) not in visited:
                stack.append((i+1,j))
                visited.append((i+1,j))
        else:
            i,j = stack.pop()


    print("\nVisited Nodes (DFS Order):")
    print(visited)
    if goal < 1:
        print("Not possibe to reach end point")
    return "Completed"


# ----------------------------------------------------------------------------------------------------------------------

grid = [    [0,	0, 0, 0, 0, 0, 0, 0, 0, 0],	
            [0,	0,	0,	1,	1,	0,	0,   0,	0,	0  ],  
            [0,	0,	0,	1,	1,	0,	0,   0,	1,	1],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	1,	1,	1,	1,	0,	0,	0,	0,	1], 
            [0,	0,	0,	0,	0,	0,	0,	0,	1,	0],
            [0,	0,	0,	0,	0,	1,	1,	0,	0,	0],
            [0,	0,	0,	0,	0,	1,	1,	0,	0,	0],	
            [0,	1,	1,	1,	0,	1,	1,	0,	0,	0],
            [0,	1,	1,	1,	0,	1,	1,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
            [0,	0,	0,	0,	0,	1,	1,	0,	0,	0],
            [0,	0,	0,	0,	0,	1,	1,	0,	0,	0]
]

n= 14
m=10

for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()


print("Calling function")
x = dfs(grid, n, m)


