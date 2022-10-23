# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame


import sys


player1 = MinimaxAI(3)
# player1 = RandomAI()
player2 = RandomAI()

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()

# board = chess.Board("r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 4")
# board = chess.Board("rnb1k1nr/pppp1ppp/8/2b1p3/4P3/2N2N2/pppp1qpp/R1BQKB1R w")
# print(board)
# print(board.outcome())

#print(hash(str(game.board)))
