import pygame
import Entity
class Collider():
    def __init__(self, group1, player):
        self.player = player
        self.obstacles = group1
    def checkAll(self):
        for wall in self.obstacles.getAll():
            top, bottom, left, right = self.collide(self.player, wall)
            if top:
                self.player.grounded = True
                self.player.move(0, ((self.player.rect.bottom) - wall.rect.top)) 
            else:
                self.player.grounded = False
    def collide(self, entity1, entity2):
        y = entity2.rect.height / 4
        x = entity2.rect.width / 4
        
        rL = pygame.Rect((entity2.rect.left),(entity2.rect.top + y),(x),(2*y))
        rR = pygame.Rect((entity2.rect.right-x),(entity2.rect.top + y),(x),(2*y))
        rT = pygame.Rect((entity2.rect.left + x),(entity2.rect.top),(2*x),(y))
        rB = pygame.Rect((entity2.rect.left + x),(entity2.rect.bottom - y),(2*x),(y))



        bL = rL.colliderect(entity1)
        bR = rR.colliderect(entity1)
        bT = rT.colliderect(entity1)
        bB = rB.colliderect(entity1)
        if (bL or bR or bT or bB):
            print("Something Collided")
        return (bL, bR, bT, bB)
    def manualCollide(self, entity1, entity2):
        if(entity1.rect.bottom >= entity2.rect.top and entity1.rect.top <= entity2.rect.bottom):
            print("Collide")
