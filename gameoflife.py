from random import randint

BOARD_SIZE = 10

class GameBoard:
    def __init__(self):
        self.board_state = [[randint(0,1) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def render(self):
        for row in range(BOARD_SIZE):
            print(' '.join([' ' if self.board_state[row][col] == 0 else '#' for col in range(BOARD_SIZE)]))


if __name__ == "__main__":
    game = GameBoard()
    game.render()    
