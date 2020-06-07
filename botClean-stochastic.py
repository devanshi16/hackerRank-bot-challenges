# The game Bot Clean took place in a deterministic environment. In this 
# version, the bot is given 200 moves to clean as many dirty cells as possible. 
# The grid initially has 1 dirty cell. When the bot cleans this cell, a new 
# cell in the grid is made dirty. The new cell can be anywhere in the grid.

# The bot here is positioned at the top left corner of a 5*5 grid. Your task 
# is to move the bot to appropriate dirty cell and clean it.

# Link: https://www.hackerrank.com/challenges/botcleanr

def next_move(posr, posc, board):
    dirt_r = dirt_c = 0
    for i in range(5):
        for j in range(5):
            if board[i][j]=='d':
                dirt_r,dirt_c = i, j
    
    if dirt_c < posc:
        print('LEFT')
    elif dirt_c  > posc:
        print('RIGHT')
    elif dirt_r < posr:
        print('UP')
    elif dirt_r > posr:
        print('DOWN')
    else:
        print('CLEAN')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)