import pygame
import random

# file to make blocks and generate maze

class Blocks:
    def __init__(self, x, y,siz):
        self.x = x
        self.y = y
        self.surr = { "n":1, "s":1, "e":1, "w":1}
        self.visited = 0
        self.status = 0
        self.siz = siz

    # Limiting the blocks to be from (0,0) to (m-1,n-1)
    def blocksLimiting(self, x, y, m, n, blocksList):
        if x<0 or x>m-1 or y<0 or y>n-1:
            return 0
        else:
            return blocksList[x+y*m]
    
    # Drawing walls all over the maze 
    def walls(self,screen,colors,a,b):
        x=self.x*self.siz - a
        y=self.y*self.siz - b
        if self.surr["n"]:
            pygame.draw.line(screen, colors, (x,y), (x+self.siz,y), int(self.siz/10))
        if self.surr["s"]:
            pygame.draw.line(screen, colors, (x,y+self.siz), (x+self.siz,y+self.siz), int(self.siz/10))
        if self.surr["e"]:
            pygame.draw.line(screen, colors, (x+self.siz,y), (x+self.siz,y+self.siz), int(self.siz/10))
        if self.surr["w"]:
            pygame.draw.line(screen, colors, (x,y), (x,y+self.siz), int(self.siz/10))
    
    #checking weather the neighboring block is visited or not and then returning a block randomly if it is not visited
    def surrStatus(self,m,n,blocksList):
        neighbors=[]
        north = self.blocksLimiting(self.x,self.y-1,m,n,blocksList)
        south = self.blocksLimiting(self.x,self.y+1,m,n,blocksList)
        east = self.blocksLimiting(self.x+1,self.y,m,n,blocksList)
        west = self.blocksLimiting(self.x-1,self.y,m,n,blocksList)
        if north and not north.visited:
            neighbors.append((north,"U"))
        if south and not south.visited:
            neighbors.append((south,"D"))
        if east and not east.visited:
            neighbors.append((east,"R"))
        if west and not west.visited:
            neighbors.append((west,"L"))
        return random.choice(neighbors) if neighbors else False

class Maze:
    def __init__(self, m, n,siz):
        self.m = m
        self.n = n
        self.siz=siz
        self.blocksList = [Blocks(m,n,siz) for n in range(self.n) for m in range(self.m)] # Making a list of Blocks
    
    # Removing the walls while generating the maze
    def removingWalls(self, current, next):
        a = current.x - next.x
        b = current.y - next.y
        if a == 1:
            current.surr["w"] = 0
            next.surr["e"] = 0
        elif a == -1:
            current.surr['e'] = 0
            next.surr['w'] = 0
        if b == 1:
            current.surr['n'] = 0
            next.surr['s'] = 0
        elif b == -1:
            current.surr['s'] = 0
            next.surr['n'] = 0

    # dfs method to generate maze
    def mazeGenerator(self):
        if self.m == 15:
            num = 5
            num2 = 3
        elif self.m == 20:
            num = 10
            num2 = 6
        elif self.m == 30:
            num = 20
            num2 = 9 
        current = [self.blocksList[0],0]
        blocksList=self.blocksList[1:-1]
        dfsOrder = []
        array = [[self.blocksList[0],0]]
        i=1
        self.blocksList[-1].status = 1
        while i != len(self.blocksList):
            current[0].visited = 1
            next = current[0].surrStatus(self.m,self.n,self.blocksList)
            if array[-1][0] != self.blocksList[-1]:
                if next:
                    array.append(next)
                else:
                    array.pop()
            if next:
                next[0].visited = 1
                i += 1
                dfsOrder.append(current)
                self.removingWalls(current[0],next[0])
                current=next
            elif dfsOrder:
                current = dfsOrder.pop()

        # generating a direct path for the maze
        k = 1
        path = []
        while k < len(array):
            path.append(array[k][1])
            k = k + 1
        f = open('path.txt','w')
        for x in path:
            f.write(x+", ")
        f.close()

        # Changing status of blocks so that they contain goldcoins
        j=0
        while j < 10:
            c=random.choice(blocksList)
            c.status=2
            blocksList.remove(c)
            j += 1

        # Changing status of blocks so that they contain obstacles
        l=0
        while l < num:
            c = random.choice(blocksList)
            c.status = 3
            blocksList.remove(c)
            l += 1
    
        # Changing status of blocks so that they contain drain
        n=0
        while n < num:
            c = random.choice(blocksList)
            c.status = 4
            blocksList.remove(c)
            n += 1
        
        # Changing status of blocks so that yhey contain extra lives if needed
        o = 0
        while o < num2:
            c = random.choice(blocksList)
            c.status = 5
            blocksList.remove(c)
            o += 1

        return blocksList
