from board import Board
import game


EMPTY = 0
RED = 1
BLUE = 2

# def evaluate(board):




def mini_max_fun(board , depth , alpha , beta , current_player):
    (game_board, game_end,current_player) = board.get_game_grid()
    if depth == 0 or game_end:
        return evaluate(board, current_player)


    if current_player == RED:
        max_eval = float('-inf')
        for col in range(7):
            (valid , grid) = board.move(col,RED)
            if(not valid):
                continue
            eval = mini_max_fun(grid , depth-1 , alpha, beta,BLUE)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = float('inf')
        for col in range(7):
            (valid, grid) = board.move(col, BLUE)
            if(not valid):
                continue
            eval = mini_max_fun(grid, depth-1, alpha, beta, RED)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval





    





