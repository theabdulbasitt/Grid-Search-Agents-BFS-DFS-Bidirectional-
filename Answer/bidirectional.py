import random

def bidirectional(grid, size):
    visited_S = []
    visited_E = []
    stack_S = []
    stack_E = []
    

    if grid[0][0] == 0:
        stack_S.append((0, 0))
        visited_S.append((0,0))
    else:
        return "No starting point"
    
    if grid[size-1][size-1] == 0:
        stack_E.append((size-1, size-1))
        visited_E.append((size-1,size-1))
    else:
        return "No goal point"


    goal = 0
    while stack_S or stack_E:

        if stack_S:
            i, j = stack_S[-1]
            if  j < (size-1) and grid[i][j+1] == 0 and (i,j+1) not in visited_S:
                    stack_S.append((i,j+1))
                    visited_S.append((i,j+1))
            elif i < (size-1) and grid[i+1][j] == 0 and (i+1,j) not in visited_S:
                    stack_S.append((i+1,j))
                    visited_S.append((i+1,j))
            else:
                i,j = stack_S.pop()

        if stack_E:
            a, b = stack_E[-1]
            if  b > 0 and grid[a][b-1] == 0 and (a,b-1) not in visited_E:
                    stack_E.append((a,b-1))
                    visited_E.append((a,b-1))
            elif a > 0 and grid[a-1][b] == 0 and (a-1,b) not in visited_E:
                    stack_E.append((a-1,b))
                    visited_E.append((a-1,b))
            else:
                a,b = stack_E.pop()


        if (i,j) in visited_E or (a,b) in visited_S :
            print("Solved")
            goal+=1
            break

    print("\nVisited Nodes (DFS Order):")
    print(f"From start : {visited_S}")
    print(f"From end : {visited_E}")

    merged = []
    for item in visited_S + visited_E[::-1]:
        if item not in merged:
            merged.append(item)
    
    print(merged)
    

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
x = bidirectional(grid, n)


