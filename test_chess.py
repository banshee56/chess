# pip3 install python-chess
import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IterativeDeepening import IterativeDeepening

import sys

player1 = HumanPlayer()
player2 = AlphaBetaAI(3)

game = ChessGame(player1, player2)
while not game.is_game_over()[0]:
    print(game)
    game.make_move()

# matches = 10
# white_wins = 0
# black_wins = 0
# draws = 0
# for i in range (matches):
#     game = ChessGame(player1, player2)
#     turn = 0
#     while not game.is_game_over()[0]:
#         print(game)
#         game.make_move()
#         turn += 1

#     # if game ends with a winner
#     if game.is_game_over()[1] == 1:
#         if (turn - 1) % 2 == 0:
#             print("white won")
#             white_wins += 1
#         else:
#             print("black won")
#             black_wins += 1
#     # draw
#     else:
#         draws += 1

# print("white: "+str(white_wins)+"; black: "+str(black_wins))

# board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")

# print(board.outcome())
# board = chess.Board()
# print(board)

# print(ord('A'))