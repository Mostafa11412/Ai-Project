from calendar import c
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

def main():
    board = Board()

    time.sleep(2)
    game_end = False
    while not game_end:


        (game_board, game_end) = board.get_game_grid()

        # FOR DEBUG PURPOSES
        board.print_grid(game_board)

        # YOUR CODE GOES HERE

        # Insert here the action you want to perform based on the output of the algorithm
        # You can use the following function to select a column



        (best_column,mx) = mini_max.mini_max_fun(game_board ,2,-math.inf,math.inf,RED)

        # random_column = random.randint(0, 6)
        board.select_column(best_column)

        time.sleep(2)


if __name__ == "__main__":
    main()
