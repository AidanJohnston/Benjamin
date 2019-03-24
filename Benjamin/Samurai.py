import pygame
import Visual
import Entity
import directions
import sys

false = False
true = True

KEY_W = 119
KEY_A = 97
KEY_S = 115
KEY_D = 100
d = directions.directions


class Samurai(Entity.Entity):
    def __init__(self, x, y, collider):

        super().__init__(x ,y, 64, 64)

        
        self.maxJumps = 4
        self.jumps = self.maxJumps
        self.groundAccel = 4
        self.maxSpeed = 16
        self.jumpPower = 13
        self.groundDecel = 8
        self.airAccel = 2
        self.slideAccel = 1

        self.jumpPressed = False
        self.leftPressed = False
        self.rightPressed = False
        self.downPressed = False
        self.upPressed = False
        self.EXIT = False

        self.moveDirection = d.none
        self.frictionToggle = False

        self.yVelo = 0
        self.xVelo = 0
        
        self.jumpY = 0
        self.jumpX = 0


        self.grounded = False
        self.running = False
        self.direction = d.none
        self.sliding = False

        self.grabbing = False
        self.grabbed = False
        self.grabTime = 0
        self.grabDirection = d.none


        self.collider = collider

        self.loadAnimations()
        self.changeAnimation('Samurai_idle_right')
        
        
    def loadAnimations(self):
        self.load_animation('Samurai_idle_left', 15)
        self.load_animation('Samurai_idle_right', 15)
        self.load_animation('Samurai_idle_forward', 15)
        self.load_animation('Samurai_idle_backwords', 15)
        self.load_animation('Samurai_falling_left', 4)
        self.load_animation('Samurai_falling_right', 4)
        self.load_animation('Samurai_run_left', 8)
        self.load_animation('Samurai_run_right', 8)
        self.load_animation('Samurai_sliding_right', 4)
        self.load_animation('Samurai_sliding_left', 4)


    def setMoveDirection(self, direction):
        self.moveDirection = direction
    def fixAnimation(self):

        if (self.grounded == True):
            if self.running == True:
                if(self.sliding == False):
                    if self.moveDirection == d.left:
                        self.changeAnimation('Samurai_run_left')
                    if self.moveDirection == d.right:
                        self.changeAnimation('Samurai_run_right')
                if(self.sliding == True):
                    if self.moveDirection == d.left:
                        self.changeAnimation('Samurai_sliding_left')
                    if self.moveDirection == d.right:
                        self.changeAnimation('Samurai_sliding_right')
            if self.running == False:
                if self.sliding == False:
                    if self.direction == d.left:
                        self.changeAnimation('Samurai_idle_left')
                    if self.direction == d.right:
                        self.changeAnimation('Samurai_idle_right')
                if self.sliding == True:
                    if self.direction == d.left:
                        self.changeAnimation('Samurai_sliding_left')
                    if self.direction == d.right:
                        self.changeAnimation('Samurai_sliding_right')
        if (self.grounded == False):
            if self.direction == d.left:
                self.changeAnimation('Samurai_falling_left')
            if self.direction == d.right:
                self.changeAnimation('Samurai_falling_right')
                
    def setDirection(self, direction): # set the direction of the samurai

        self.direction = direction
        
    def jump(self):
        if(self.jumps > 1):
            print("HOP")
            self.jumps = self.jumps - 1
            if(self.grabbed == False):
                print("NOT GRABBED BUT JUMPING ANYWAYS")
            #self.yVelo =  -1*self.jumpPower
            #self.grounded = False
                self.jumpY = -1 * self.jumpPower
            if(self.grabbed == True):
                
                self.grabbed = False
                self.grabTime -= 30
                if(self.grabTime < 0):
                    self.grabTime = 0
                self.jumpY = -1 * self.jumpPower
                if(self.grabDirection == d.right):
                    print("WALLJUMP LEFT")
                    self.jumpX = -1 * self.jumpPower
                #self.setMoveDirection(d.left)
                if(self.grabDirection == d.left):
                    print("WALLJUMP RIGHT")
                    self.jumpX = self.jumpPower
                self.grabDirection = d.none
                #self.setMoveDirection(d.right)#Remove this once acceleration is in


    def update(self):
        super().update()
        self.updateKeys()
        self.doMovement()
        self.fixAnimation()

    def doMovement(self):

        dir = 0
        if self.moveDirection == d.LEFT:
            dir = -1
        if self.moveDirection == d.RIGHT:
            dir = 1

        if(self.grounded == True):
            if(self.sliding == False):
                accel = self.groundAccel * dir
            if(self.sliding == True):
                if self.xVelo == 0:
                    accel = 0
                else:
                    accel = 0
                    if(self.frictionToggle == True):#make friction occur every other tick so you can slider farther
                        accel = -1 * dir * self.slideAccel
                    self.frictionToggle = not(self.frictionToggle)

                        
        if(self.grounded == False):
            accel = self.airAccel * dir

        #determine movement conditions in x

        print(self.sliding)

        if(self.grabbed == False):
            if(self.grabTime < 60):
                self.grabTime = self.grabTime + 1
    
        if(self.grabbed == True):
            self.grabTime = self.grabTime - 1
            self.jumps = self.maxJumps -1
            if (self.grabTime <= 0):
                self.grabbed = False
                self.grabDirection = d.none
                print("SLIPPED")
            if (self.moveDirection != self.grabDirection):
                self.grabbed = False
        #print(self.grabbed)
        #determine movement conditions in y

        if(accel == 0 and self.sliding == False and self.grounded == True):
            if(self.xVelo >0):
                self.xVelo = self.xVelo - self.groundDecel
                if(self.xVelo < 0):
                    self.xVelo = 0
            if(self.xVelo < 0):
                self.xVelo = self.xVelo + self.groundDecel
                if(self.xVelo > 0):
                    self.xVelo = 0
        #decelerate if applicable

        self.xVelo = self.xVelo + accel
        if(self.jumpX != 0):
            self.xVelo = self.jumpX
            self.jumpX = 0

        if(abs(self.xVelo) > self.maxSpeed):
            if(self.xVelo <0):
                self.xVelo = -1*self.maxSpeed
            if(self.xVelo >0):
                self.xVelo = 1*self.maxSpeed  
        #accelerate in x
        
        
        if(self.grounded == False and self.grabbed == False):
            self.yVelo += 1 #apply gravity
        if(self.grounded == True):
            self.jumps = self.maxJumps
        if(self.grabbed == True):
            self.yVelo = 0
        if(self.jumpY != 0):
            self.yVelo = self.jumpY
            self.jumpY = 0
        #accelerate in y


        if(abs(self.yVelo) >15):# limit yVelo
            if(self.yVelo > 0):
                self.yVelo = 15
            if(self.yVelo <0):
                self.yVelo = -15


        groundedFlag = False #assume not on ground to start

        if(self.xVelo != 0):
            self.move(self.xVelo, 0)#move in x first
            if self.collider.doCollision(self, self.xVelo, 0):
                groundedFlag = True

        if(self.yVelo != 0):
            self.move(0, self.yVelo)#then move in y
            if self.collider.doCollision(self, 0,self.yVelo):
              groundedFlag = True

        self.grounded = groundedFlag

    def updateKeys(self):
        pygame.event.pump()#give it a lil' pump
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.fixDirection(d.LEFT, True)
                if event.key == pygame.K_d:
                    self.fixDirection(d.RIGHT, True)
                if event.key == pygame.K_s:
                    self.sliding = True
                    #self.fixDirection(d.DOWN, True)
                if event.key == pygame.K_w:
                    self.grabbing = True
                if event.key == pygame.K_SPACE:
                    
                    if (self.jumpPressed == False):
                        print("S P A C E   B A R")
                        self.jump()
                    self.jumpPressed = True
                if event.key == pygame.K_ESCAPE:
                    self.EXIT = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.fixDirection(d.LEFT, False)
                if event.key == pygame.K_d:
                    self.fixDirection(d.RIGHT, False)
                if event.key == pygame.K_s:
                    self.sliding = False
                    #self.fixDirection(d.DOWN, False)
                if event.key == pygame.K_w:
                    self.grabbing = False
                    self.grabbed = False
                    print("LET GO")
                if event.key == pygame.K_SPACE:
                    self.jumpPressed = False

    
    
    def fixDirection(self, direction, down):
        if down == True:
            self.setDirection(direction)
            
            if direction == d.LEFT:
                self.leftPressed = True
                self.setMoveDirection(direction)
            if direction == d.RIGHT:
                self.rightPressed = True
                self.setMoveDirection(direction)
            if direction == d.DOWN:
                self.downPressed = True
            if direction == d.UP:
                self.upPressed = True
        if down == False:
            if direction == d.LEFT:
                self.leftPressed = False
                self.setMoveDirection(d.NONE)
                if self.rightPressed == True:
                    self.setDirection(d.RIGHT)
                    self.setMoveDirection(d.RIGHT)
            if direction == d.RIGHT:
                self.rightPressed = False
                self.setMoveDirection(d.NONE)
                if self.leftPressed == True:
                    self.setDirection(d.LEFT)
                    self.setMoveDirection(d.LEFT)
            if direction == d.UP:
                self.upPressed = False
                if self.downPressed == True:
                    self.setDirection(d.DOWN)
            if direction == d.DOWN:
                self.downPressed = False
                if self.upPressed == True:
                    self.setDirection(d.UP)
        if self.leftPressed == False:
            if self.rightPressed == False:
                if self.upPressed == False:
                    if self.downPressed == False:
                        a = 1
        #rationalize animation variables
        
        if self.moveDirection == d.none:
            self.running = False
        else:
            self.running = True