# chess-ai
## Bansharee Ireen

AI playing chess game by searching the chess game tree using a cut-off evaluation for quick responses.

## How to Use

### `ChessGame`

I modified the class to allow the constructor to take an optional parameter, `init_board`, which can take a starting `fen` for the game board; otherwise, it uses the default `fen` used by the `chess` package:

```Python
Chess(player1, player2, init_board="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
```

### `MinimaxAI`

`MinimaxAi(depth)` takes 1 parameter, `depth`, which refers to the depth limit of the game tree search. It uses the `ChessGame` class to create a game board.

#### Usage Example

2 Minimax AIs playing against each other at different depth limits.

```Python
depth = 2
player1 = MinimaxAI(depth)
player2 = MinimaxAI(depth+1)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()
```

### `AlphaBetaAI`

`AlphaBetaAi(depth)` takes 1 parameter, `depth`, which refers to the depth limit of the game tree search.

#### Usage Example

AlphaBeta and Minimax AIs playing against each other at the same depth limit.

```Python
depth = 2
player1 = AlphaBetaAI(depth)
player2 = MinimaxAI(depth)

game = ChessGame(player1, player2)

while not game.is_game_over():
    print(game)
    game.make_move()
```

## Implementation Choices

* Keeping track of chess pieces

    Instead of having my `State` object keep track of all the `Piece` objects in that state, I decided to only keep track of the pieces on the board whenever I need my evaluation function to calculate the value of a move, which is typically done at cutoff. I did this, as opposed to always keeping track of the pieces, as I assumed that recalculating the state and checking for conquered pieces at every state explored would be much slower.
