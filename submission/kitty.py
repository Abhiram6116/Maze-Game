import pygame, time

# This file is to update player position and control speed
class Kitty:
    def __init__(self, x, y,siz):
        self.x = int(x)
        self.y = int(y)
        self.siz=siz
        self.color = (255,255,255)
        self.xspeed = 0
        self.yspeed = 0
        self.up = 0
        self.down = 0
        self.right = 0
        self.left = 0
        self.spdval=0
        self.spd = 10
        self.status = 0
        self.timer = 0
        self.life = 6
        self.drainable = 0

    # Getting the cordinates of current block
    def currentBlock(self,x,y,blocksList):
        for block in blocksList:
            if block.x == x and block.y == y:
                return block
    def liquidPower(self):
        self.status = 1
        self.drainable = 1
        self.spdval = 1
        self.timer = time.time()
    def cooldown(self):
        self.spdval = 0
        self.timer = time.time()
            
    # Stopping the player from going through walls and detecting collision with obstacle while running
    def movementLimits(self, blocksList,siz,a,b,m):
        collision = 0
        block = self.currentBlock((a+self.x)//siz,(b+self.y)//siz,blocksList)
        blockAbsX, blockAbsY = block.x*siz-a,block.y*siz-b

        if self.left:
            if block.surr['w'] or (self.status == 0 and block.blocksLimiting(block.x-1,block.y,m,m,blocksList).status == 3) :
                if self.x <= blockAbsX + siz/10:
                    self.left = 0
                    if block.blocksLimiting(block.x-1,block.y,m,m,blocksList):
                        if self.spdval == 1 and self.status == 0 and block.blocksLimiting(block.x-1,block.y,m,m,blocksList).status == 3 and not block.surr['w']:
                            collision = 1
        if self.right:
            if block.surr['e'] or (self.status == 0 and block.blocksLimiting(block.x+1,block.y,m,m,blocksList).status == 3) :
                if self.x >= blockAbsX + siz - siz/10-siz/4:
                    self.right = 0
                    if block.blocksLimiting(block.x+1,block.y,m,m,blocksList):
                        if self.spdval == 1 and self.status == 0 and block.blocksLimiting(block.x+1,block.y,m,m,blocksList).status == 3 and not block.surr['e']:
                            collision = 1
        if self.up:
            if block.surr['n'] or (self.status == 0 and block.blocksLimiting(block.x,block.y-1,m,m,blocksList).status == 3) :
                if self.y <= blockAbsY + siz/10:
                    self.up = 0
                    if block.blocksLimiting(block.x,block.y-1,m,m,blocksList):
                        if self.spdval == 1 and self.status == 0 and block.blocksLimiting(block.x,block.y-1,m,m,blocksList).status == 3 and not block.surr['n']:
                            collision = 1
        if self.down:
            if block.surr['s'] or (self.status == 0 and block.blocksLimiting(block.x,block.y+1,m,m,blocksList).status == 3) :
                if self.y >= blockAbsY + siz - siz/10 - siz/4:
                    self.down = 0
                    if block.blocksLimiting(block.x,block.y+1,m,m,blocksList):
                        if self.spdval == 1 and self.status == 0 and block.blocksLimiting(block.x,block.y+1,m,m,blocksList).status == 3 and not block.surr['s']:
                            collision = 1
        return collision

    # changing speed of players according to the buttons pressed or changing the position of camera to follow player
    def move(self,a,b):
        self.xspeed = 0
        self.yspeed = 0
        if self.left and not self.right :
            self.xspeed = -(self.spd+self.spdval*10)
        if self.right and not self.left :
            self.xspeed = (self.spd+self.spdval*10)
        if self.up and not self.down :
            self.yspeed = -(self.spd+self.spdval*10)
        if self.down and not self.up:
            self.yspeed = (self.spd+self.spdval*10)
        a = a + self.xspeed
        b = b + self.yspeed
        self.rect = pygame.Rect(int(self.x), int(self.y), self.siz/4, self.siz/4)
        return [a,b]
        