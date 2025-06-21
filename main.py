import pygame, constants, player
from constants import *

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_guy = player.Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)

    fps_timer = pygame.time.Clock()
    dt = 0
        

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill((0,0,0))
        my_guy.draw(screen)
        pygame.display.flip()

        dt = (fps_timer.tick(60))/1000
        
    

if __name__ == "__main__":
    main()