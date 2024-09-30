import pygame

# THIS IS TO PRINT LEADERBOARD WHEN SCORE BUTTON IS CLICKED

class Score:
    def leaderboard(screen,a,b):
        x=1
        # Fonts to be used
        font1=pygame.font.Font("fonts/generalFont.ttf",50)
        font2=pygame.font.Font("fonts/generalFont.ttf",30)
        # colors to be used
        colors=[(211,175,55),(145,154,158),(73,55,27),(255,255,255),(255,255,255)]

        text1=font1.render("LEADERBOARD", True, (0,0,255)) # Rendering "Leaderbord" as heading
        textRect1=text1.get_rect()
        textRect1.center=(a/2,b/4)

        text2=font2.render("BACKSPACE to go back", True, (255,255,255)) # rendering "backspace to go back" as keyboard index at bottom
        textRect2=text2.get_rect()
        textRect2.center=(a/2,4*b/5)

        while x:
            i=0
            # First opening the file "scoresorted.txt" which stores all the scores
            f=open("scoresorted.txt", "r")
            # drawing a  rectangular area over the screen to show leaderboard
            pygame.draw.rect(screen,(10,10,10),[a/2-2*a/9,b/2-b/3,4*a/9,2*b/3])
            pygame.draw.rect(screen,(100,100,100),[a/2-2*a/9,b/2-b/3,4*a/9,2*b/3],2,5)
            # Prinying the rendered texts
            screen.blit(text1,textRect1)
            screen.blit(text2,textRect2)
            #Applying the condition to print only top 5 scores
            while i < 5:
                j=str(i+1)

                line=f.readline().split(",")
                line[2]=line[2][:-1]
                #rendering the text containing (i+1)th score with appropriate color 
                text=font2.render(j+".     "+line[1]+"    "+line[2], True,colors[i])
                textRect=text.get_rect()
                textRect.center=(a/2,b/4+i*b/10+3*b/40)
                #printing the rendered text
                screen.blit(text,textRect)
                i=i+1
            f.close() # File is closed after the process

            # adjusting mouse controls such that when mouse is clicked outside the pop up surface, the pop up surface will be closed
            mouse=pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT: # To exit the game
                    x=0
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN: # keyboard control to go back
                    if event.key == pygame.K_BACKSPACE:
                        x=0
                if event.type == pygame.MOUSEBUTTONDOWN: # mouse control to go back
                    if mouse[0]<a/2-2*a/9 or mouse[0]>a/2+2*a/9 or mouse[1]<b/6 or mouse[1]>5*b/6:
                        x=0
            pygame.display.update() # display must be updated for every loop so that we can see the leaderboard
