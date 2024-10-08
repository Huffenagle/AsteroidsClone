import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quit game...")
                return
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            print("Exited via escape...")
            sys.exit()
            
        for game_obj in updatable:
            game_obj.update(dt)

        for asteroid in asteroids:
            if asteroid.detect_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.detect_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill((0,0,0))

        for game_obj in drawable:
            game_obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()