# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    fps_clock = pygame.time.Clock()
    dt = 0

    player_1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        #Input
        player_1.update(dt)

        #Rendering
        screen.fill((0,0,0))
        player_1.draw(screen)

        pygame.display.flip()
        dt = fps_clock.tick(FRAME_RATE)/1000
        

if __name__ == "__main__":
    main()