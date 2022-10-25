# Name: Bansharee Ireen
# 
# IterativeDeepening - the iterative deepening implementation of minimax
# cosc76
# oct 24 2022

from MinimaxAI import MinimaxAI

class IterativeDeepening:
    def __init__(self, depth):
        # the max limit we will incremement each iteration's depth to
        self.depth_limit =  depth

    def choose_move(self, board):
        # increment current depth until it reaches the depth limit
        for curr_depth in range(self.depth_limit + 1):
            player = MinimaxAI(curr_depth)

            # get the best move at the current depth and print it
            best_move = player.choose_move(board)
            print("best move at depth " + str(curr_depth) + " = " + str(best_move))
            print("--------------------------")

        # return the best move found at the last depths
        return best_move