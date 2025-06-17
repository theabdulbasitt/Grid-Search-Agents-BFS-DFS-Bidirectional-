import random

def dfs(grid, size):
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

        if i == size - 1 and j == size - 1:
            print("Reached goal state!")
            goal+=1
            break  # Stop if goal is reached
        
        if  j < (size-1) and grid[i][j+1] == 0 and (i,j+1) not in visited:
                stack.append((i,j+1))
                visited.append((i,j+1))

        elif i < (size-1) and grid[i+1][j] == 0 and (i+1,j) not in visited:
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
x = dfs(grid, n)


