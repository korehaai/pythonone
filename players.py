import random


class HumanPlayer:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        while True:
            choice = input(f"{self.name} ({self.symbol}), choose a position (1-9): ").strip()
            if not choice.isdigit():
                print("Enter a number from 1 to 9.")
                continue
            position = int(choice)
            if position not in board.available_moves():
                print("That position is not available. Try again.")
                continue
            return position


class RandomComputerPlayer:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        return random.choice(board.available_moves())


class SmartComputerPlayer:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self, board):
        best_score = float("-inf")
        best_move = None
        for move in board.available_moves():
            candidate = board.copy()
            candidate.place(move, self.symbol)
            score = self._minimax(candidate, False)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def _minimax(self, board, maximizing):
        result = board.winner()
        if result == self.symbol:
            return 1
        if result is not None:
            return -1
        if board.is_full():
            return 0

        opponent = "O" if self.symbol == "X" else "X"
        scores = []
        for move in board.available_moves():
            candidate = board.copy()
            candidate.place(move, self.symbol if maximizing else opponent)
            scores.append(self._minimax(candidate, not maximizing))

        return max(scores) if maximizing else min(scores)
