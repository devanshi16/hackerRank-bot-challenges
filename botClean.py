#The bot here is positioned at the top left corner of a 5*5 grid. 
# Your task is to move the bot to clean all the dirty cells. One move at a time.

# Link: https://www.hackerrank.com/challenges/botclean
import math

def position(posr,posc,dirt):
    distance = []
    for i in range(len(dirt)):
        # Manhattan distance
        result = abs(dirt[i][0] - posr) + abs(dirt[i][1] - posc) 
        # Euclidean distance
        #result = math.sqrt(((dirties[i][0] - posr) ** 2) + ((dirties[i][1] - posc) ** 2))
        distance.append(result)
    return [x for (y,x) in sorted(zip(distance,dirt))]


def next_move(posr, posc, board):
    dirt = []
    for i in range(5):
        for j in range(5):
            if board[i][j]=='d':
                dirt.append([i,j])
    
    nearest_dirt = position(posc,posc,dirt)
    if nearest_dirt[0][1] < posc:
        print('LEFT')
    elif nearest_dirt[0][1]  > posc:
        print('RIGHT')
    elif nearest_dirt[0][0] < posr:
        print('UP')
    elif nearest_dirt[0][0] > posr:
        print('DOWN')
    else:
        print('CLEAN')

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)