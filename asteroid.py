import pygame, random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        vel1 = self.velocity
        rot1 = vel1.rotate(angle)
        vel2 = self.velocity
        rot2 = vel2.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_ast_1 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast_1.velocity = rot1 * 1.2
        new_ast_2 = Asteroid(self.position.x, self.position.y, new_rad)
        new_ast_2.velocity = rot2 * 1.2