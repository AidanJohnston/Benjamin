import pygame
import Entity

class Platform(Entity.Entity):
    def __init__(self, group, x, y):

        super().__init__(group, x ,y)
        self.loadImages()
        self.changeAnimation('Platform')
        self.height = 32
        self.width = 32
    def loadImages(self):
        self.load_animation('Platform',1)
    def update(self):
        a = 1