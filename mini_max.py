from board import Board
import game


EMPTY = 0
RED = 1
BLUE = 2

# def evaluate(board):




def mini_max_fun(board , depth , alpha , beta , maximizing_player):
    (game_board, game_end,player) = board.get_game_grid()
    if depth == 0 or game_end:
        return evaluate(board)


    if maximizing_player:
        max_eval = float('-inf')
        for col in range(7):
            (valid , grid) = board.move(col,RED)
            if(not valid):
                continue
            eval = mini_max_fun(grid , depth-1 , alpha, beta,False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
            return max_eval







    





