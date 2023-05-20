from calendar import c
import re
from board import Board
import time
import random
import mini_max
import math

# GAME LINK
# http://kevinshannon.com/connect4/
EMPTY = 0
RED = 1
BLUE = 2

ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4


# def is_valid_cell(board , col):
#       return board[0][col] == 0

# def get_vaild_cols(board):
#      empty_cols = []
#      for col in range(COLUMN_COUNT):
#           if is_valid_cell(board, col):
#                empty_cols.append(col)
#      return empty_cols

# def get_Socre_(window , player):
#     score = 0
#     opp_player = RED
#     if player == RED:
#          opp_player = BLUE

#     if window.count(player) == 4: score += 100
#     elif window.count(player) == 3 and  window.count(EMPTY) == 1 : score += 5
#     elif window.coint(player) == 2 and window.count(EMPTY) == 2 : score +=2
#     if window.count(opp_player) == 3 and window.count(EMPTY) == 1: score -= 4
#     return score


# def score_(board, player):
# 	score = 0


# 	## Score center column
# 	center_array = [int(i) for i in (board[:, COLUMN_COUNT//2])]
# 	center_count = center_array.count(player )
# 	score += center_count * 3

# 	## Score Horizontal
# 	for r in range(ROW_COUNT):
# 		row_array = [int(i) for i in (board[r,:])]
# 		for c in range(COLUMN_COUNT-3):
# 			window = row_array[c:c+WINDOW_LENGTH]
# 			score += get_Socre_(window, player)

# 	## Score Vertical
# 	for c in range(COLUMN_COUNT):
# 		col_array = [int(i) for i in list(board[:,c])]
# 		for r in range(ROW_COUNT-3):
# 			window = col_array[r:r+WINDOW_LENGTH]
# 			score += get_Socre_(window, player)

# 	## Score posiive sloped diagonal
# 	for r in range(ROW_COUNT-3):
# 		for c in range(COLUMN_COUNT-3):
# 			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
# 			score += get_Socre_(window, player)

# 	for r in range(ROW_COUNT-3):
# 		for c in range(COLUMN_COUNT-3):
# 			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
# 			score += get_Socre_(window, player)

# 	return score


def count_streaks(board, player):
    rows, cols = len(board), len(board[0])
    count = 0

    # Check horizontal streaks
    for row in range(rows):
        for col in range(cols - 3):
            if board[row][col] == player and board[row][col + 1] == player and \
                    board[row][col + 2] == player and board[row][col + 3] == player:
                count += 1

    # Check vertical streaks
    for row in range(rows - 3):
        for col in range(cols):
            if board[row][col] == player and board[row + 1][col] == player and \
                    board[row + 2][col] == player and board[row + 3][col] == player:
                count += 1

    # Check diagonal (from top-left to bottom-right) streaks
    for row in range(rows - 3):
        for col in range(cols - 3):
            if board[row][col] == player and board[row + 1][col + 1] == player and \
                    board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                count += 1

    # Check diagonal (from top-right to bottom-left) streaks
    for row in range(rows - 3):
        for col in range(3, cols):
            if board[row][col] == player and board[row + 1][col - 1] == player and \
                    board[row + 2][col - 2] == player and board[row + 3][col - 3] == player:
                count += 1

    return count





def is_valid_cell(board , col):
      return board[0][col] == 0 # if the column has at least one empty cell 

def get_vaild_cols(board):
     empty_cols = []
     for col in range(COLUMN_COUNT):
          if is_valid_cell(board, col):
               empty_cols.append(col)
     return empty_cols


def winning_move(board, player):
	# Check horizontal locations for win
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT):
			if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
				return True

	# Check vertical locations for win
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT-3):
			if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
				return True

	# Check positively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(ROW_COUNT-3):
			if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
				return True

	# Check negatively sloped diaganols
	for c in range(COLUMN_COUNT-3):
		for r in range(3, ROW_COUNT):
			if board[r][c] == player and board[r-1][c+1] == player and board[r-2][c+2] == player and board[r-3][c+3] == player:
				return True



def is_terminal_(board):
      return winning_move(board , RED) or winning_move(board , BLUE)


def get_vaild_row(board , col):
      for r in range(5, -1, -1):
            if(board[r][col] == EMPTY):
                  return r



def get_opponent(player):
    if(player == RED):
        return BLUE
    else:
        return RED


def is_draw(board) :
    return (len(get_vaild_cols(board)) == 0)

def calculate_score(board, player):
    # Define the scoring values
    win_score = 1000
    lose_score = -1000

    # Check if the game is over (winning or draw)
    if winning_move(board, player):
        return win_score
    elif winning_move(board, get_opponent(player)):
        return lose_score
    elif is_draw(board):
        return 0

    # Calculate the score based on the current game state
    score = 0

    # Evaluate the board based on the number of consecutive pieces
    # for the current player and the opponent
    player_streaks = count_streaks(board, player)
    opponent_streaks = count_streaks(board, get_opponent(player))

    # Update the score based on the streaks
    score += player_streaks * 10
    score -= opponent_streaks * 10

    return score


def heuristic(state):
        heur = 0

        for i in range(0, ROW_COUNT):
            for j in range(0, COLUMN_COUNT):
                # check horizontal streaks
                try:
                    # add player one streak scores to heur
                    if state[i][j] == state[i + 1][j] == RED:
                        heur += 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == RED:
                        heur += 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == RED:
                        heur += 10000
 
                    # subtract player two streak score to heur
                    if state[i][j] == state[i + 1][j] == BLUE:
                        heur -= 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == BLUE:
                        heur -= 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == BLUE:
                        heur -= 10000
                except IndexError:
                    pass
 
                # check vertical streaks
                try:
                    # add player one vertical streaks to heur
                    if state[i][j] == state[i][j + 1] == RED:
                        heur += 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == RED:
                        heur += 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == RED:
                        heur += 10000
 
                    # subtract player two streaks from heur
                    if state[i][j] == state[i][j + 1] == BLUE:
                        heur -= 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == BLUE:
                        heur -= 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == BLUE:
                        heur -= 10000
                except IndexError:
                    pass
 
                # check positive diagonal streaks
                try:
                    # add player one streaks to heur
                    if not j + 3 > COLUMN_COUNT and state[i][j] == state[i + 1][j + 1] == RED:
                        heur += 100
                    if not j + 3 > COLUMN_COUNT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == RED:
                        heur += 100
                    if not j + 3 > COLUMN_COUNT and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] == state[i+3][j + 3] == RED:
                        heur += 10000
 
                    # add player two streaks to heur
                    if not j + 3 > COLUMN_COUNT and state[i][j] == state[i + 1][j + 1] == BLUE:
                        heur -= 100
                    if not j + 3 > COLUMN_COUNT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == BLUE:
                        heur -= 100
                    if not j + 3 > COLUMN_COUNT and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] == state[i+3][j + 3] == BLUE:
                        heur -= 10000
                except IndexError:
                    pass
 
                # check negative diagonal streaks
                try:
                    # add  player one streaks
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == RED:
                        heur += 10
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == RED:
                        heur += 100
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == state[i+3][j - 3] == RED:
                        heur += 10000
 
                    # subtract player two streaks
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == BLUE:
                        heur -= 10
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == BLUE:
                        heur -= 100
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == state[i+3][j - 3] == BLUE:
                        heur -= 10000
                except IndexError:
                    pass
        return heur







def mini_max_fun(board , depth , alpha , beta , current_player):
    vaild_cols = get_vaild_cols(board)


    

    game_end = is_terminal_(board)
    if depth == 0 or game_end:
        if(game_end):
            if(winning_move(board , RED)):
                return (None,math.inf)
            elif(winning_move(board , BLUE)):
                return(None,-math.inf)
            else: # draw 
                return(None,0)
        else : 
             return (None , heuristic(board)) 

    if current_player == RED:
        max_eval = -math.inf

        column = vaild_cols[0] # set the columns with value 

        for col in vaild_cols:
            row = get_vaild_row(board , col)
            new_board = []
            for i in range(len(board)):
                new_board.append(list(board[i]))
            new_board[row][col] = RED
            eval = mini_max_fun(new_board , depth-1 , alpha, beta,BLUE)[1]
            if(eval >= max_eval) :
                max_eval = eval
                column = col
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break
        return (column,max_eval)

        

    else:
        min_eval = math.inf
        column = vaild_cols[0]
        for col in vaild_cols:
            row = get_vaild_row(board , col)
            new_board = []
            for i in range(len(board)):
                new_board.append(list(board[i]))
            new_board[row][col] = BLUE
            eval = mini_max_fun(new_board, depth-1, alpha, beta, RED)[1]
            if(eval <= min_eval):
                min_eval = eval 
                column = col
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return (column,min_eval)


def main():
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:

# يارب
        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        print("____________--------___________________________ \n")

        # for i in range(6):
        #     for j in range(7):
        #         print(game_board[i][j])
        #     print("\n")

        # print("____________--------___________________________ \n")

        valid_cols = get_vaild_cols(game_board)

        print('_____valid ____')

        for i in range (len(valid_cols)):
            print(valid_cols[i])

        print("_____valid rows ______")

        for i in range (len(valid_cols)):
            row = get_vaild_row(game_board , i)
            print(row , " is a valid row ")




        

        # # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column



        (best_column,mx) = mini_max_fun(game_board ,4,-math.inf,math.inf,RED)

        # random_column = random.randint(0, 6)
        board.select_column(best_column)
        # if best_column is not None:
        #     board.select_column(best_column)
        # else :
        #     print("No valid column available. Game ended in a draw.")

        time.sleep(2)


if __name__ == "__main__":
    main()
