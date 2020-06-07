# Given the robot's current location and the configuration of dirty and clean cells 
# in the matrix, print the next operation MegaMaid will perform 

# Link: https://www.hackerrank.com/challenges/botcleanlarge

import math
def position(posr,posc,dirt):
    distance = []
    for i in range(len(dirt)):
        # Manhattan distance
        result = abs(dirt[i][0] - posr) + abs(dirt[i][1] - posc) 
        # Euclidean distance
        #result = math.sqrt(((dirt[i][0] - posr) ** 2) + ((dirt[i][1] - posc) ** 2))
        distance.append(result)
    return [x for (y,x) in sorted(zip(distance,dirt))]
    
def next_move(posr, posc, dimx, dimy, board):
    dirt = []
    for i in range(dimx):
        for j in range(dimy):
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
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)