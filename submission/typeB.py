import pygame

class TypeB:
    def startgame(screen):
        a,b = 900, 900
        font1 = pygame.font.Font('fonts/generalFont.ttf',40)
        font2 = pygame.font.Font('fonts/generalFont.ttf',60)

        text1 = font2.render('Under Development',True,(255,255,255))
        textRect1 = text1.get_rect()
        textRect1.center = (a/2,b/2-b/6)
        
        text2 = font1.render('Backspace for menu', True,(255,255,255))
        textRect2 = text2.get_rect()
        textRect2.center = (a/2,b/2+b/6)

        text3 = font1.render('Not a part of project', True,(255,255,255))
        textRect3 = text3.get_rect()
        textRect3.center=(a/2,b/2+50)

        underDevelopment = pygame.image.load('images/underDevelopment.png')
        underDevelopment = pygame.transform.scale(underDevelopment,(200,200))
        
        x=1
        # Initiating the loop
        while x:
            # Drawing rectangular surface for popup
            pygame.draw.rect(screen,(0,0,0),[a/2-a/3,b/2-5*b/18,2*a/3,5*b/9])
            pygame.draw.rect(screen,(255,255,255),[a/2-a/3,b/2-5*b/18,2*a/3,5*b/9],4)
            # printing the text over the rectangular surface
            screen.blit(text1,textRect1)
            screen.blit(text2,textRect2)
            screen.blit(text3,textRect3)
            screen.blit(underDevelopment,(350,300))

            # For mouse controls
            mouse=pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    x=0
                    pygame.quit()
                    quit() # exiting the game
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0]<a/2-a/3 or mouse[0]>a/2+a/3 or mouse[1]<b/2-5*b/18 or mouse[1]>b/2+5*b/18:
                        return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        x=0
                    if event.key == pygame.K_ESCAPE:
                        quit()
            
            pygame.display.update()
