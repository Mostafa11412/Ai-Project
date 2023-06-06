import math
EMPTY = 0
RED = 1
BLUE = 2

ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4

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




def evaluate_window(window, player):
    score = 0
    opponent = get_opponent(player)  # Assuming player is either 1 or 2

    if window.count(player) == 4:
        score += 100
    elif window.count(player) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(player) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(0) == 1:
        score -= 4

    return score


def mini_max_fun(board , depth , alpha , beta , current_player):
    vaild_cols = get_vaild_cols(board)


    

    game_end = is_terminal_(board)
    if depth == 0 or game_end:
        if(game_end):
            if(winning_move(board , RED)):
                return (None,100000000000000)
            elif(winning_move(board , BLUE)):
                return(None,-100000000000000)
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
            if(eval > max_eval) :
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
            if(eval < min_eval):
                min_eval = eval 
                column = col
            beta = min(beta, min_eval)
            if beta <= alpha:
                break
        return (column,min_eval)