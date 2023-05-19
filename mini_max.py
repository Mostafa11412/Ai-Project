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


def score_(board, piece):
	score = 0

	## Score center column
	center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
	center_count = center_array.count(piece)
	score += center_count * 3

	## Score Horizontal
	for r in range(ROW_COUNT):
		row_array = [int(i) for i in list(board[r,:])]
		for c in range(COLUMN_COUNT-3):
			window = row_array[c:c+WINDOW_LENGTH]
			score += get_Score_(window, piece)

	## Score Vertical
	for c in range(COLUMN_COUNT):
		col_array = [int(i) for i in list(board[:,c])]
		for r in range(ROW_COUNT-3):
			window = col_array[r:r+WINDOW_LENGTH]
			score += get_Score_(window, piece)

	## Score posiive sloped diagonal
	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
			score += get_Score_(window, piece)

	for r in range(ROW_COUNT-3):
		for c in range(COLUMN_COUNT-3):
			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
			score += get_Score_(window, piece)

	return score



def mini_max_fun(board , depth , alpha , beta , current_player):
    (game_board, game_end,current_player) = board.get_game_grid()
    if depth == 0 or game_end:

        if(game_end):
            if(current_player == RED):
                return (None,math.inf)
            elif(current_player == BLUE):
                return(None,-math.inf)
            else:
                return(None,0)
        else :
             return (None , score_(board , current_player))

    if current_player == RED:
        max_eval = -math.inf

        column = 0

        for col in range(7):
            (valid , grid) = board.move(col,RED)
            if(not valid):
                continue
            eval = mini_max_fun(grid , depth-1 , alpha, beta,BLUE)
            if(eval > max_eval) :
                max_eval = eval
                column = col

            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return (max_eval,column)

    else:
        min_eval = math.inf
        column = 0
        for col in range(7):
            (valid, grid) = board.move(col, BLUE)
            if(not valid):
                continue
            eval = mini_max_fun(grid, depth-1, alpha, beta, RED)
            if(eval < min_eval):
                eval = min_eval
                column = col
            # min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return (min_eval,column)
