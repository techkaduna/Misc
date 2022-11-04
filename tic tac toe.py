
# Print game board

def display_board(board):
   
    print(board[7]+ ' | ' + board[8] + ' | ' + board[9])
    print("_________")
    print(board[4]+ ' | ' + board[5] + ' | ' + board[6])
    print("_________")
    print(board[1]+ ' | ' + board[2] + ' | ' + board[3])
    print('\n'*100)


test_board = [" "]*10
#x = display_(test_board)
#print(x)

# function that takes player input and set value as x or o

def player_input():
    '''
    OUTPUT = PLAYER 1,PLAYER 2
    '''
    marker = ' '
    while not (marker == 'X' or marker == 'O'):
        marker = input("player1 choose 'x' or 'o' :  ").upper()

    if marker == "X":
        return ("x","O")

    else:
        return ("O","X")


player1_marker,player2_marker = player_input()

#print(player1_marker)

# Write a function that takes in a board list object,a marker and a position(correlating with 1 - 9)

def place_marker(board,marker,position):
    board[position] = marker

'''
place_marker(test_board, "$", 8)
p = display_board(test_board)
print(p)
'''

# Writing a function that checks board input and tells if any player has won

def win_check(board,mark):
    return ((board[1] == board[2] == board[3] == mark) or 
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    (board[1] == board[5] == board[9] == mark) or
    (board[3] == board[5] == board[7] == mark))

'''
display_board(test_board)
win_check(test_board, 'X')
p = win_check(test_board, 'X')
print(p)
'''

# Writing a function that uses the random module to decide which player goes first 
import random

def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "player1"
    else:
        return "player2"

#Writing a function that retuns a boolean if there's space on the board
def space_check(board,position):
    return board[position] == " "

#Writing a function that checks if the board is full
def full_board_check(board):
    for i in range(0,10):
        if space_check(board, i):
            return False

    #If board is full return full
    return True

#Writing a function that collects player's position input and use step 6 to check if the position is free
def player_choice(board):
    #default position == 0
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9,10] or not space_check(board,position):
        position = int(input('Choose your position (0-9): '))

    return position

#Write a function that asks player if the still want to play and returns a boolean if true
def replay():
    choice = input("Want to play again? Yes or No: ").upper()
    return choice == "YES"

#Using while loop and the functions invoked to run the game
#First while loop that keeps the gane running 
print("Welcome to TIC TAC TOE!")

while True:


    # game play


    ##set everything up(board,whos first and choose markers)
    the_board = [" "]*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first")

    play_game = input("Ready to play? y or n")
    if play_game == "y":
        game_on = True

    else:
        game_on = False

#the actual game play

    while game_on:
        if turn == "player1":
        #show the board
            display_board(the_board)
        #choose position
            position = player_choice(the_board)
        #place marker on position
            place_marker(the_board, player1_marker, position)
        #check if they won
            if win_check(the_board , player1_marker):
                display_board(the_board)
                print("Player1 has won")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("There is a TIE!")
                    game_on = False
                else:
                    turn = "Player 2"


        else:
        #show the board
            display_board(the_board)
        #choose position
            position = player_choice(the_board)
        #place marker on position
            place_marker(the_board, player2_marker, position)
        #check if they won
            if win_check(the_board , player2_marker):
                display_board(the_board)
                print("Player2 has won")
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("There is a TIE!")
                    game_on = False
                else:
                    turn = "Player1"


    #player onr turn
    if not replay():
        break
#break out of the while loop on replay()
