#In this version of "Bot saves princess", Princess Peach and bot's position are randomly set. 
# Can you save the princess?outputs the next move the bot makes to rescue the princess.
def nextMove(s,r,c,grid):
    p=[0,0]
    m=[r,c]
    for i in range(s):
        for j in range(s):
            if grid[i][j]=='p':
                p = i ,j
    row_diff, col_diff = p[0] - m[0], p[1] - m[1] 
    if(col_diff != 0):
        print('LEFT' if col_diff < 0 else 'RIGHT')
    elif(row_diff != 0):
        print('UP '  if row_diff < 0 else 'DOWN ')
    return ""
                
s = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, s):
    grid.append(input().strip())
print(nextMove(s,r,c,grid))