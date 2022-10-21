import chess

class MinimaxAI():
    def __init__(self, depth):
        self.depth_limit =  depth
    
    def get_successors(self, state):
        # get_successors functions
        pass

    # checks if the state is a terminal state or not
    def terminal_test(self, state):
        children = self.get_successors(state)
        
        # no children -> terminal state
        if not children:
            return True
        
        # not terminal state
        return False

    def choose_move(self, board):
        pass

    def max_value(self, state):
        pass

    def min_value(self, state):
        pass
