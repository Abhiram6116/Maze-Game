import pygame

# This file gives the pop-up window for level selection

class Level:
    def popup(a,b,screen):
        x=1
        # Fonts to be used
        font1=pygame.font.Font("fonts/generalFont.ttf",60)
        font2=pygame.font.Font("fonts/generalFont.ttf",30)
        # Colors to be used
        colors = [(0,0,0), (211,175,55), (255,255,255)]

        text=font1.render("LEVEL", True, (255,255,255)) # Rendering "level" as heading
        textRect=text.get_rect()
        textRect.center=(a/2,b/2-5*b/18+b/20)

        text1=font2.render("TYPE", True, (255,255,255)) # Rendering "type" as sub-heading
        textRect1=text1.get_rect()
        textRect1.center=(a/2,b/2-5*b/18+b/10)

        text2=font2.render("DIFFICULTY", True, (255,255,255)) # Rendering "difficulty" as sub-heading
        textRect2=text2.get_rect()
        textRect2.center=(a/2,b/2)

        text3=font1.render("A",True,colors[1])  # Rendering "A" as an option in types
        textRect3=text3.get_rect()
        a1=text3.get_width()
        b1=text3.get_height()
        textRect3.center = (a/3,5*b/12-10)

        text4=font1.render("B", True, (255,255,255)) # Rendering "B" as as option in types
        textRect4=text4.get_rect()
        a2=text4.get_width()
        b2=text4.get_height()
        textRect4.center = (2*a/3,5*b/12-10)

        text5 = font1.render("1", True, colors[1]) # Rendering "1" as an option in difficulty
        textRect5=text5.get_rect()
        a3=text5.get_width()
        b3=text5.get_height()
        textRect5.center=(a/4,7*b/12)

        text6 = font1.render("2", True, colors[2]) # Rendering "2" as an option in difficulty
        textRect6=text6.get_rect()
        a4=text6.get_width()
        b4=text6.get_height()
        textRect6.center=(a/2,7*b/12)

        text7 = font1.render("3", True, colors[2]) # Rendering "3" as an option in difficulty
        textRect7=text7.get_rect()
        a5=text7.get_width()
        b5=text7.get_height()
        textRect7.center=(3*a/4,7*b/12)
 
        text8 = font2.render("SPACE to continue",True,(255,255,255)) # Rendering index for keyboard control
        textRect8=text8.get_rect()
        textRect8.center=(a/2,2*b/3)

        text9 = font2.render("BACKSPACE to go back", True, colors[2]) # Rendering index for keyboard control
        textRect9 = text9.get_rect()
        textRect9.center=(a/2,b/2+5*b/18-b/20)

        # setting default initial conditions as type A, Difficulty 1
        T="A"
        D='1'
 
        # Initiating the loop
        while x:
            # Drawing rectangular surface for popup
            pygame.draw.rect(screen,(0,0,0),[a/2-a/3,b/2-5*b/18,2*a/3,5*b/9])
            pygame.draw.rect(screen,(255,255,255),[a/2-a/3,b/2-5*b/18,2*a/3,5*b/9],4)
            # printing the text over the rectangular surface
            screen.blit(text,textRect)
            screen.blit(text1,textRect1)
            screen.blit(text2,textRect2)
            screen.blit(text8,textRect8)
            screen.blit(text9,textRect9)

            # For mouse controls
            mouse=pygame.mouse.get_pos()

            # Drawing rectangle around the buttons
            # Color changing of type A button when mouse is on the button or when button is clicked
            if a/3-a1/2 <= mouse[0] <= a/3+a1/2 and 5*b/12-10-b1/2<= mouse[1] <= 5*b/12-10+b1/2:
                pygame.draw.rect(screen,colors[2],[a/3-a1/2-5,5*b/12-15-b1/2,a1+10,b1+10],0,3)
                text3=font1.render("A",True,colors[0])
            elif T=='A':
                pygame.draw.rect(screen,colors[1],[a/3-a1/2-5,5*b/12-15-b1/2,a1+10,b1+10],2,3)
                text3=font1.render('A',True,colors[1])
            else:
                pygame.draw.rect(screen,colors[2],[a/3-a1/2-5,5*b/12-15-b1/2,a1+10,b1+10],2,3)
                text3=font1.render('A',True,colors[2])

            # Color changing of type B button when mouse is on the button or when button is clicked
            if 2*a/3-a2/2 <= mouse[0] <= 2*a/3+a2/2 and 5*b/12-10-b2/2<= mouse[1] <= 5*b/12-10+b2/2:
                pygame.draw.rect(screen,colors[2],[2*a/3-a2/2-5,5*b/12-15-b2/2,a2+10,b2+10],0,3)
                text4=font1.render("B",True,colors[0])
            elif T=='B':
                pygame.draw.rect(screen,colors[1],[2*a/3-a2/2-5,5*b/12-15-b2/2,a2+10,b2+10],2,3)
                text4=font1.render('B',True,colors[1])
            else:
                pygame.draw.rect(screen,colors[2],[2*a/3-a2/2-5,5*b/12-15-b2/2,a2+10,b2+10],2,3)
                text4=font1.render('B',True,colors[2])

            # Color changing of difficulty 1 button when mouse is on the button or when button is clicked
            if a/4-a3/2 <= mouse[0] <= a/4+a3/2 and 7*b/12-b3/2<= mouse[1] <= 7*b/12+b3/2:
                pygame.draw.rect(screen,colors[2],[a/4-a3/2-5,7*b/12-5-b3/2,a3+10,b3+10],0,3)
                text5=font1.render("1",True,colors[0])
            elif D=='1':
                pygame.draw.rect(screen,colors[1],[a/4-a3/2-5,7*b/12-b3/2-5,a3+10,b3+10],2,3)
                text5=font1.render('1',True,colors[1])
            else:
                pygame.draw.rect(screen,colors[2],[a/4-a3/2-5,7*b/12-b3/2-5,a3+10,b3+10],2,3)
                text5=font1.render('1',True,colors[2])

            # Color changing of difficulty 2 button when mouse is on the button or when button is clicked
            if 2*a/4-a4/2 <= mouse[0] <= 2*a/4+a4/2 and 7*b/12-b4/2<= mouse[1] <= 7*b/12+b4/2:
                pygame.draw.rect(screen,colors[2],[2*a/4-a4/2-5,7*b/12-b4/2-5,a4+10,b4+10],0,3)
                text6=font1.render("2",True,colors[0])
            elif D=='2':
                pygame.draw.rect(screen,colors[1],[2*a/4-a4/2-5,7*b/12-b4/2-5,a4+10,b4+10],2,3)
                text6=font1.render('2',True,colors[1])
            else:
                pygame.draw.rect(screen,colors[2],[2*a/4-a4/2-5,7*b/12-b4/2-5,a4+10,b4+10],2,3)
                text6=font1.render('2',True,colors[2])

            # Color changing of difficulty 3 button when mouse is on the button or when button is clicked
            if 3*a/4-a5/2 <= mouse[0] <= 3*a/4+a5/2 and 7*b/12-b5/2<= mouse[1] <= 7*b/12+b5/2:
                pygame.draw.rect(screen,colors[2],[3*a/4-a5/2-5,7*b/12-b5/2-5,a5+10,b5+10],0,3)
                text7=font1.render("3",True,colors[0])
            elif D=='3':
                pygame.draw.rect(screen,colors[1],[3*a/4-a5/2-5,7*b/12-b5/2-5,a5+10,b5+10],2,3)
                text7=font1.render('3',True,colors[1])
            else:
                pygame.draw.rect(screen,colors[2],[3*a/4-a5/2-5,7*b/12-b5/2-5,a5+10,b5+10],2,3)
                text7=font1.render('3',True,colors[2])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x=0
                    pygame.quit()
                    quit() # exiting the game
                # Keyboard controls for selecting type and difficulty 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        x=0
                        return ['0','0']
                    if event.key == pygame.K_1:
                        D = '1'
                    if event.key == pygame.K_2:
                        D = '2'
                    if event.key == pygame.K_3:
                        D = '3'
                    if event.key == pygame.K_a:
                        T = 'A'
                    if event.key == pygame.K_b:
                        T = 'B'
                    # Entering the game after selecting type and difficulty
                    if event.key == pygame.K_SPACE:
                        return [T,D]
                    # Exiting the game
                    if event.key == pygame.K_ESCAPE:
                        quit()
                # Mouse controls for selecting type and difficulty
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0]<a/2-a/3 or mouse[0]>a/2+a/3 or mouse[1]<b/2-5*b/18 or mouse[1]>b/2+5*b/18:
                        return [0,0]
                    if a/3-a1/2 <= mouse[0] <= a/3+a1/2 and 5*b/12-10-b1/2<= mouse[1] <= 5*b/12-10+b1/2:
                        T = 'A'
                    if 2*a/3-a2/2 <= mouse[0] <= 2*a/3+a2/2 and 5*b/12-10-b2/2<= mouse[1] <= 5*b/12-10+b2/2:
                        T = 'B'
                    if a/4-a3/2 <= mouse[0] <= a/4+a3/2 and 7*b/12-b3/2<= mouse[1] <= 7*b/12+b3/2:
                        D = '1'
                    if 2*a/4-a4/2 <= mouse[0] <= 2*a/4+a4/2 and 7*b/12-b4/2<= mouse[1] <= 7*b/12+b4/2:
                        D = '2'
                    if 3*a/4-a5/2 <= mouse[0] <= 3*a/4+a5/2 and 7*b/12-b5/2<= mouse[1] <= 7*b/12+b5/2:
                        D = '3'
            # printing the buttons after changing colors according to mouse positioning
            screen.blit(text3,textRect3)
            screen.blit(text4,textRect4)
            screen.blit(text5,textRect5)
            screen.blit(text6,textRect6)
            screen.blit(text7,textRect7)

            pygame.display.update() # updating display for every loop
