import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Ensure Sprite init always runs
        if hasattr(self.__class__, "containers"):
            pygame.sprite.Sprite.__init__(self, self.__class__.containers)
        else:
            pygame.sprite.Sprite.__init__(self)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # being overridden in other files
        pass

    def update(self, dt):
        # being overridden in other files
        pass

    def collision(self, other):
        if pygame.math.Vector2.distance_to(self.position, other.position) <= (self.radius + other.radius):
            return True
        return False