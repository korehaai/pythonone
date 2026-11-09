import unittest

from board import Board
from players import SmartComputerPlayer


class TestSmartComputerPlayer(unittest.TestCase):
    def test_takes_winning_move(self):
        board = Board()
        board.place(8, "X")
        board.place(9, "X")
        board.place(4, "O")
        board.place(5, "O")
        player = SmartComputerPlayer("Computer", "O")
        self.assertEqual(player.get_move(board), 6)

    def test_blocks_opponent_winning_move(self):
        board = Board()
        board.place(1, "X")
        board.place(2, "X")
        player = SmartComputerPlayer("Computer", "O")
        self.assertEqual(player.get_move(board), 3)


if __name__ == "__main__":
    unittest.main()
