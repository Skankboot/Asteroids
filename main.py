import pygame
import constants
import player
import asteroid, asteroidfield
import sys
from constants import * # type: ignore

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # type: ignore
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    player.Player.containers = (updateable, drawable)
    asteroid.Asteroid.containers = (asteroids, updateable, drawable)
    asteroidfield.AsteroidField.containers = (updateable)
    my_guy = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    field = asteroidfield.AsteroidField()

    fps_timer = pygame.time.Clock()
    dt = 0

        

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       
        updateable.update(dt)

        for rock in asteroids:
            if rock.collision(my_guy) == True:
                print ("Game over!")
                sys.exit()

        screen.fill((0,0,0))

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = (fps_timer.tick(60))/1000
        
    
if __name__ == "__main__":
    main()