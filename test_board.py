import unittest

from board import Board


class TestBoard(unittest.TestCase):
    def test_board_starts_empty(self):
        board = Board()
        self.assertEqual(board.available_moves(), list(range(1, 10)))
        self.assertIsNone(board.winner())

    def test_place_valid_move(self):
        board = Board()
        self.assertTrue(board.place(5, "X"))
        self.assertEqual(board.cells[4], "X")

    def test_reject_occupied_position(self):
        board = Board()
        board.place(1, "X")
        self.assertFalse(board.place(1, "O"))

    def test_reject_out_of_range_position(self):
        board = Board()
        self.assertFalse(board.place(0, "X"))
        self.assertFalse(board.place(10, "X"))

    def test_detect_row_winner(self):
        board = Board()
        for position in (1, 2, 3):
            board.place(position, "X")
        self.assertEqual(board.winner(), "X")

    def test_detect_diagonal_winner(self):
        board = Board()
        for position in (1, 5, 9):
            board.place(position, "O")
        self.assertEqual(board.winner(), "O")

    def test_detect_draw(self):
        board = Board()
        moves = [(1, "X"), (2, "O"), (3, "X"), (5, "O"),
                 (4, "X"), (6, "O"), (8, "X"), (7, "O"), (9, "X")]
        for position, symbol in moves:
            board.place(position, symbol)
        self.assertTrue(board.is_draw())

    def test_copy_is_independent(self):
        board = Board()
        board.place(1, "X")
        copied = board.copy()
        copied.place(2, "O")
        self.assertEqual(board.cells[1], " ")
        self.assertEqual(copied.cells[1], "O")


if __name__ == "__main__":
    unittest.main()
