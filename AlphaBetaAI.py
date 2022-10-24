import chess
from random import shuffle

class State():
    def __init__(self, board):
        self.board = board
        self.depth = 0

class AlphaBetaAI():
    def __init__(self, depth):
        # color defaulted to white
        self.color = True
        self.depth_limit =  depth

    def choose_move(self, board):
        state = State(board)

        # set the AI's color
        fen = str(board.fen()).split()
        if fen[-5] == 'w':
            self.color = True
        else:
            self.color = False

        move = self.alphabeta_decision(state)
        print("Alpha Beta AI recommending move " + str(move))
        return move

    def evaluation_fn(self, state):
        # if terminal, win > draw > loss -> 0
        
        if self.terminal_test(state):
            outcome = state.board.outcome()

            # wins
            # AI is white
            # outcome.winner == chess.WHITE == self.color == True
            if outcome.winner and self.color:
                return 78
            # AI is black
            # there was a checkmate, and self.color == chess.BLACK == False
            if outcome.termination.value == 1 and outcome.winner == self.color:
                return 78

            # losses
            # AI is black
            # the enemy, white, won 
            if outcome.winner and not self.color:
                return -78
            # AI is white
            # the enemy, black, won
            if outcome.termination.value == 1 and not outcome.winner and self.color:
                return -78

            # draw
            else:
                return 0

        # if non-terminal, weighted points
        (white, black) = self.find_pieces(state)

        white_score = 0
        for char in white:
            if char == 'K':
                continue  
            elif char == 'P':
                val = 1
            elif char == 'N':
                val = 3
            elif char == 'B':
                val = 3
            elif char == 'R':
                val = 5
            elif char == 'Q':
                val = 9
            
            white_score += val

        black_score = 0
        for char in black:
            if char == 'k':
                continue
            elif char == 'p':
                val = 1
            elif char == 'n':
                val = 3
            elif char == 'b':
                val = 3
            elif char == 'r':
                val = 5
            elif char == 'q':
                val = 9
    
            black_score += val
        
        # minimax is white
        if self.color == chess.WHITE:
            score = white_score - black_score

        # it is black
        else:
            score = black_score - white_score
        
        return score

    # checks if the state is a terminal state or not
    def terminal_test(self, state):
        # if there are legal moves left
        if list(state.board.legal_moves):
            return False
        # otherwise, we reached the end
        return True

    # cutoff when we reach terminal state with a win or draw
    # or when we hit max depth
    def cutoff_test(self, state):
        if self.terminal_test(state) or state.depth > self.depth_limit:
            return True
        return False

    def alphabeta_decision(self, state):
        arg_max = -float('inf')
        chosen_move = None

        moves = list(state.board.legal_moves)
        shuffle(moves)

        for move in moves:
            self.make_move(state, move)

            utility = self.min_value(state, -float('inf'), float('inf'))
            if utility >  arg_max:
                arg_max = utility
                chosen_move = move
            
            self.undo_move(state)
        
        print(arg_max)
        return chosen_move

    def max_value(self, state, alpha, beta):
        if self.cutoff_test(state):
            utility = self.evaluation_fn(state)
            return utility
        
        v = -float('inf')

        for move in list(state.board.legal_moves):
            self.make_move(state, move)
            v = max(v, self.min_value(state, alpha, beta))
            self.undo_move(state)

            if v >= beta:
                return v

            alpha = max(alpha, v)

        return v

    def min_value(self, state, alpha, beta):
        if self.cutoff_test(state):
            utility = self.evaluation_fn(state)
            return utility
        
        v = float('inf')

        for move in list(state.board.legal_moves):
            self.make_move(state, move)
            v = min(v, self.max_value(state, alpha, beta))
            self.undo_move(state)

            if v <= alpha: 
                return v

            beta = min(beta, v)

        return v

    def make_move(self, state, move):
        # made a move at a lower depth
        # so increment depth
        state.depth += 1
        state.board.push(move)

    def undo_move(self, state):
        # undid move, so decrement depth
        state.board.pop()
        state.depth -= 1

    def find_pieces(self, state):
        white = []
        black = []

        # going through the characters on the board to figure out which side has which pieces left
        row = 8
        col = 1
        for char in str(state.board):
            # go to first col
            if col > 8:
                col = 1

            # ignore
            if char == ' ':
                continue
            
            # ignore empty square
            if char == '.':
                col += 1
                continue

            # go to next row
            if char == '\n':
                row -= 1
                continue

            # white pieces are capital letters with ord() values < 97 ('a')
            if ord(char) < 97:
                white.append(char)    
            # char is a black piece otherwise   
            else:
                black.append(char)

            # go to next col
            col += 1

        return (white, black)
