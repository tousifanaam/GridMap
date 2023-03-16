from gridmap import GridMap as gm
import random
from os import system
from basics import *


class GameofLife:

    def __init__(self, r, c) -> None:
        self.r = r # total row
        self.c = c # total column
        self.plots = [] # [(row0, column0), ..., (rowX, columnX)]

    def next(self):
        "calculate next state"
        new_plots = []
        for i in range(self.r):
            for j in range(self.c):
                live_neighbors = self.count_live_neighbors(i, j)
                if (i, j) in self.plots:
                    if live_neighbors in (2, 3):
                        new_plots.append((i, j))
                else:
                    if live_neighbors == 3:
                        new_plots.append((i, j))
        self.plots = new_plots

    def count_live_neighbors(self, row, col):
        "count live neighbors around given cell"
        count = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if (i, j) in self.plots and (i, j) != (row, col):
                    count += 1
        return count

    def __str__(self) -> str:
        return gm(self.r, self.c, *self.plots).font2()


def clear():
    _ = system('cls')

def main():
    # Initialize GameofLife with a 10x10 grid
    game = GameofLife(50, 50)
    
    # Generate random starting state with neighbors
    for row in range(game.r):
        for col in range(game.c):
            # Generate a random number between 0 and 1
            rand_num = random.random()
            # Add the plot if the random number is greater than 0.5
            if rand_num > 0.5:
                game.plots.append((row, col))
    
    # Calculate the next state for 10 iterations and print the grid after each iteration
    i = 1
    while True:
        print("Iteration", i)
        print(game)
        game.next()
        clear()
        i += 1

if __name__ == "__main__":
    main()



    