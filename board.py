class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]

    def display(self):
        print()
        for row in range(3):
            start = row * 3
            values = [
                self.cells[index] if self.cells[index] != " " else str(index + 1)
                for index in range(start, start + 3)
            ]
            print(f" {values[0]} | {values[1]} | {values[2]} ")
            if row < 2:
                print("---+---+---")
        print()

    def place(self, position, symbol):
        if position < 1 or position > 9:
            return False
        index = position - 1
        if self.cells[index] != " ":
            return False
        self.cells[index] = symbol
        return True

    def available_moves(self):
        return [index + 1 for index, cell in enumerate(self.cells) if cell == " "]

    def winner(self):
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in lines:
            if self.cells[a] != " " and self.cells[a] == self.cells[b] == self.cells[c]:
                return self.cells[a]
        return None

    def is_full(self):
        return " " not in self.cells

    def is_draw(self):
        return self.winner() is None and self.is_full()

    def reset(self):
        self.cells = [" " for _ in range(9)]

    def copy(self):
        new_board = Board()
        new_board.cells = self.cells.copy()
        return new_board
