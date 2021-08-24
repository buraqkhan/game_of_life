import numpy as np
import pygame

class GameOfLife():
    def __init__(self, state, WIDTH = 800, HEIGHT = 600):
        self.screen = state
        self.cols = int(HEIGHT/10)
        self.rows = int(WIDTH/10)

        self.grid = np.random.randint( 0, 2, size = (self.rows, self.cols), dtype=bool)

    
    def drawGrid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j]:
                    pygame.draw.rect(self.screen, (255,255,255), (i * 10, j * 10, 9, 9))
                else:
                    pygame.draw.rect(self.screen, (50,50,50), (i * 10, j * 10, 9, 9))

    def evolve(self):
        updated_grid = np.copy(self.grid)
        for i in range(self.rows):
            for j in range(self.cols):
                updated_grid[i][j] = self.rules(i, j)
        
        self.grid = updated_grid

    def rules(self, row, col):
        cell = self.grid[row][col]
        alive = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if i == 0 and j == 0:
                        continue
                    elif self.grid[row+i][col+j]:
                        alive += 1
                except:
                    continue

        if cell and alive < 2:
            return False
        elif cell and alive == 2 or alive == 3:
            return True
        elif cell and alive > 3:
            return False
        elif not cell and alive == 3:
            return True

    def draw(self):
        self.drawGrid()
        self.evolve()