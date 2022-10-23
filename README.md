# chess-ai
AI that plays chess

## How to Use

### `MinimaxAI`

`MinimaxAi(chess.COLOR, depth)` takes 2 parameters:
* `chess.COLOR` uses the `COLOR` class of the `chess` package. Please input the `chess.COLOR` of the AI.

    When `MinimaxAi` plays as white:
    ```C
    game = ChessGame(MinimaxAI(chess.WHITE, depth), player2)
    ```

    When it plays as black:
    ```C
    game = ChessGame(player1, MinimaxAI(chess.BLACK, depth))
    ```

* `depth` refers to the depth limit of the game tree search.

## Implementation Choices

* Keeping track of chess pieces

    Instead of having my `State` object keep track of all the `Piece` objects in that state, I decided to only keep track of the pieces on the board whenever I need my evaluation function to calculate the value of a move, which is typically done at cutoff. I did this, as opposed to always keeping track of the pieces, as I assumed that recalculating the state and checking for conquered pieces at every state explored would be much slower.