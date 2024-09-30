import pygame, time

pygame.font.init()

#To set the timer

class Timer:
    def __init__(self,m):
        if m==15:
            self.finalTime = 180 # 3 minutes for difficulty 1
        elif m==20:
            self.finalTime = 360 # 6 minutes for difficulty 2
        elif m==30:
            self.finalTime = 480 # 8 minutes for difficulty 3
        self.currentTime = 0
        self.initialTime = 0
        self.pausedTime = 0
        self.font = pygame.font.Font("fonts/generalFont.ttf", 50)


    def initiateTimer(self):
        self.initialTime += time.time()-self.pausedTime # starting the timer initially or continuing it after every pause


    def pauseTimer(self):
        self.pausedTime = time.time() # pausing the timer


    def displayTimer(self):
        if self.currentTime <= self.finalTime:
            self.currentTime = time.time()-self.initialTime # stopping the timer to exceed time limit
        timeDiff=self.finalTime-self.currentTime
        secs=int(timeDiff%60) # secs to be displayed
        mins=int(timeDiff/60) # mins to be displayed
        displayTime = self.font.render(f"{mins:02}:{secs:02}", True, (255,255,255)) # total time to be displayed
        if self.currentTime > self.finalTime:
            return 0 # if timelimit is reached nothing is returned
        else:
            return displayTime # else displaytime is returned