import chess

class ChessGame:
    def __init__(self, player1, player2, init_board="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"):
        self.board = chess.Board(fen=init_board)
        self.players = [player1, player2]

    def make_move(self):

        player = self.players[1 - int(self.board.turn)]
        move = player.choose_move(self.board)

        self.board.push(move)  # Make the move

    def is_game_over(self):
        if self.board.is_game_over():
            column_labels = "\n----------------\na b c d e f g h\n"
            board_str =  str(self.board) + column_labels
            print(board_str)

            # ended in checkmate
            if self.board.outcome().termination.value == 1:
                # game is over = True, has a winner = 1
                return (True, 1)
            # game is over = True, draw = 0
            return (True, 0)

        # game is not over
        return (False, 0)

    def __str__(self):

        column_labels = "\n----------------\na b c d e f g h\n"
        board_str =  str(self.board) + column_labels

        # did you know python had a ternary conditional operator?
        move_str = "White to move" if self.board.turn else "Black to move"

        return board_str + "\n" + move_str + "\n"
