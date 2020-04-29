# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:10:13 2020

@author: Nathan
"""

from py2048_classes import Board, Tile
from functools import reduce
import time
import math
import random

def main():
#    allmoves = ['UP','LEFT','DOWN','RIGHT']
    board = Board()
    board.add_random_tiles(2)
    print("main code")

    move_counter = 0
    move = None
    move_result = False
    
    
    overalltime=time.time()
    while True:
        print("Number of successful moves:{}, Last move attempted:{}:, Move status:{}".format(move_counter, move, move_result))
        print(board)
        #print(board.print_metrics())
        if board.possible_moves()==[]:
            if (board.get_max_tile()[0]<2048):
                print("You lost!")
            else:
                print("Congratulations - you won!")
            break
        begin = time.time()
###################################### Your code should be inserted below 
###################################### (feel free to define additional functions to determine the next move)
        
        move = expectimax(board, 5, True, None)[1]
        board.make_move(move)
        
######################################  Do not modify 4 lines below      
######################################
        print("Move time: ", time.time()-begin)
        board.add_random_tiles(1)
        move_counter = move_counter + 1
    print("Average time per move:", (time.time()-overalltime)/move_counter)
    
###############

def expectimax(board, depth, maxing, move):
    if depth == 0:
        return snake_strategy(board), move
    if maxing:
        score = (0, move)
        for c in board.possible_moves():
            temp = getBoardCopy(board)
            temp.make_move(c)
            val = expectimax(temp, depth-1, False, move)[0]
            if val >= score[0]:
                score = (val, c)
        return score
    if not maxing:
        score = 0
        tempGrid = getBoardCopy(board).export_state()
        temp = [[(x, y) for y, col in enumerate(row) if col == None] for x, row in enumerate(tempGrid)]
        rcList = reduce(lambda x,y: x+y, temp)
        for cell in rcList:
            temp = getBoardCopy(board).export_state()
            temp[cell[0]][cell[1]] = 1
            score += 0.8 * expectimax(Board(temp), depth - 1, True, move)[0]
            
            temp = getBoardCopy(board).export_state()
            temp[cell[0]][cell[1]] = 2
            score += 0.2 * expectimax(Board(temp), depth - 1, True, move)[0]
        return score/(len(rcList)), move

    
def snake_strategy(board):
    possGrids = [
        [
            [2 ** 15, 2 ** 14, 2 ** 13, 2 ** 12],
            [2 ** 8, 2 ** 9, 2 ** 10, 2 ** 11],
            [2 ** 7, 2 ** 6, 2 ** 5, 2 ** 4],
            [2 ** 0, 2 ** 1, 2 ** 2, 2 ** 3]
        ]
        ,
        [
           [2 ** 15, 2 ** 8, 2 ** 7, 2 ** 0],
           [2 ** 14, 2 ** 9, 2 ** 6, 2 ** 1],
           [2 ** 13, 2 ** 10, 2 ** 5, 2 ** 2],
           [2 ** 12, 2 ** 11, 2 ** 4, 2 ** 3]
        ]
        ,
        [
           [2 ** 12, 2 ** 13, 2 ** 14, 2 ** 15],
           [2 ** 11, 2 ** 10, 2 ** 9, 2 ** 8],
           [2 ** 4, 2 ** 5, 2 ** 6, 2 ** 7],
           [2 ** 3, 2 ** 2, 2 ** 1, 2 ** 0]
        ]
        ,
        [
           [2 ** 3, 2 ** 2, 2 ** 1, 2 ** 0],
           [2 ** 4, 2 ** 5, 2 ** 6, 2 ** 7],
           [2 ** 11, 2 ** 10, 2 ** 9, 2 ** 8],
           [2 ** 12, 2 ** 13, 2 ** 14, 2 ** 15]
        ]
        ,
        [
           [2 ** 0, 2 ** 1, 2 ** 2, 2 ** 3],
           [2 ** 7, 2 ** 6, 2 ** 5, 2 ** 4],
           [2 ** 8, 2 ** 9, 2 ** 10, 2 ** 11],
           [2 ** 15, 2 ** 14, 2 ** 13, 2 ** 12]
        ]
        ,
        [
           [2 ** 12, 2 ** 11, 2 ** 4, 2 ** 3],
           [2 ** 13, 2 ** 10, 2 ** 5, 2 ** 2],
           [2 ** 14, 2 ** 9, 2 ** 6, 2 ** 1],
           [2 ** 15, 2 ** 8, 2 ** 7, 2 ** 0]
        ]
        ,
        [
           [2 ** 3, 2 ** 4, 2 ** 11, 2 ** 12],
           [2 ** 2, 2 ** 5, 2 ** 10, 2 ** 13],
           [2 ** 1, 2 ** 6, 2 ** 9, 2 ** 14],
           [2 ** 0, 2 ** 7, 2 ** 8, 2 ** 15]
        ]
        ,
        [
           [2 ** 0, 2 ** 7, 2 ** 8, 2 ** 15],
           [2 ** 1, 2 ** 6, 2 ** 9, 2 ** 14],
           [2 ** 2, 2 ** 5, 2 ** 10, 2 ** 13],
           [2 ** 3, 2 ** 4, 2 ** 11, 2 ** 12]
        ]
    ]
    
    max_value = 0
    valDic = {
        "0" : 0,
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0,
        "5" : 0,
        "6" : 0,
        "7" : 0
    }

    for i in range(4):
        for j in range(4):
            if(board.grid[i][j] != None):
                boardVal = board.grid[i][j].get_tile_value()
                valDic["0"] += boardVal * possGrids[0][i][j]
                valDic["1"] += boardVal * possGrids[1][i][j]
                valDic["2"] += boardVal * possGrids[2][i][j]
                valDic["3"] += boardVal * possGrids[3][i][j]
                valDic["4"] += boardVal * possGrids[4][i][j]
                valDic["5"] += boardVal * possGrids[5][i][j]
                valDic["6"] += boardVal * possGrids[6][i][j]
                valDic["7"] += boardVal * possGrids[7][i][j]
                
    max_value = max(valDic.values())
    return max_value / 2**13


def getBoardCopy(board):
    copy = board.export_state()
    return Board(copy)       
        

if __name__ == "__main__":
    main()