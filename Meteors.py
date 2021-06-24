# Lucas Williams
# creating an asteroids rip off
from typing import Text
import pygame, math, random, sys, time, os

from pygame import display

pygame.init() 

os.system('cls')


#create our screen or window

WIDTH=1200
HEIGHT=1200
screen = pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("Meteors")
clock = pygame.time.Clock()



# Define Colors
WHITE=[255,255,255]
LAZER_BLUE=[92,255,255]
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
win= pygame.display.set_mode((WIDTH, HEIGHT))
testingvar=" "
Wbox=300
Hbox=50
half_WIDTH=WIDTH/2
half_HEIGHT=HEIGHT/2
background_x=-600
background_y=-600
BG=pygame.image.load("Meteor Images\\background.jpg")
PI=pygame.image.load("Meteor Images\\Player Icon.png")
M_128=pygame.image.load("Meteor Images\\M_128.png")
M_64=pygame.image.load("Meteor Images\\M_64.png")
M_32=pygame.image.load("Meteor Images\\M_32.png")
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
    
def levelsmenu(): #prints the level selection screen
    test=True
    while test:
        background()
        text = LetterFont.render("<- esc", 1, WHITE)
        screen.blit(text, (10, 10))
        text = TitleFont.render("Level Selection", 1, FADED)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/6)))
        text = TitleFont.render("Level Selection", 1, WHITE)
        screen.blit(text, ((WIDTH/2 - text.get_width()/2)-5, (round(HEIGHT/6))-5))
        
        
        #rect1
        starty1=450
        rect1a=pygame.Rect(half_WIDTH-Wbox, starty1, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, SPACE, rect1a)
        rect1b=pygame.Rect(half_WIDTH-Wbox, starty1, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, FADED, rect1b, width=5)
        text = LetterFont.render("Level One", 1, FADED)
        screen.blit(text, (half_WIDTH -text.get_width()/2, starty1+text.get_height()/2))
        text = LetterFont.render("Level One", 1, WHITE)
        screen.blit(text, ((half_WIDTH -text.get_width()/2)-3, (starty1+text.get_height()/2)-3))
        
        #rect 2
        starty2=650
        rect2a=pygame.Rect(half_WIDTH-Wbox, starty2, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, SPACE, rect2a)
        rect2b=pygame.Rect(half_WIDTH-Wbox, starty2, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, FADED, rect2b, width=5)
        text = LetterFont.render("Level Two", 1, FADED)
        screen.blit(text, (half_WIDTH -text.get_width()/2, starty2+text.get_height()/2))
        text = LetterFont.render("Level Two", 1, WHITE)
        screen.blit(text, ((half_WIDTH -text.get_width()/2)-3, (starty2+text.get_height()/2)-3))

        #rect 3
        starty3=850
        rect3a=pygame.Rect(half_WIDTH-Wbox, starty3, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, SPACE, rect3a)
        rect3b=pygame.Rect(half_WIDTH-Wbox, starty3, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, FADED, rect3b, width=5)
        text = LetterFont.render("Level Three", 1, FADED)
        screen.blit(text, (half_WIDTH -text.get_width()/2, starty3+text.get_height()/2))
        text = LetterFont.render("Level Three", 1, WHITE)
        screen.blit(text, ((half_WIDTH -text.get_width()/2)-3, (starty3+text.get_height()/2)-3))
        pygame.display.update()
        for event in pygame.event.get():
                KB=pygame.key.get_pressed()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx,my= pygame.mouse.get_pos()
                    if rect1a.collidepoint((mx,my)):#tells what level picked, hit escape to leave the selection screen
                        gameover = False
                        mainFunc(gameover, count)
                        # testingvar="Level 1"
                        # background()
                        # text = TitleFont.render(testingvar, 1, FADED)
                        # screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/6)))
                        # text = TitleFont.render(testingvar, 1, WHITE)
                        # screen.blit(text, ((WIDTH/2 - text.get_width()/2)-5, (round(HEIGHT/6))-5))
                        # pygame.display.update()
                        pygame.time.delay(1000)           
                    if rect2a.collidepoint((mx,my)):
                        testingvar="Level 2"
                        background()
                        text = TitleFont.render(testingvar, 1, FADED)
                        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/6)))
                        text = TitleFont.render(testingvar, 1, WHITE)
                        screen.blit(text, ((WIDTH/2 - text.get_width()/2)-5, (round(HEIGHT/6))-5))
                        pygame.display.update()
                        pygame.time.delay(1000)
                    if rect3a.collidepoint((mx,my)):
                        testingvar="Level 3"
                        background()
                        text = TitleFont.render(testingvar, 1, FADED)
                        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/6)))
                        text = TitleFont.render(testingvar, 1, WHITE)
                        screen.blit(text, ((WIDTH/2 - text.get_width()/2)-5, (round(HEIGHT/6))-5))
                        pygame.display.update()
                        pygame.time.delay(1000)
                if KB[pygame.K_ESCAPE]:
                    test=False
        

class Player(object):
    def __init__(self):
        self.img = PI
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = half_WIDTH - (self.w/2) #may need to remove the centering parts later
        self.y = half_HEIGHT - (self.h/2)
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w/2, self.y - self.sine * self.h/2)


    def draw(self, win):
        #win.blit(self.img, [self.x, self.y, self.w, self.h])
        win.blit(self.rotatedSurf, self.rotatedRect)

    def turnLeft(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w/2, self.y - self.sine * self.h/2)

    def turnRight(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w/2, self.y - self.sine * self.h/2)

    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w/2, self.y - self.sine * self.h/2)

    def updateLocation(self):
        if self.x > WIDTH + self.w:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = WIDTH
        elif self.y > HEIGHT + self.h:
            self.y = 0
        elif self.y < 0 - self.h:
            self.y = HEIGHT

class Bullet(object):
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 2
        self.h = 2
        self.c = player.cosine
        self.s = player.sine
        self.xv = self.c * 10
        self.yv = self.s * 10

    def move(self):
        self.x += self.xv
        self.y -= self.yv

    def draw(self,win):
        pygame.draw.rect(win, LAZER_BLUE, [self.x, self.y, self.w, self.h])
    def checkOffScreen(self):
        if self.x < -50 or self.x > WIDTH+50 or self.y < -50 or self.y > HEIGHT + 50:
            return True

class Asteroid(object): # defines the asteroids
    def __init__(self, rank):
        self.rank = rank
        if self.rank ==1:
            self.image = M_32
        elif self.rank == 2:
            self.image = M_64
        else:
            self.image = M_128
        self.w = 32*(2^(rank-1))
        self.h = 32*(2^(rank-1))#randomizes the asteroids
        self.ranPoint = random.choice([(random.randrange(0,WIDTH-self.w), random.choice([-1*self.h - 5, HEIGHT + 5])), (random.choice([-1*self.w - 5, WIDTH + 5]), random.randrange(0, HEIGHT - self.h))])
        self.x, self.y = self.ranPoint
        if self.x < WIDTH/2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < HEIGHT/2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xv = self.xdir * random.randrange(1,3)
        self.yv = self.ydir * random.randrange(1,3)

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


def redrawGameWindow(): # redraws the game window
    win.blit(BG,(-600,-600))
    player.draw(win)
    for a in asteroids:
        a.draw(win)
    for b in playerBullets:
        b.draw(win)
    pygame.display.update()
    #def
player = Player()
playerBullets = []
asteroids = []
count = 0 
def mainFunc(gameover,count):
    while not gameover:
        clock.tick(60)
        count += 1
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid(ran))
        redrawGameWindow()
        player.updateLocation()
        for b in playerBullets:
            b.move()
            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))

        for a in asteroids:
            a.x += a.xv
            a.y += a.yv


            # bullet collision
            for b in playerBullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or (b.x + b.w >= a.x and b.x + b.w <= a.x + a.w):
                    if (b.y >= a.y and b.y <= a.y + a.h) or (b.y + b.h >= a.y and b.y + b.h <= a.y + a.h):
                        asteroids.pop(asteroids.index(a))
                        playerBullets.pop(playerBullets.index(b))
        KB=pygame.key.get_pressed()
        if KB[pygame.K_UP]:
            player.moveForward()
        if KB[pygame.K_RIGHT]:
            player.turnRight()
        if KB[pygame.K_LEFT]:
            player.turnLeft()
        if KB[pygame.K_ESCAPE]:
                break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()    
            if KB[pygame.K_SPACE]:
                    playerBullets.append(Bullet())
                    
def game_Init():
    test=True
    while test:
        
        background()
        #screen.fill(DARK)
        text = TitleFont.render("Meteors", 1, FADED)
        screen.blit(text, (WIDTH/2 - text.get_width()/2, round(HEIGHT/6)))
        text = TitleFont.render("Meteors", 1, WHITE)
        screen.blit(text, ((WIDTH/2 - text.get_width()/2)-5, (round(HEIGHT/6))-5))
        
       
        #rect1 button1
        starty1=450
        rect1a=pygame.Rect(half_WIDTH-Wbox, starty1, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, SPACE, rect1a)
        rect1b=pygame.Rect(half_WIDTH-Wbox, starty1, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, FADED, rect1b, width=5)
        text = LetterFont.render("Start Game", 1, FADED)
        screen.blit(text, (half_WIDTH -text.get_width()/2, starty1+text.get_height()/2))
        text = LetterFont.render("Start Game", 1, WHITE)
        screen.blit(text, ((half_WIDTH -text.get_width()/2)-3, (starty1+text.get_height()/2)-3))
       
        #rect 2 button 2
        starty2=650
        rect2a=pygame.Rect(half_WIDTH-Wbox, starty2, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, SPACE, rect2a)
        rect2b=pygame.Rect(half_WIDTH-Wbox, starty2, Wbox*2,Hbox*2)
        pygame.draw.rect(screen, FADED, rect2b, width=5)
        text = LetterFont.render("View Scores", 1, FADED)
        screen.blit(text, (half_WIDTH -text.get_width()/2, starty2+text.get_height()/2))
        text = LetterFont.render("View Scores", 1, WHITE)
        screen.blit(text, ((half_WIDTH -text.get_width()/2)-3, (starty2+text.get_height()/2)-3))

        #rect 3 button 3
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
                    levelsmenu()
                if rect2a.collidepoint((mx,my)):
                    print("hello")
                    #call main function
                    #mainFunc()
                if rect3a.collidepoint((mx,my)):
                    dis_message("GAME COMPLETE")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
#main program
game_Init()
