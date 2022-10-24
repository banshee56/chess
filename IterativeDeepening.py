from MinimaxAI import MinimaxAI

# inputs:
#       * depth_limit: the max limit we will incremement each iteration's depth to
# output: returns the solution, a SearchSolution object
class IterativeDeepening:
    def __init__(self, depth):
        self.depth_limit =  depth

    def choose_move(self, board):
        # increment current depth until it reaches the depth limit
        for curr_depth in range(self.depth_limit + 1):
            player = MinimaxAI(curr_depth)
            best_move = player.choose_move(board)
            print("best move at depth " + str(curr_depth) + " = " + str(best_move))

        return best_move