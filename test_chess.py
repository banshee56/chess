# pip3 install python-chess
import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame


import sys




player2 = AlphaBetaAI(2)
player1 = HumanPlayer()

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()

# board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")

# print(board.outcome())
# board = chess.Board()
# print(board)

# print(ord('A'))