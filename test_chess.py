# Name: Bansharee Ireen
# 
# test script - can be run to run tests using human players, alphabeta, minimax, and iterative deepening AIs
# cosc76
# oct 24 2022

# pip3 install python-chess
import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IterativeDeepening import IterativeDeepening

import sys

player1 = IterativeDeepening(3)
player2 = AlphaBetaAI(3)

game = ChessGame(player1, player2)
while not game.is_game_over()[0]:
    print(game)
    game.make_move()


# making two AIs fight a set number of matches
make_AIs_fight = False

if make_AIs_fight:
    matches = 10            # number of matches played
    white_wins = 0          # number of wins for white
    black_wins = 0          # number of wins for black
    draws = 0               # number of draws

    player1 = MinimaxAI(2)
    player2 = AlphaBetaAI(3)

    for i in range (matches):
        # create a new game
        game = ChessGame(player1, player2)

        # the first turn goes to white, represented by 0
        turn = 0

        while not game.is_game_over()[0]:
            print(game)
            game.make_move()

            # next player's turn
            turn += 1

        # if game ends with a winner, it returns a 1
        if game.is_game_over()[1] == 1:
            # white has even turn numbers
            if (turn - 1) % 2 == 0:
                print("white won")
                white_wins += 1
            else:
                print("black won")
                black_wins += 1
        # draw
        else:
            draws += 1

    print("white: "+str(white_wins)+"; black: "+str(black_wins))
