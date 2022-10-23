import chess
from random import shuffle

class State():
    def __init__(self, board):
        self.board = board
        self.depth = 0
        

class MinimaxAI():
    def __init__(self, depth):
        self.depth_limit =  depth

    def choose_move(self, board):
        state = State(board)
        move = self.minimax_decision(state)
        print("Minimax AI recommending move " + str(move))
        return move

    # def evaluation_fn(self, state):

    # checks if the state is a terminal state or not
    def terminal_test(self, state):
        outcome = state.board.outcome()

        # no win or draw
        if outcome is None:
            return False
        # checkmate or draws
        elif outcome.termination.value >= 1:
            return True
        
        return False

    # cutoff when we reach terminal state with a win or draw
    # or when we hit max depth
    def cutoff_test(self, state):
        if self.terminal_test(state) or state.depth > self.depth_limit:
            return True
        return False

    def minimax_decision(self, state):
        board = state.board
        arg_max = -float('inf')
        chosen_move = None

        moves = list(board.legal_moves)
        shuffle(moves)
        for move in moves:
            state.depth += 1

            board.push(move)
            utility = self.min_value(state)

            state.depth -= 1

            if utility >  arg_max:
                arg_max = utility
                chosen_move = move
            
            board.pop()
        
        return chosen_move

    def max_value(self, state):
        if self.cutoff_test(state):
            return self.evaluation_fn(state)
        
        board = state.board
        v = -float('inf')

        for move in list(board.legal_moves):
            state.depth += 1

            board.push(move)
            v = max(v, self.min_value(state))
            board.pop()

            state.depth -= 1

        return v

    def min_value(self, state):
        if self.cutoff_test(state):
            return self.evaluation_fn(state)
        
        board = state.board
        v = float('inf')

        for move in list(board.legal_moves):
            state.depth += 1

            board.push(move)
            v = min(v, self.max_value(state))
            board.pop()

            state.depth -= 1

        return v
