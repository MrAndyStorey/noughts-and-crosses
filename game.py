#!/usr/bin/env python3
import time

def displayBoard(passedBoard):
    strBoard="""
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 ]
-------------
| 7 | 8 | 9 |
-------------
"""
    for counter in range(1,10):
        #Iterate through all board positions, seeing if each position has been taken
        if (passedBoard[counter] == 'O' or passedBoard[counter] == 'X'):
            #Taken position - Output the correct player's marker
            strBoard = strBoard.replace(str(counter), passedBoard[counter])
        else:
            #Available position - remove the number placeholder with a space
            strBoard = strBoard.replace(str(counter), ' ')
    print(strBoard)

def checkPosition(passedBoard, passedPosition):
    # Returns either True or False if the position is taken
    return passedBoard[passedPosition] == '#'

def checkFullBoard(passedBoard):
    #Iterate through the passedBoard to see if the board is full
    #****This need simplfying better for the pupils****
    return len([x for x in passedBoard if x == '#']) == 1

    
    if __name__ == '__main__':
      print('Welcome to Noughts & Crosses!')

      # Initialise an empty board - we ignore item 0 throughout
      board = ['#'] * 10
      
      displayBoard(board)
      
