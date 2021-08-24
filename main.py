from gameoflife import GameOfLife
import sys
import pygame


WIDTH = 800
HEIGHT = 600

pygame.init()
pygame.display.set_caption("Game Of Life")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
disp = pygame.time.Clock()
fps = 60

game = GameOfLife(screen)

def main():
    while True:
        
        disp.tick(fps)
        screen.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.draw()
        pygame.display.update()

if __name__ == "__main__":
    main()