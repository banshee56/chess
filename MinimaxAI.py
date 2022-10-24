import chess
from random import shuffle

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
            outcome = state.board.outcome()

            # wins
            # AI is white
            # outcome.winner == chess.WHITE == self.color == True
            if outcome.winner and self.color:
                return 78
            # AI is black
            # there was a checkmate, and self.color == chess.BLACK == False
            if outcome.termination.value == 1 and outcome.winner == self.color:
                print(state.board)
                print(outcome)
                print('cause 2')
                print('---------')
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
            utility = self.evaluation_fn(state)
            return utility
        
        v = -float('inf')

        for move in list(state.board.legal_moves):
            self.make_move(state, move)
            v = max(v, self.min_value(state))
            self.undo_move(state)

        return v

    def min_value(self, state):
        if self.cutoff_test(state):
            utility = self.evaluation_fn(state)
            return utility
        
        v = float('inf')

        for move in list(state.board.legal_moves):
            self.make_move(state, move)
            v = min(v, self.max_value(state))
            self.undo_move(state)

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