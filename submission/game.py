import pygame
from leaderboard import Score
from levelSelection import Level
from typeA import TypeA
from typeB import TypeB
from scoreSorting import Sorting

pygame.init()
pygame.font.init()
a=900
b=900
screen=pygame.display.set_mode((a,b)) # creating the window of 900*900

pygame.display.set_caption("Lost in the Void") # Title

void = pygame.image.load("images/void.jpeg") # icon image
pygame.display.set_icon(void)

background = pygame.image.load("images/background.jpg") # Background image
background = pygame.transform.scale(background,(1000,900))
#Different fonts to be used
font1=pygame.font.Font("fonts/headingFont.otf",80) # Downloaded from google
font2=pygame.font.Font("fonts/generalFont.ttf", 50)
font3=pygame.font.Font("fonts/generalFont.ttf", 30)

text1=font1.render("LOST IN THE VOID", True, (150,20,20)) # Rendering Heading
textRect1=text1.get_rect()
textRect1.center = (a/2,b/4)

text2=font2.render("START",True,(255,255,255)) # Rendering start button to start the game and ask for difficulty
textRect2=text2.get_rect()
a2=text2.get_width()
b2=text2.get_height()
textRect2.center = (a/4,b/2)

text3=font2.render("SCORE", True, (255,255,255)) # Rendering Score button to show leaderboard
textRect3=text3.get_rect()
a3=text3.get_width()
b3=text3.get_height()
textRect3.center = (a/2,b/2)

text4 = font2.render("QUIT", True, (255,255,255)) # rendering quit button to quit the game
textRect4=text4.get_rect()
a4=text4.get_width()
b4=text4.get_height()
textRect4.center=(3*a/4,b/2)

text5 = font3.render("START-SPACE  SCORE-BACKSPACE  QUIT-ESCAPE", True, (255,255,255)) # index for keyboard controls
textRect5=text5.get_rect()
textRect5.center=(a/2,3*b/4)

test= True 
# initiating the loop
while test: 
    screen.blit(background,(0,0)) # First putting the background
    mouse = pygame.mouse.get_pos() # To get the position of mouse
    
    # To make the start button chande color when mouse is on the button
    if a/4-a2/2-5<= mouse[0] <= a/4+a2/2+5 and b/2-b2/2 -55<= mouse[1] <= b/2+b2/2+5: 
        pygame.draw.rect(screen,(255, 255, 255),[a/4-a2/2-15,b/2-b2/2-15,a2+30,b2+30])  
        text2=font2.render("START", True, (100,100,100))      
    else: 
        pygame.draw.rect(screen,(255, 255, 255),[a/4-a2/2-15,b/2-b2/2-15,a2+30,b2+30],2)
        text2=font2.render("START", True, (255,255,255))

    # To make the score button change color when mouse is on the button
    if a/2-a3/2-5 <= mouse[0] <= a/2+a3/2+5 and b/2-b3/2-5 <= mouse[1] <= b/2+b3/2+5: 
        pygame.draw.rect(screen,(255, 255, 255),[a/2-a3/2-15,b/2-b3/2-15,a3+30,b3+30]) 
        text3=font2.render("SCORE", True, (100,100,100))
    else: 
        pygame.draw.rect(screen,(255, 255, 255),[a/2-a3/2-15,b/2-b3/2-15,a3+30,b3+30],2)
        text3=font2.render("SCORE", True, (255,255,255))

    # To make the quit button change color when mouse is on it
    if 3*a/4-a4/2-5 <= mouse[0] <= 3*a/4+a4/2+5 and b/2-b4/2-5 <= mouse[1] <= b/2+b4/2+5: 
        pygame.draw.rect(screen,(255, 255, 255),[3*a/4-a4/2-15,b/2-b4/2-15,a4+30,b4+30])
        text4=font2.render("QUIT", True, (100,100,100))   
    else: 
        pygame.draw.rect(screen,(255, 255, 255),[3*a/4-a4/2-15,b/2-b4/2-15,a4+30,b4+30],2)
        text4=font2.render("QUIT", True, (255,255,255))

    #printing all the texts over background
    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)
    screen.blit(text3, textRect3)
    screen.blit(text4, textRect4)
    screen.blit(text5, textRect5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # To quit the game by pressing cross
            test = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN: # To use mouse controls for clicking buttons
            # THE START BUTTON
            if a/4-a2/2-5<= mouse[0] <= a/4+a2/2+5 and b/2-b2/2 -55<= mouse[1] <= b/2+b2/2+5:
                # LEVEL SELECTION
                lvl=Level.popup(a,b,screen)
                # Setting maze size with difficulty
                if lvl[1] == '1':
                    m = 15
                elif lvl[1] == '2':
                    m = 20
                elif lvl[1] == '3':
                    m = 30
                # Choosing Type of Maze
                if lvl[0] == 'A':
                    blah=TypeA.startgame(m)
                    screen = pygame.display.set_mode((900,900))
                    sorting=Sorting()
                    if blah:
                        Sorting.Sort(sorting,lvl,blah)
                elif lvl[0] == 'B':
                    TypeB.startgame(screen)
                    screen = pygame.display.set_mode((900,900))
            # THE SCORE BUTTON
            elif a/2-a3/2-5 <= mouse[0] <= a/2+a3/2+5 and b/2-b3/2-5 <= mouse[1] <= b/2+b3/2+5:
                Score.leaderboard(screen,a,b) # leaderboard funtion from leaderboard.py file to get leaderboard
            # THE QUIT BUTTON 
            elif 3*a/4-a4/2-5 <= mouse[0] <= 3*a/4+a4/2+5 and b/2-b4/2-5 <= mouse[1] <= b/2+b4/2+5: 
                test=0
                pygame.quit()
                quit() # Game has been exited

        # Using keyboard to control
        if event.type == pygame.KEYDOWN:
            # THE START BUTTON
            if event.key == pygame.K_SPACE:
                lvl=Level.popup(a,b,screen)
                if lvl[1] == '1':
                    m = 15
                elif lvl[1] == '2':
                    m = 20
                elif lvl[1] == '3':
                    m = 30
                if lvl[0] == 'A':
                    blah=TypeA.startgame(m)
                    screen = pygame.display.set_mode((900,900))
                    sorting=Sorting()
                    if blah:
                        Sorting.Sort(sorting,lvl,blah)
                elif lvl[0] == 'B':
                    TypeB.startgame(screen)
                    screen = pygame.display.set_mode((900,900))
            # THE EXIT BUTTON
            elif event.key == pygame.K_ESCAPE: 
                test=0
                pygame.quit()
                quit() # Exit the game
            # THE SCORE BUTTON
            elif event.key == pygame.K_BACKSPACE:
                Score.leaderboard(screen,a,b) # leaderboard funtion from leaderboard.py file to get leaderboard
    pygame.display.update() # updating the screen