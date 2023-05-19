from board import Board
import game
import math


EMPTY = 0
RED = 1
BLUE = 2





def evaluate(board, current_player):
    





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
            score = evaluate(board , current_player) 

        
        
        


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
