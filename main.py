from constants import *
from player import *
from circleshape import *
import pygame


def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0.03
    player = Player(SCREEN_WIDTH/2, SCREEN_WIDTH/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        #dt = fps.tick() / 1000
        fps.tick(60)
        
        pygame.display.flip()


if __name__ == "__main__":
    main()