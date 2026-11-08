import pygame
import sys
from constants import *
from logger import log_state
from player import *
from asteroid import *
from asteroidfield import *
from logger import log_event
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")
    clock=pygame.time.Clock()
    dt=0.0
    
    
    updatable=pygame.sprite.Group() #holds objects that can be updated
    drawable=pygame.sprite.Group()  #holds objects that can be drawn
    Player.containers=(updatable,drawable)

   
    asteroids=pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    

    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroidfield=AsteroidField()

    shots=pygame.sprite.Group()
    Shot.containers=(shots,updatable,drawable)


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #drawable.draw(screen)
        for obj in drawable:
            obj.draw(screen)

        updatable.update(dt)

        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        #print(dt)

        



if __name__ == "__main__":
    main()
