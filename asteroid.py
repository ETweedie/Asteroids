import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        vector1 = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(random_angle)
        vector2 = pygame.Vector2(self.velocity.x, self.velocity.y).rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_rock1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_rock2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_rock1.velocity = vector1 * 1.2
        new_rock2.velocity = vector2 * 1.2
        
    
    def update(self, dt):
        self.position += self.velocity * dt