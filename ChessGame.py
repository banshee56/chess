import chess


class ChessGame:
    def __init__(self, player1, player2):
        self.board = chess.Board(fen="1B2q1B1/2n1kPR1/R1b2n1Q/2p1r3/8/3Q2B1/4p3/4K3 w - - 0 1")
        self.players = [player1, player2]

    def make_move(self):

        player = self.players[1 - int(self.board.turn)]
        move = player.choose_move(self.board)

        self.board.push(move)  # Make the move

    def is_game_over(self):
        return self.board.is_game_over()

    def __str__(self):

        column_labels = "\n----------------\na b c d e f g h\n"
        board_str =  str(self.board) + column_labels

        # did you know python had a ternary conditional operator?
        move_str = "White to move" if self.board.turn else "Black to move"

        return board_str + "\n" + move_str + "\n"
