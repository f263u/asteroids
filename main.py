# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #Display on entry
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Setup engine
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps_clock = pygame.time.Clock()
    dt = 0

    #Generate Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    #Initialize Objects
    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while 1:
        #Process Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        #Handle Input
        for item in updatable:
            item.update(dt)

        #Update Render
        screen.fill(COLOR_BLACK)
        for item in drawable:
            item.draw(screen)

        #Clear Screen Buffer
        pygame.display.flip()
        dt = fps_clock.tick(FRAME_RATE)/1000
        

if __name__ == "__main__":
    main()