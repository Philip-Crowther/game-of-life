from random import randint
import time

BOARD_SIZE = 30

class GameBoard:
    """Conway's Game of Life class"""
    def __init__(self):
        self.board_state = [[randint(0,1) for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    def render(self):
        # print top border
        print('', ''.join(['—' for _ in range((BOARD_SIZE * 2) + 1)]))
        # print content
        for row in range(BOARD_SIZE):
            print('|', ' '.join([' ' if self.board_state[row][col] == 0 else '#' for col in range(BOARD_SIZE)]), '|')
        # print bottom border
        print('', ''.join(['—' for _ in range((BOARD_SIZE * 2) + 1)]))    

    def next_state(self):
        # calculate next board state
        def count_neighbors(row, col):
            # count number of neighbors
            row_start = row
            row_stop = row + 1
            col_start = col
            col_stop = col + 1

            if row > 0:
                row_start -= 1
            if row < BOARD_SIZE - 1:
                row_stop += 1
            if col > 0:
                col_start -= 1
            if col < BOARD_SIZE - 1:
                col_stop += 1
            
            count = 0
            for r in range(row_start, row_stop):
                for c in range(col_start, col_stop):
                    if r == row and c == col:
                        continue
                    count += self.board_state[r][c]
            return count

        number_of_neighbors = [[count_neighbors(row, col) for col in range (BOARD_SIZE)] for row in range(BOARD_SIZE)]

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                # iterate through each position
                if number_of_neighbors[row][col] == 3:
                    # every position with three neighbors comes back
                    self.board_state[row][col] = 1
                elif self.board_state[row][col] == 0:
                    # position is dead
                    continue
                elif number_of_neighbors[row][col] == 2:
                    # position is alive
                    self.board_state[row][col] = 1
                else: # position is dead
                    self.board_state[row][col] = 0



if __name__ == "__main__":
    def board_is_active(board):
        # function to check if there are any life positions on the board
        for row in board.board_state:
            if 1 in row:
                return True
        return False

    current_game = GameBoard()
    while board_is_active(current_game):
        current_game.render()    
        current_game.next_state()
        time.sleep(.5)
    current_game.render()
