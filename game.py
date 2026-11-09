from board import Board
from players import HumanPlayer, RandomComputerPlayer, SmartComputerPlayer


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.scores = {"X": 0, "O": 0, "draws": 0}

    def run(self):
        print("Welcome to Tic-Tac-Toe!")
        while True:
            players = self._choose_players()
            self._play_round(players)
            if not self._play_again():
                self._show_scores()
                print("Thanks for playing!")
                break

    def _choose_players(self):
        while True:
            print("\nChoose a game mode:")
            print("1. Player vs Player")
            print("2. Player vs Computer")
            mode = input("Enter 1 or 2: ").strip()
            if mode == "1":
                return {
                    "X": HumanPlayer("Player 1", "X"),
                    "O": HumanPlayer("Player 2", "O")
                }
            if mode == "2":
                return self._choose_computer()
            print("Please choose 1 or 2.")

    def _choose_computer(self):
        while True:
            print("\nChoose computer difficulty:")
            print("1. Easy")
            print("2. Unbeatable")
            difficulty = input("Enter 1 or 2: ").strip()
            if difficulty == "1":
                computer = RandomComputerPlayer("Computer", "O")
            elif difficulty == "2":
                computer = SmartComputerPlayer("Computer", "O")
            else:
                print("Please choose 1 or 2.")
                continue
            return {
                "X": HumanPlayer("Player", "X"),
                "O": computer
            }

    def _play_round(self, players):
        self.board.reset()
        current_symbol = "X"
        while True:
            self.board.display()
            player = players[current_symbol]
            print(f"{player.name}'s turn.")
            move = player.get_move(self.board)
            self.board.place(move, current_symbol)

            winner = self.board.winner()
            if winner:
                self.board.display()
                print(f"{players[winner].name} wins!")
                self.scores[winner] += 1
                return
            if self.board.is_full():
                self.board.display()
                print("It's a draw!")
                self.scores["draws"] += 1
                return
            current_symbol = "O" if current_symbol == "X" else "X"

    def _play_again(self):
        while True:
            answer = input("\nPlay another round? (y/n): ").strip().lower()
            if answer in {"y", "yes"}:
                return True
            if answer in {"n", "no"}:
                return False
            print("Please enter y or n.")

    def _show_scores(self):
        print("\nFinal scores")
        print(f"X wins: {self.scores['X']}")
        print(f"O wins: {self.scores['O']}")
        print(f"Draws: {self.scores['draws']}")
