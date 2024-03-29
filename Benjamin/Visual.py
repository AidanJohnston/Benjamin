import pygame

def getImageByName(name, count):
    filename = getPath(name, count)
    return pygame.image.load(filename)

def getPath(name, index):
    filename = name + '/' + name + str(index) + '.png'
    return filename

class Animation(pygame.sprite.Sprite):
    def __init__(self, name, count, x, y, rect):
        super(Animation, self).__init__()
        self.count = count
        self.name = name
        self.images = []
        self.imagepaths = []
        self.index = 0
        self.loadImages()
        self.image = self.images[self.index]
        self.rect = rect
        self.frameCount = 0

    def loadImages(self):
        for i in range(1, self.count + 1):
            self.images.append(getImageByName(self.name, i))
            self.imagepaths.append(getPath(self.name, i))

    def update(self):
        return
    def resize(self, width, height):
        self.rect.width = width
        self.rect.height = height
    def nextFrame(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

    def move(self, dx, dy):
        self.rect = self.rect.move(dx, dy)

    def moveTo(self, x,y):
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        pygame.sprite.Sprite.draw(self)

