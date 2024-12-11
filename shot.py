import pygame
from circleshape import *
from constants import *
from player import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
        # if bullet reaches the edges of the screen, delete the bullet so that
        # it doesn't fly infinitely in whichever direction
        if (
            self.position.x > SCREEN_WIDTH or self.position.x < 0
            or self.position.y > SCREEN_HEIGHT or self.position.y < 0
        ):
            self.kill()