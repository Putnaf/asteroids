from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *
import pygame


def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_WIDTH/2)
    af = AsteroidField()
    dt = .03
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in updatable:
            i.update(dt)

        for i in asteroids:
            if i.collide(player) == True:
                print("Game over!")
                return
            for bullet in shots:
                if i.collide(bullet) == True:
                    i.split()
                    bullet.kill()

        screen.fill("black")
        
        for i in drawable:
            i.draw(screen)
        #dt = fps.tick() / 1000
        fps.tick(60)
        
        pygame.display.flip()


if __name__ == "__main__":
    main()