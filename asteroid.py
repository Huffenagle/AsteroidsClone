import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position), self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        self.random_angle = random.uniform(20, 50)
        self.split_vector_a = self.velocity.rotate(self.random_angle)
        self.split_vector_b = self.velocity.rotate(-self.random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.split_roid_a = Asteroid(self.position.x, self.position.y, new_radius)
        self.split_roid_b = Asteroid(self.position.x, self.position.y, new_radius)
        self.split_roid_a.velocity = self.split_vector_a * 1.2
        self.split_roid_b.velocity = self.split_vector_b * 1.2