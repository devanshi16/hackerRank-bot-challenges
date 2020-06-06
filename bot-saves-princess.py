def nextMove(m,grid):
    p=[0,0]
    m=[s//2,s//2]
    for i in range(s):
        for j in range(s):
            if grid[i][j]=='p':
                p = i ,j
    row_diff, col_diff = p[0] - m[0], p[1] - m[1] 
    print('UP' * -row_diff if row_diff < 0 else 'DOWN' * row_diff)
    print('LEFT' * -col_diff if col_diff < 0 else 'RIGHT' * col_diff)
    return ""
                
s = int(input())
grid = []
for i in range(0, s):
    grid.append(input().strip())

print(nextMove(s,grid))