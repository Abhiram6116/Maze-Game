import pygame,random,time
from maze import Maze
from kitty import Kitty
from clocks import Timer

# This file is to start game of type A

class TypeA:
    def startgame(m):
        # siz gives the size of blocks in the maze
        # (a,b) is the coordinate of the camera following player
        siz = 180
        a = -360
        b = -360

        # Initializing screen
        # setting mode such that 5x5 blocks of entire maze is visible at an instant
        screen = pygame.display.set_mode((900,1000))
        pygame.display.set_caption("Normal Maze Game")
        void= pygame.image.load('images/void.jpeg')
        pygame.display.set_icon(void)
        background2 = pygame.image.load('images/background2.jpg')
        background2 = pygame.transform.rotate(background2,90)
        background2 = pygame.transform.scale(background2,(900,1000))

        clock=pygame.image.load("images/clock.jpg")
        clock = pygame.transform.scale(clock, (50,50))
        portal = pygame.image.load("images/portal.gif")
        portal = pygame.transform.scale(portal, (siz/2,siz/2))

        ground1=pygame.image.load("images/ground1.png")
        ground1 = pygame.transform.scale(ground1, (siz,siz))
        ground2=pygame.image.load("images/ground2.jpeg")
        ground2 = pygame.transform.scale(ground2, (siz,siz))
        ground3=pygame.image.load("images/ground3.png")
        ground3 = pygame.transform.scale(ground3, (siz,siz))
        # This is to rantomly generate a ground image and its wall color
        colors={ground1:(73,55,27),ground2:(150,75,0), ground3:(145,154,158)}
        ground=random.choice([ground3,ground1,ground2])

        # This is to show goldcoins at status 2 places
        goldcoin1 = pygame.image.load('images/goldcoin1.png')
        goldcoin1 = pygame.transform.scale(goldcoin1,(siz/2,siz/2))
        goldcoin2 = pygame.image.load('images/goldcoin2.png')
        goldcoin2 = pygame.transform.scale(goldcoin2,(siz/2,siz/2))
        goldcoin3 = pygame.image.load('images/goldcoin3.png')
        goldcoin3 = pygame.transform.scale(goldcoin3,(siz/2,siz/2))
        goldcoin4 = pygame.image.load('images/goldcoin4.png')
        goldcoin4 = pygame.transform.scale(goldcoin4,(siz/2,siz/2))
        goldcoin5 = pygame.image.load('images/goldcoin5.png')
        goldcoin5 = pygame.transform.scale(goldcoin5,(siz/2,siz/2))
        goldcoin6 = pygame.image.load('images/goldcoin6.png')
        goldcoin6 = pygame.transform.scale(goldcoin6,(siz/2,siz/2))
        goldcoin7 = pygame.image.load('images/goldcoin7.png')
        goldcoin7 = pygame.transform.scale(goldcoin7,(siz/2,siz/2))
        goldcoin = [goldcoin1,goldcoin2,goldcoin3,goldcoin4,goldcoin5,goldcoin6,goldcoin7]

        kitty1 = pygame.image.load('images/kitty1.png')
        kitty1 = pygame.transform.scale(kitty1,(2*siz/5,siz/4))
        kitty2 = pygame.image.load('images/kitty2.png')
        kitty2 = pygame.transform.scale(kitty2,(2*siz/5,siz/4))
        kitty3 = pygame.image.load('images/kitty3.png')
        kitty3 = pygame.transform.scale(kitty3,(2*siz/5,siz/4))
        kitty4 = pygame.image.load('images/kitty4.png')
        kitty4 = pygame.transform.scale(kitty4,(2*siz/5,siz/4))
        kitty5 = pygame.image.load('images/kitty5.png')
        kitty5 = pygame.transform.scale(kitty5,(2*siz/5,siz/4))
        kitty6 = pygame.image.load('images/kitty6.png')
        kitty6 = pygame.transform.scale(kitty6,(2*siz/5,siz/4))
        kitty7 = pygame.image.load('images/kitty7.png')
        kitty7 = pygame.transform.scale(kitty7,(2*siz/5,siz/4))
        kitty8 = pygame.image.load('images/kitty8.png')
        kitty8 = pygame.transform.scale(kitty8,(2*siz/5,siz/4))
        liquidkitty = pygame.image.load('images/liquidkitty.png')
        liquidkitty = pygame.transform.scale(liquidkitty,(2*siz/5,siz/4))
        kitty0 = [kitty1,kitty2,kitty3,kitty4,kitty5,kitty6,kitty7,kitty8]
        kitty000 = kitty0[6]

        life1 = pygame.image.load('images/life1.png')
        life1 = pygame.transform.scale(life1,(siz/2,siz/2))
        life2 = pygame.image.load('images/life2.png')
        life2 = pygame.transform.scale(life2,(siz/2,siz/2))
        life3 = pygame.image.load('images/life3.png')
        life3 = pygame.transform.scale(life3,(siz/2,siz/2))

        obstacle = pygame.image.load('images/obstacle.png')
        obstacle = pygame.transform.scale(obstacle,(siz,siz))

        drain = pygame.image.load('images/drain.png')
        drain = pygame.transform.scale(drain,(siz,siz))

        catFood = pygame.image.load('images/catFood.png')
        catFood = pygame.transform.scale(catFood,(siz/2,siz/2))

        font1 = pygame.font.Font("fonts/generalFont.ttf",40)
        font2 = pygame.font.Font('fonts/generalFont.ttf',70)

        # Initializing class for Maze setting mxm as the dimensions
        maze=Maze(int(m),int(m),siz)
        # Initializing class for timer setting the argument as m
        timer= Timer(m)
        # Initializing Class for Player 
        kitty = Kitty(450,450,siz)
        # Generating a maze
        maze.mazeGenerator()
        # Initializing the timer
        timer.initiateTimer()
        # Setting initial score to Zero
        score=0

        test=1

        # Starting the game loop
        while test :
            pygame.draw.rect(screen,(0,0,0),[0,0,900,1000])
            screen.blit(background2,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # exiting the game
                    test=0
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: # Going back to menu
                        test=0
                        return 0
                    if event.key == pygame.K_ESCAPE: # Exiting the game
                        quit()
                    if event.key == pygame.K_SPACE: # Pausing the game
                        timer.pauseTimer()

                        text1 = font2.render('Game is paused',True,(255,0,0))
                        textRect1 = text1.get_rect()
                        textRect1.center=(450,500)
                        text2 = font1.render('SPACE to continue',True,(255,255,255))
                        textRect2 = text2.get_rect()
                        textRect2.center=(450,600)
                        text3 = font1.render('BACKSPACE for menu',True,(255,255,255))
                        textRect3 = text3.get_rect()
                        textRect3.center=(450,700)

                        run = 1
                        # Displaying the paused game window
                        while run:
                            pygame.draw.rect(screen,(0,0,0),[0,0,900,1000])
                            screen.blit(text1,textRect1)
                            screen.blit(text2,textRect2)
                            screen.blit(text3,textRect3)

                            for event2 in pygame.event.get():
                                if event2.type == pygame.QUIT: # Exiting the game
                                    quit()
                                if event2.type == pygame.KEYDOWN:
                                    if event2.key == pygame.K_BACKSPACE: # Going back to menu
                                        run = 0
                                        test = 0
                                        return 0
                                    if event2.key == pygame.K_SPACE: # Continuing the game
                                        run = 0
                                        timer.initiateTimer()
                                    if event2.key == pygame.K_ESCAPE: # Exiting the game
                                        quit()
                            pygame.display.update()

                    # Starting the Movement using LEFT,RIGHT,UP,DOWN OR A,D,W,S when button is pressed       
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        kitty.left = True
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        kitty.right = True
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        kitty.up = True
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        kitty.down = True
                    # controlling between run and walk
                    if event.key == pygame.K_RCTRL or event.key == pygame.K_r:
                        kitty.spdval = not kitty.spdval
                    # shifting kitty to liquid kitty
                    if event.key == pygame.K_RSHIFT or event.key == pygame.K_q:
                        if time.time()>=kitty.timer+5 and kitty.status == 0:
                            kitty.liquidPower()
                    # Making sure that player don't pass through walls or obstacles
                    kitty.movementLimits(maze.blocksList, siz,a,b,m)

                # Ending the Movement when the button is released 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        kitty.left = False
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        kitty.right = False
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        kitty.up = False
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        kitty.down = False
                    # Making sure that player don't pass through walls or obstacles
                    kitty.movementLimits(maze.blocksList, siz, a, b, m)

            # Printing the ground and walls
            for blocks in maze.blocksList:
                screen.blit(ground,(blocks.x*siz-a,blocks.y*siz-b))
                blocks.walls(screen,colors[ground],a,b)
            #Applying movement limits and checking for collision with obstacle while running
            collision = kitty.movementLimits(maze.blocksList,siz, a, b, m)

            #Liquid power expiring
            if time.time()>=kitty.timer+3 and kitty.status == 1:
                kitty.status = 0
                kitty.drainable = 0
                kitty.cooldown()

            # Changing the position of camera following player
            c=kitty.move(a,b)
            a=c[0]
            b=c[1]

            # making a time dependent random variable x
            x=int(10*time.time())
            y=x%7
            z=x%8

            for blocks in maze.blocksList:
                # Printing the portal at end of the maze
                if blocks.status == 1:
                    screen.blit(portal,(blocks.x*siz-a+siz/2,blocks.y*siz-b+siz/2))
                # Printing the GoldCoins at status 2 blocks
                if blocks.status==2:
                    screen.blit(goldcoin[y],(blocks.x*siz-a,blocks.y*siz-b))
                    # Player collecting the coins if he is on the coin and score is increased by 100 for every coin
                    if (blocks.x*siz<=kitty.x+a<=blocks.x*siz + siz/2) and (blocks.y*siz<=kitty.y+b<=blocks.y*siz+siz/2) and kitty.status == 0:
                        blocks.status=0
                        score = score+100
                if blocks.status==3:
                    # Creating the obstacle
                    screen.blit(obstacle,(blocks.x*siz-a,blocks.y*siz-b))
                if blocks.status==4:
                    # Creating the drain
                    screen.blit(drain,(blocks.x*siz-a,blocks.y*siz-b))
                if blocks.status==5:
                    # Creating the cat food
                    screen.blit(catFood,(blocks.x*siz-a,blocks.y*siz-b))
                    # player collecting the cat food if they are on the cat food and don't have maximum life
                    if (blocks.x*siz<=kitty.x+a<=blocks.x*siz + siz/2) and (blocks.y*siz<=kitty.y+b<=blocks.y*siz+siz/2) and kitty.status == 0 and kitty.life != 6:
                        blocks.status = 0
                        if kitty.life == 5:
                            kitty.life = 6
                        else :
                            kitty.life += 2

            kitty00 = kitty0[z]
            if kitty.status == 1:
                kitty00 = liquidkitty
                kitty000 = liquidkitty

            # Drawing the player on the screen
            if kitty.right == 1 :
                kitty000 = kitty0[6]
                if kitty.status==1:
                    kitty000 == liquidkitty
                if kitty.down == 1:
                    kitty00 = pygame.transform.rotate(kitty00,-45)
                    kitty000 = pygame.transform.rotate(kitty000,-45)
                    screen.blit(kitty00,(kitty.x-10,kitty.y-10))
                elif kitty.up == 1:
                    kitty00 = pygame.transform.rotate(kitty00,45)
                    kitty000 = pygame.transform.rotate(kitty000,45)
                    screen.blit(kitty00,(kitty.x-10,kitty.y-10))
                else:
                    screen.blit(kitty00,(kitty.x-10,kitty.y-10))
            elif kitty.left == 1 :
                kitty000 = kitty0[6]
                if kitty.status == 1:
                    kitty000 == liquidkitty
                kitty00 = pygame.transform.flip(kitty00,1,0)
                kitty000 = pygame.transform.flip(kitty000,1,0)

                if kitty.down == 1:
                    kitty00 = pygame.transform.rotate(kitty00,45)
                    kitty000 = pygame.transform.rotate(kitty000,45)
                    screen.blit(kitty00,(kitty.x-10,kitty.y-10))
                elif kitty.up == 1:
                    kitty000 = pygame.transform.rotate(kitty000,-45)
                    kitty00 = pygame.transform.rotate(kitty00,-45)
                    screen.blit(kitty00,(kitty.x-10,kitty.y-10))
                else:
                    screen.blit(kitty00,(kitty.x-10,kitty.y-10))
            elif kitty.up == 1:
                kitty000 = kitty0[6]
                if kitty.status == 1:
                    kitty000 = liquidkitty
                kitty00 = pygame.transform.rotate(kitty00,90)
                kitty000 = pygame.transform.rotate(kitty000,90)
                screen.blit(kitty00,(kitty.x-10,kitty.y-10))
            elif kitty.down == 1:
                kitty000 = kitty0[6]
                if kitty.status == 1:
                    kitty000 = liquidkitty
                kitty000 = pygame.transform.rotate(kitty000,-90)
                kitty00 = pygame.transform.rotate(kitty00,-90)
                screen.blit(kitty00,(kitty.x-10,kitty.y-10))
            else:
                screen.blit(kitty000,(kitty.x-10,kitty.y-10))

            # Losing half life when collided with obstacle while running in normal state
            if collision:
                kitty.life -= 1

            # Losing full life when went through the drain while being liquid
            if kitty.currentBlock((a+kitty.x)//siz,(b+kitty.y)//siz,maze.blocksList).status == 4 and kitty.drainable==1:
                kitty.life -= 2
                kitty.drainable = 0

            # Showing the lives of kitty left
            if kitty.life ==  6:
                lives = [life1,life1,life1]
            elif kitty.life == 5:
                lives = [life2,life1,life1]
            elif kitty.life == 4:
                lives = [life3, life1,life1]
            elif kitty.life == 3:
                lives = [life3,life2,life1]
            elif kitty.life == 2:
                lives = [life3,life3,life1]
            elif kitty.life == 1:
                lives = [life3,life3,life2]
            else:
                lives = [life3,life3,life3]

            screen.blit(lives[0],(600,40))
            screen.blit(lives[1],(700,40))
            screen.blit(lives[2],(800,40))
            
            # Showing the display Time
            displayTime = timer.displayTimer()
            if displayTime:
                textRect = displayTime.get_rect()
                textRect.center=(800,950)
                screen.blit(displayTime,textRect)
            # Printing clock beside the display time
            screen.blit(clock, (650,925))
            
            # Rendering texts to print at the bottom of the maze game
            text4=font1.render("SCORE:"+str(score),True,(255,255,255))
            textRect4 = text4.get_rect()
            textRect4.center=(100,950)
            text5=font1.render("SPACE to pause",True,(255,255,255))
            textRect5 = text5.get_rect()
            textRect5.center=(450,950)

            # Printing the texts
            screen.blit(text4,textRect4)
            screen.blit(text5,textRect5)

            # If lives are over, game stops
            if kitty.life <= 0:
                while test:
                    for event in pygame.event.get():
                        if event.type==pygame.QUIT: # Exiting the game
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE: # Going Back to menu
                                test=0
                            if event.key == pygame.K_ESCAPE: # Exiting the game
                                quit()
                    # Printing the popup window
                    pygame.draw.rect(screen,(0,0,0),[200,200,500,600])
                    pygame.draw.rect(screen,(100,100,100),[200,200,500,600],3)


            # If the time is up, game stops
            if int(timer.currentTime)>=int(timer.finalTime):
                pygame.draw.rect(screen,(0,0,0),[200,300,500,400])
                pygame.draw.rect(screen,(100,100,100),[200,300,500,400],3)
                text6=font2.render('OOPS!', True, (255, 255, 255))
                textRect6 = text6.get_rect()
                textRect6.center = (450,400)
                text7 = font2.render('Time is up', True, (255,255,255))
                textRect7 = text7.get_rect()
                textRect7.center=(450,500)
                text8=font1.render('BACKSPACE for menu', True, (255,255,255))
                textRect8 = text8.get_rect()
                textRect8.center=(450,600)

                run2 = 1
                # Starting the loop
                while run2:
                    # Making the window and printing text
                    pygame.draw.rect(screen,(0,0,0),[200,300,500,400])
                    pygame.draw.rect(screen,(100,100,100),[200,300,500,400],3)
                    screen.blit(text6,textRect6)
                    screen.blit(text7,textRect7)
                    screen.blit(text8,textRect8)

                    for event in pygame.event.get():
                        if event.type==pygame.QUIT: # Exiting the game
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE: # Going Back to menu
                                run2=0
                                test=0
                            if event.key == pygame.K_ESCAPE: # Exiting the game
                                quit()

                    pygame.display.update()
                return 0 # Returning 0 as the game is over
            
            # If the player reaches portal, the game is won
            if a>= m*180-450-siz/2 and b>=m*180-450-siz/2:
                while test:
                    # Printing the popup window
                    pygame.draw.rect(screen,(0,0,0),[150,100,600,800])
                    pygame.draw.rect(screen,(100,100,100),[150,100,600,800],3)

                    # Giving a 5x time bonus
                    TBonus=5*int(timer.finalTime-timer.currentTime)

                    # Giving a life bonus
                    LBonus = 100*kitty.life
                    totalScore=TBonus+LBonus+score

                    # Rendering the scoreBoard texts
                    text9 =font2.render('SCOREBOARD', True, (255,255,255))
                    textRect9=text9.get_rect()
                    textRect9.center=(450,200)
                    text10 = font1.render('Score : '+str(score), True,(255,255,255))
                    textRect10 = text10.get_rect()
                    textRect10.center=(450,300)
                    text14 = font1.render('Life Bonus : '+str(LBonus), True, (255,255,255))
                    textRect14 = text14.get_rect()
                    textRect14.center = (450,500)
                    text11 = font1.render('Time Bonus : '+str(TBonus),True,(255,255,255))
                    textRect11=text11.get_rect()
                    textRect11.center=(450,650)
                    text12 = font1.render('Total Score : '+str(totalScore),True,(255,255,255))
                    textRect12=text12.get_rect()
                    textRect12.center=(450,750)
                    text13 = font1.render('BACKSPACE for menu', True, (255,255,255))
                    textRect13 = text13.get_rect()
                    textRect13.center=(450,850)

                    # Printing the texts
                    screen.blit(text9,textRect9)
                    screen.blit(text10,textRect10)
                    screen.blit(text11,textRect11)
                    screen.blit(text12,textRect12)
                    screen.blit(text13,textRect13)
                    screen.blit(text14,textRect14)
                    screen.blit(lives[2],(250-45,550-25))
                    screen.blit(lives[1],(450-45,550-25))
                    screen.blit(lives[0],(650-45,550-25))

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: # Exiting the game
                            quit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_BACKSPACE: # Going back to menu
                                test=0
                                return totalScore
                            if event.key == pygame.K_ESCAPE: # Exiting the game
                                quit() 

                    # Printing the collected goldcoins on the scoreBoard
                    i=int(10*time.time())
                    j=i%7
                    k=0
                    goldcoin0 = goldcoin[j]
                    goldcoin0 = pygame.transform.scale(goldcoin0,(50,50))
                    while k < score/100:
                        if k < 5 :
                            screen.blit(goldcoin0,(450+(k-2)*100-25,350))
                        else:
                            screen.blit(goldcoin0,(450+(k-7)*100-25,450-30))
                        k += 1
                    pygame.display.update()

            pygame.display.flip()
            pygame.time.Clock().tick(60) # Setting the frame rate
