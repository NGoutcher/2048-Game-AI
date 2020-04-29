"""
Python 2048 Game : Basic Console Based User Interface For Game Play

Originally written by Phil Rodgers, University of Strathclyde
"""

from py2048_classes import Board, Tile
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
       # print(board.print_metrics())
        if board.possible_moves()==[]:
            if (board.get_max_tile()[0]<2048):
                print("You lost!")
            else:
                print("Congratulations - you won!")
            break
        begin = time.time()
###################################### Your code should be inserted below 
###################################### (feel free to define additional functions to determine the next move)
        
        move = board.possible_moves()[random.randint(0,len(board.possible_moves())-1)]
        board.make_move(move)            
        
######################################  Do not modify 4 lines below      
######################################
        print("Move time: ", time.time()-begin)
        board.add_random_tiles(1)
        move_counter = move_counter + 1
    print("Average time per move:", (time.time()-overalltime)/move_counter)
        

if __name__ == "__main__":
    main()

  

