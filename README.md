# Tic-Tac-Toe in Python

A terminal-based Tic-Tac-Toe game built using Python's standard library. It supports two-player matches, single-player matches against a computer, two computer difficulty levels, score tracking, and automated tests.

## Features

- Player vs Player mode
- Player vs Computer mode
- Easy computer opponent with random legal moves
- Unbeatable computer opponent using the minimax algorithm
- Input validation
- Match score tracking across rounds
- Unit tests using `unittest`
- No third-party dependencies

## Requirements

- Python 3.8 or newer

## Run the game

Clone the repository and open its directory:

```bash
git clone https://github.com/YOUR-USERNAME/tictactoe-python.git
cd tictactoe-python
python main.py
```

On some systems, use `python3 main.py` instead.

## How to play

The board positions are numbered from 1 to 9:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Choose a game mode, select a difficulty when playing against the computer, and enter the number of the position where you want to place your symbol. The first player uses X and the second player or computer uses O.

## Run tests

From the repository root, run:

```bash
python -m unittest discover -s tests -v
```

## Project structure

```text
tictactoe-python/
├── main.py
├── game.py
├── board.py
├── players.py
├── tests/
│   ├── test_board.py
│   └── test_players.py
└── README.md
```

## Technologies

- Python
- Object-oriented programming
- Minimax game-search algorithm
- Python standard library (`unittest`, `random`)

## License

This project is available under the MIT License.
