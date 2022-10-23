class Piece():
    def __init__(self, type, value, color, location):
        self.type = type            # pawn: 0; knight: 1; bishop: 2; rook: 3; queen: 4; king: 5
        self.value = value          # pawn: 1; knight: 3; bishop: 3; rook: 5; queen: 9; king: -
        self.color = color          # white: 0; black: 1
        self.location = location    # square on the chess board, such as 'e4'

    def __str__(self) -> str:
        summary = "type: " + str(self.type) + "; color: " + str(self.color)  + "; location: " + str(self.location)
        return summary

        