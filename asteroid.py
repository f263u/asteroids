import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return()
        angle = random.uniform(20, 50)
        random_angle = self.velocity + self.velocity.rotate(angle)
        minus_random_angle = self.velocity - self.velocity.rotate(angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = random_angle * 1.2
        new_asteroid_2.velocity = minus_random_angle * 1.2
        self.kill()


