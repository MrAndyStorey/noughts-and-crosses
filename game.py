#!/usr/bin/env python3

# importing the required module(s)
import random

def displayBoard(passedBoard):
    strBoard="""
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
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

def placeMarker(passedBoard, passedPosition, passedMarker):
    passedBoard[passedPosition] = passedMarker
    return passedBoard

def checkPosition(passedBoard, passedPosition):
    # Returns either True or False if the position is taken
    return passedBoard[passedPosition] == '#'

def checkFullBoard(passedBoard):
    #Initialise local variable that we'll pass bnack as the return value
    blnReturn  = True

    #Iterate through the passedBoard to see if the board is full
    for position in range(1,10):
        if passedBoard[position] == '#':
            blnReturn  = False

            #If we've found a blank, there's no need to iterate through the remaining.
            break

    return blnReturn

def checkForAWinner(passedBoard, passedMarker):
    if passedBoard[1] == passedBoard[2] == passedBoard[3] == passedMarker:
        # Top Row Winner
        return True
    if passedBoard[4] == passedBoard[5] == passedBoard[6] == passedMarker:
        # Middle Row Winner
        return True
    if passedBoard[7] == passedBoard[8] == passedBoard[9] == passedMarker:
        # Bottom Row Winner
        return True
    if passedBoard[1] == passedBoard[4] == passedBoard[7] == passedMarker:
        # Left Column Winner
        return True
    if passedBoard[2] == passedBoard[5] == passedBoard[8] == passedMarker:
        # Center Column Winner
        return True
    if passedBoard[3] == passedBoard[6] == passedBoard[9] == passedMarker:
        # Right Column Winner
        return True
    if passedBoard[1] == passedBoard[5] == passedBoard[9] == passedMarker:
        # Left to Right Diagonal Winner
        return True
    if passedBoard[3] == passedBoard[5] == passedBoard[7] == passedMarker:
        # Right to Left Diagonal Winner
        return True
    return False

def getPlayerChoice(passedBoard):
    while True:
        choice = input("Please select an empty space between 1 & 9: ")
        # Check the user input to ensure they've only entered a number 1 to 9
        if choice not in {"1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            print('We expect you to enter a valid number.')
        else:
            # Check the user input to see if they have selected a free space
            if not checkPosition(passedBoard, int(choice)):
                print("Sorry, that space is taken.")
            else:
                break
    return int(choice)

def returnOnlyLegalMoves(passedBoard):
    localArray=[]

    for i in range(1,10):
        if checkPosition(passedBoard,i):
            localArray.append(i)

    return localArray
 
def randomNextMove(passedBoard):
    candidates = returnOnlyLegalMoves(passedBoard)
    return random.choice(candidates)
 
if __name__ == '__main__':
    print('Welcome to Noughts & Crosses!')

    #Setup local variables
    numberOfGames, countDraws, countWins0, countWinsX = 0,0,0,0
    playAgain = "y"

    #Add a loop for repeated game play
    while playAgain.lower() == "y":
        #numberOfGames is only used in the end of game stats.
        numberOfGames +=1

        # Initialise an empty board - we ignore item 0 throughout
        board = ['#'] * 10
        
        # Initialise the intTurns counter.  This is how we work out if it's player 1 or 2
        intTurns = 0

        # Display the initial blank board.
        displayBoard(board)

        #Iterate for the game, checking to see if the board is full
        while not checkFullBoard(board):

            # Who's turn is it? - P1 (User) or P2 (Computer)
            if intTurns % 2 == 0:

                # Player 1 (user) to choose where to put the mark
                marker = "O"
                position = getPlayerChoice(board)

                # Play the marker on the board
                placeMarker(board, position, marker)

            else:
                #Get the next move for Player 2 (computer)
                marker = "X"
                placeMarker(board,randomNextMove(board),marker)

            # Increment the intTurns counter
            intTurns +=1

            # Display the board
            displayBoard(board)

            # Check the status of the board game - do we have a winner?
            if checkForAWinner(board, marker):
                print(marker + "'s won!")
                if marker == "O":
                    countWins0 +=1
                else:
                    countWinsX +=1
                break
            elif checkFullBoard(board):
                #Check for a Draw
                countDraws += 1
                print("No winner - it's a draw!")
                
        #Ask the user if they wish to play again.   we check for y or Y in the condition of the while loop.
        playAgain = input("Do you want to play again (y / Y)?")

#Output the game stats to the user - the \n is a carriage return and % figures are rounded to 2 decimal places.
print("After {} game(s) we have:\nDraws: {}, {:.2%}\nPlayer 1 (User) wins: {}, {:.2%}\nPlayer 2 (Computer) wins: {}, {:.2%}".format(numberOfGames, countDraws, countDraws/numberOfGames,countWins0, countWins0/numberOfGames, countWinsX, countWinsX/numberOfGames))
