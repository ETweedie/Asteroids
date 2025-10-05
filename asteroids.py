import pygame
from circleshape import CircleShape

class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle((self.x, self.y), self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)