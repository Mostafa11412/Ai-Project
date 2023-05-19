from board import Board
import game
import math


EMPTY = 0
RED = 1
BLUE = 2

ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4


def get_Socre_(window , player):
    score = 0
    opp_player = RED
    if player == RED:
         opp_player = BLUE

    if window.count(player) == 4: score += 100
    elif window.count(player) == 3 and  window.count(EMPTY) == 1 : score += 5
    elif window.coint(player) == 2 and window.count(EMPTY) == 2 : score +=2
    if window.count(opp_player) == 3 and window.count(EMPTY) == 1: score -= 4
    return score


def score_(board, player):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
	center_count = center_array.count(player )
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_COUNT-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += get_Socre_(window, player)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_COUNT-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += get_Socre_(window, player)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += get_Socre_(window, player)

	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += get_Socre_(window, player)

	return score


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
      return winning_move(board , RED) or winning_move(board , BLUE) or len(get_vaild_cols(board))==0


def get_vaild_row(board , col):
      for r in range(ROW_COUNT):
            if(board[r][col] == EMPTY):
                  return r
    
      

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
             return (None , score_(board , BLUE)) 

    if current_player == RED:
        max_eval = -math.inf

        column = vaild_cols[0] # set the columns with value 

        for col in vaild_cols:
            row = get_vaild_row(board , col)
            new_board = board.copy()
            new_board[row][col] = RED
            eval = mini_max_fun(new_board , depth-1 , alpha, beta,BLUE)
            if(eval > max_eval) :
                max_eval = eval
                column = col
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return (column,max_eval)

    else:
        min_eval = math.inf
        column = vaild_cols[0]
        for col in vaild_cols:
            row = get_vaild_row(board , row)
            new_board  = board.copy()
            new_board[row][col] = BLUE
            eval = mini_max_fun(new_board, depth-1, alpha, beta, RED)
            if(eval < min_eval):
                eval = min_eval
                column = col
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return (column,min_eval)
