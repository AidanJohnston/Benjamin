import pygame
import Visual
import Entity
import Samurai
import directions
import Platform
import Collider
import Bricks
import Dirt
import Background

SIZE = WIDTH, HEIGHT = 1200, 600 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 60 #Frames per second

def main():
    pygame.init()
    screen = pygame.display.set_mode(SIZE)
    d = directions.directions

    Terrain = Entity.EntityGroup(screen)
    players = Entity.EntityGroup(screen)
    background = Entity.EntityGroup(screen)
    
    level = [
             "",
             ""
             ]

    for x in range(0, 30):
        Dirt.build(64*x, 368, Terrain)


    for x in range(15, 20):
        Bricks.build(64*x, 208, Terrain)
    
    for y in range(1, 5):
        Bricks.build(672, 64*y, Terrain)

    for y in range(4, 8):
        Bricks.build(0, 64*y, Terrain)

    for x in range(0, 25):
        Background.build(128*x, 0, background)

    sam = Samurai.Samurai(50, 50, Collider.Collider(Terrain))

    players.add(sam)
    sam.setDirection(d.LEFT)

    clock = pygame.time.Clock()
 
    while True:
        
        screen.fill(BACKGROUND_COLOR)
        background.drawAll()
        background.updateAll()
        Terrain.updateAll()
        Terrain.drawAll()
        
        players.updateAll()
        players.drawAll()
        if(sam.EXIT):
            break
        pygame.display.update()
        clock.tick(FPS)
 
if __name__ == '__main__':
    main()
