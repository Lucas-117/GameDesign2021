# Lucas Williams
# creating an asteroids rip off
from typing import Text
import pygame, math, random, sys, time, os

pygame.init() 

os.system('cls')


#create our screen or window

WIDTH=1200
HEIGHT=1200
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Meteors")

 

# Define Colors
WHITE=[255,255,255]
BLACK=[0,0,0]
DARK=[5,5,5]
SPACE=[20,20,20]
FADED=[230,230,230]


# Words list
#gameWords= ['python','java','trackpad','computer','keyboard','geeks','laptop','headphones','charger','mouse','software','hardware']

# Load images to list
# images = []
# for i in range(7):
#     image= pygame.image.load("Hangman Images\hangman"+str(i)+ ".png")
#     images.append(image)
    # screen.blit(images[i],(80,100))
    # pygame.display.update()
    # pygame.time.delay(500)
#variables for text
Wbox=300
Hbox=50
half_WIDTH=WIDTH/2
half_HEIGHT=HEIGHT/2
background_x=-600
background_y=-600
BG=pygame.image.load("Meteor Images\\background.jpg")
PI=pygame.image.load("Meteor Images\\undo.png")

#Set up fonts
TitleFont = pygame.font.SysFont("comicsans", 200)
AccentFont = pygame.font.SysFont("comicsans", 150)
WordFont = pygame.font.SysFont("comicsans", 100)
LetterFont=pygame.font.SysFont("comicsans",80)
def background():
    screen.blit(BG, (background_x, background_y))
def dis_message(message):
    background()
    text = AccentFont.render(message,1,FADED)
    screen.blit(text, (half_WIDTH - text.get_width()/2, round(HEIGHT/3)))
    text = AccentFont.render(message,1,WHITE)
    screen.blit(text, (half_WIDTH - text.get_width()/2-5, round(HEIGHT/3)-5))
    pygame.display.update()
    pygame.time.delay(2000)
    
def game_Init():
    test=True
    while test:
        background()
        #screen.fill(DARK)
        text = TitleFont.render("Meteors", 1, FADED)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/6)))
        text = TitleFont.render("Meteors", 1, WHITE)
        screen.blit(text, ((WIDTH/2 - text.get_width()/2)-5, (round(HEIGHT/6))-5))
        
       
        #rect1
        starty1=450
        rect1a=pygame.Rect(half_WIDTH-Wbox, starty1, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, SPACE, rect1a)
        rect1b=pygame.Rect(half_WIDTH-Wbox, starty1, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, FADED, rect1b, width=5)
        text = LetterFont.render("Start Game", 1, FADED)
        screen.blit(text, (half_WIDTH -text.get_width()/2, starty1+text.get_height()/2))
        text = LetterFont.render("Start Game", 1, WHITE)
        screen.blit(text, ((half_WIDTH -text.get_width()/2)-3, (starty1+text.get_height()/2)-3))
       
        #rect 2
        starty2=650
        rect2a=pygame.Rect(half_WIDTH-Wbox, starty2, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, SPACE, rect2a)
        rect2b=pygame.Rect(half_WIDTH-Wbox, starty2, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, FADED, rect2b, width=5)
        text = LetterFont.render("View Scores", 1, FADED)
        screen.blit(text, (half_WIDTH -text.get_width()/2, starty2+text.get_height()/2))
        text = LetterFont.render("View Scores", 1, WHITE)
        screen.blit(text, ((half_WIDTH -text.get_width()/2)-3, (starty2+text.get_height()/2)-3))

        #rect 3
        starty3=850
        rect3a=pygame.Rect(half_WIDTH-Wbox, starty3, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, SPACE, rect3a)
        rect3b=pygame.Rect(half_WIDTH-Wbox, starty3, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, FADED, rect3b, width=5)
        text = LetterFont.render("Exit Game", 1, FADED)
        screen.blit(text, (half_WIDTH -text.get_width()/2, starty3+text.get_height()/2))
        text = LetterFont.render("Exit Game", 1, WHITE)
        screen.blit(text, ((half_WIDTH -text.get_width()/2)-3, (starty3+text.get_height()/2)-3))
       
        #Check collide Point and rectangle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx,my= pygame.mouse.get_pos()
                if rect1a.collidepoint((mx,my)):
                    mainFunc()
                if rect2a.collidepoint((mx,my)):
                    print("hello")
                    #call main function
                    #mainFunc()
                if rect3a.collidepoint((mx,my)):
                    dis_message("GAME COMPLETE")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
def mainFunc():
    background()
    screen.blit(PI,(600,600))

#main program
game_Init()
