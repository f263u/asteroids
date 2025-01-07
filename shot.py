import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, SHOT_RADIUS, SHOT_LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        
