import chess
from random import shuffle
from Piece import Piece
from time import time

class State():
    def __init__(self, board):
        self.board = board
        self.depth = 0

        # # to quickly check what piece is at a location we want to move to
        # letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        # nums = ['1', '2', '3', '4', '5', '6', '7', '8']
        # locations = {}
        # # initialize
        # for letter in letters:
        #     for num in nums:
        #         locations[str(letter+num)] = None

        # # a collection of pieces
        # black = []
        # white = []

        # # mapping locations to the occupying pieces
        # row = 8
        # col = 1 # = ord('a')-96 
        # for char in str(board):
        #     if col > 8:
        #         col = 1

        #     if char == ' ':
        #         continue

        #     if char == '.':
        #         col += 1
        #         continue
        #     if char == '\n':
        #         row -= 1
        #         continue

        #     # white pieces are capital letters with ord() values < 97 ('a')
        #     if ord(char) < 97:
        #         white.append(char)

        #         if char == 'P':
        #             type = 0
        #             val = 1
        #         if char == 'N':
        #             type = 1
        #             val = 3
        #         if char == 'B':
        #             type = 2
        #             val = 3
        #         if char == 'R':
        #             type = 3
        #             val = 5
        #         if char == 'Q':
        #             type = 4
        #             val = 9
        #         if char == 'K':
        #             type = 5
        #             val = None

        #         locations[str(chr(col+96))+str(row)] = Piece(type, val, 0, str(chr(col+96))+str(row))

        #     else:
        #         black.append(char)

        #         if char == 'p':
        #             type = 0
        #             val = 1
        #         if char == 'n':
        #             type = 1
        #             val = 3
        #         if char == 'b':
        #             type = 2
        #             val = 3
        #         if char == 'r':
        #             type = 3
        #             val = 5
        #         if char == 'q':
        #             type = 4
        #             val = 9
        #         if char == 'k':
        #             type = 5
        #             val = None

        #         locations[str(chr(col+96))+str(row)] = Piece(type, val, 1, str(chr(col+96))+str(row))
        #     col += 1

        # self.locations = locations
        # self.black_pieces = black
        # self.white_pieces = white

class MinimaxAI():
    def __init__(self, color, depth):
        self.color = color
        self.depth_limit =  depth

    def choose_move(self, board):
        state = State(board)
        move = self.minimax_decision(state)
        print("Minimax AI recommending move " + str(move))
        return move

    def evaluation_fn(self, state):
        # if terminal, win > draw > loss -> 0
        if self.terminal_test(state):
            if self.color == chess.WHITE:
                enemy = chess.BLACK
            else:
                enemy = chess.WHITE

            outcome = state.board.outcome()

            # AI won
            if outcome.winner == self.color:
                return 78
            # loss
            elif outcome.winner == enemy:
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
        if self.color == 0:
            score = white_score - black_score

        # it is black
        else:
            score = black_score - white_score
        
        return score

    # checks if the state is a terminal state or not
    def terminal_test(self, state):
        if state.board.outcome():
            return True
        return False

    # cutoff when we reach terminal state with a win or draw
    # or when we hit max depth
    def cutoff_test(self, state):
        if self.terminal_test(state) or state.depth > self.depth_limit:
            return True
        return False

    def minimax_decision(self, state):
        arg_max = -float('inf')
        chosen_move = None

        moves = list(state.board.legal_moves)
        shuffle(moves)

        for move in moves:
            self.make_move(state, move)

            utility = self.min_value(state)
            if utility >  arg_max:
                arg_max = utility
                chosen_move = move
            
            self.undo_move(state)
        
        print(arg_max)
        return chosen_move

    def max_value(self, state):
        if self.cutoff_test(state):
            # before  = time()
            utility = self.evaluation_fn(state)
            # after = time()
            # print(after-before)
            return utility
        
        v = -float('inf')

        for move in list(state.board.legal_moves):
            self.make_move(state, move)
            v = max(v, self.min_value(state))
            self.undo_move(state)

        return v

    def min_value(self, state):
        if self.cutoff_test(state):
            # before  = time()
            utility = self.evaluation_fn(state)
            # after = time()
            # print(after-before)
            return utility
        
        v = float('inf')

        for move in list(state.board.legal_moves):
            # prev_piece = state.locations[move[:2]]
            self.make_move(state, move)
            v = min(v, self.max_value(state))
            self.undo_move(state)

        return v

    def make_move(self, state, move):
        state.depth += 1
        state.board.push(move)

        # # update tracking stuff
        # origin = move[:2]
        # end = move[2:]
        
        # piece = state.locations[origin]
        # state.locations[origin] = None

        # state.locations[end] = piece

    def undo_move(self, state):
        state.board.pop()
        state.depth -= 1

    def find_pieces(self, state):
        white = []
        black = []

        row = 8
        col = 1
        for char in str(state.board):
            if col > 8:
                col = 1

            if char == ' ':
                continue

            if char == '.':
                col += 1
                continue
            if char == '\n':
                row -= 1
                continue

            # white pieces are capital letters with ord() values < 97 ('a')
            if ord(char) < 97:
                white.append(char)       
            else:
                black.append(char)
            col += 1

        return (white, black)