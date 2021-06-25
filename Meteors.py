# Lucas Williams
# creating an asteroids style game
from typing import Text
import pygame, math, random, sys, datetime, os, time

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

#variables for text
win= pygame.display.set_mode((WIDTH, HEIGHT))
testingvar=" " 
Wbox=300# standard size for letter boxes
Hbox=50
half_WIDTH=WIDTH/2 # for ease of use
half_HEIGHT=HEIGHT/2
background_x=-600
background_y=-600# default postion due to the size of the background image
BG=pygame.image.load("Meteor Images\\background.jpg")# loads the custom made images
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

def dis_scores(message,v):
    text = LetterFont.render(message,1,FADED)
    screen.blit(text, (half_WIDTH - text.get_width()/2, round((HEIGHT/7)*(v+1))))
    text = LetterFont.render(message,1,WHITE)
    screen.blit(text, ((half_WIDTH - text.get_width()/2)-2, round((HEIGHT/7)*(v+1))-2))
    pygame.display.update()
    pygame.time.delay(1000)
    
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
                        dis_message("Level 1")
                        gameover = False
                        lives = 3
                        score = 0
                        mainFunc(gameover, count, score, lives)
                        pygame.time.delay(1000)           
                    if rect2a.collidepoint((mx,my)):
                        dis_message("Level 2")
                        gameover = False
                        lives = 2
                        score = 5000
                        mainFunc(gameover, count, score, lives)
                        pygame.display.update()
                        pygame.time.delay(1000)
                    if rect3a.collidepoint((mx,my)):
                        dis_message("Level 3")
                        gameover = False
                        lives = 1
                        score = 10000
                        mainFunc(gameover, count, score, lives)
                        pygame.display.update()
                        pygame.time.delay(1000)
                if KB[pygame.K_ESCAPE]:
                    test=False
        

class Player(object):
    def __init__(self):
        self.img = PI
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = half_WIDTH - (self.w/2) #defining properties of the character
        self.y = half_HEIGHT - (self.h/2)
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w/2, self.y - self.sine * self.h/2)


    def draw(self, win):
        win.blit(self.rotatedSurf, self.rotatedRect) #redraws the space ship at the correct angle

    def turnLeft(self): #def the movement of the spaceship
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w/2, self.y - self.sine * self.h/2)

    def turnRight(self):# turns right
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w/2, self.y - self.sine * self.h/2)

    def moveForward(self): #moves in the direction the ship is facing
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x,self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w/2, self.y - self.sine * self.h/2)

    def updateLocation(self): #keeps the spaceship on the screen, allowing it to drive off one side around to the other 
        if self.x > WIDTH + self.w:
            self.x = 0
        elif self.x < 0 - self.w:
            self.x = WIDTH
        elif self.y > HEIGHT + self.h:
            self.y = 0
        elif self.y < 0 - self.h:
            self.y = HEIGHT

class Bullet(object):# defines the bullet obj
    def __init__(self):
        self.point = player.head
        self.x, self.y = self.point
        self.w = 4
        self.h = 4
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
        if self.x < -50 or self.x > WIDTH+50 or self.y < -50 or self.y > HEIGHT + 50: #if the bullet is offscreen deletes it to make the game less demanding on the processor
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
        self.w = 32*rank  #orgianlly a more accurate number, makes the biggest asteroid a bit more forgiving
        self.h = 32*rank #randomizes the asteroids
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


def redrawGameWindow(lives, score): # redraws the game window
    win.blit(BG,(-600,-600))
    player.draw(win)
    for a in asteroids:
        a.draw(win)
    for b in playerBullets:
        b.draw(win)
    text = TitleFont.render("^"*lives, 1, LAZER_BLUE)
    screen.blit(text, (10, 10))
    text = TitleFont.render(str(score), 1, FADED)
    screen.blit(text, ((WIDTH/2)-text.get_width()/2, 10))
    text = TitleFont.render(str(score), 1, WHITE)
    screen.blit(text, (((WIDTH/2)-text.get_width()/2)-5, 10-5))
    pygame.display.update()
def Intialkeypad(initials):
    A=65
    Wbox=70
    dist=20
    letters=[]#an array of arrays   [[x, y, ltr, boolean]]
    #Define where to start our drawing of 26 letters, 13 letters in each line
    startx= round ((WIDTH - (Wbox + dist)*13) /2) #int function round
    starty= round ((HEIGHT/9)*5)
    #load the letters into our double array
    check = True
    while check:
        background()
        for i in range(26):
            x=startx+dist*2+((Wbox + dist)*(i%13))
            y=starty+((i//13)*(dist + Wbox * 2))
            letters.append([x,y,chr(A+i), True])
        for letter in letters:
            x,y,ltr, see= letter
            if see:
                rect1=pygame.Rect(x -Wbox/2,y -Wbox/2,Wbox,Wbox)
                pygame.draw.rect(screen, FADED, rect1)
                rect2=pygame.Rect((x -Wbox/2)-3,(y -Wbox/2)-3,Wbox,Wbox)
                pygame.draw.rect(screen, WHITE, rect2)
                text=LetterFont.render(ltr,1,BLACK)
                screen.blit(text,(x -text.get_width()/2,y -text.get_height()/2))
        while check:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    check = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    for letter in letters:
                        x,y, ltr,see=letter
                        if see:
                            rect=pygame.Rect(x-Wbox/2, y-Wbox/2,Wbox,Wbox)
                            if rect.collidepoint(mx,my):
                                initials.append(ltr)
                    pygame.time.delay(1000)
            InitialBox_w= WIDTH*1.5
            InitialBox_h= HEIGHT/3
            posIB_x=-(WIDTH/4)
            posIB_y=-(HEIGHT/10)
            rect1=pygame.Rect(posIB_x,posIB_y,InitialBox_w,InitialBox_h)
            pygame.draw.rect(screen, WHITE, rect1)
            rect2=pygame.Rect((posIB_x)-3,(posIB_y)-3,InitialBox_w,InitialBox_h)
            pygame.draw.rect(screen, FADED, rect2)
            text = WordFont.render(("press enter to continue"), 1, BLACK)
            screen.blit(text, ((WIDTH/2)-text.get_width()/2, 180))       
            text = TitleFont.render(str(initials), 1, SPACE)
            screen.blit(text, ((WIDTH/2)-text.get_width()/2, 10))
            text = TitleFont.render(str(initials), 1, BLACK)
            screen.blit(text, (((WIDTH/2)-text.get_width()/2)-5, 10-5))
            pygame.display.update()
            KB=pygame.key.get_pressed()
            if KB[pygame.K_RETURN]:
                check=False
                break
def printScores(): # prints the scores note: unstable if interacted with while printing it will crash
    file="Meteor Scoreboard.txt"
    FileRead=open(file,'r')
    v = 0
    background()
    for line in FileRead:
        dis_scores(line,v)
        v += 1
    FileRead.close
    
        
player = Player()
playerBullets = []
asteroids = []
initials= []
count = 0 
def mainFunc(gameover,count,score,lives): 
    while not gameover:
        clock.tick(60)
        count += 1
        score += 1
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid(ran))
        redrawGameWindow(lives,score)
        player.updateLocation() #checks if the player is offscreen
        for b in playerBullets: ##checks if a bullet is offscreen
            b.move()
            if b.checkOffScreen():
                playerBullets.pop(playerBullets.index(b))

        for a in asteroids:
            a.x += a.xv
            a.y += a.yv
            #player collsion 
            if (player.x >= a.x and player.x <= a.x + a.w) or (player.x + player.w >= a.x and player.x + player.w <= a.x + a.w):
                if (player.y >= a.y and player.y <= a.y + a.h) or (player.y + player.h >= a.y and player.y + player.h <= a.y + a.h):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    break
            # bullet collision
            for b in playerBullets:
                if (b.x >= a.x and b.x <= a.x + a.w) or (b.x + b.w >= a.x and b.x + b.w <= a.x + a.w):
                    if (b.y >= a.y and b.y <= a.y + a.h) or (b.y + b.h >= a.y and b.y + b.h <= a.y + a.h):
                        if a.rank == 3:
                            score +=2500
                            na1 = Asteroid(2)
                            na2 = Asteroid(2)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        elif a.rank == 2:
                            score += 5000
                            na1 = Asteroid(1)
                            na2 = Asteroid(1)
                            na1.x = a.x
                            na2.x = a.x
                            na1.y = a.y
                            na2.y = a.y
                            asteroids.append(na1)
                            asteroids.append(na2)
                        else:
                            score += 10000
                        asteroids.pop(asteroids.index(a))
                        playerBullets.pop(playerBullets.index(b))

        if lives <=0: #gives game over and records the scores
            pygame.time.delay(1000)
            dis_message("GAME OVER")
            initials=[]
            Intialkeypad(initials)
            file= "Meteor Scoreboard.txt"
            fileWrite=open(file, 'a')
            dt=datetime.datetime.now()
            linef="\t"+str(dt.month) + "/" + str(dt.day) + "/" + str(dt.year) +"\t"+dt.strftime("%A")+"\t"
            line= "\t"+ linef +"\t"+ str(score)
            fileWrite.write("\n")
            for x in initials:
                fileWrite.write(str(x))
            fileWrite.write(line)
            fileWrite.close()
            
            gameover=True
            

            



        KB=pygame.key.get_pressed() #plays the movement functions
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
            if KB[pygame.K_SPACE]: # Fires the bullets
                    playerBullets.append(Bullet())
                    
def game_Init():
    test=True
    while test:# MainMenu
        
        background()
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
                    printScores()
                    #call main function
                    #mainFunc()
                if rect3a.collidepoint((mx,my)):
                    dis_message("GAME COMPLETE")
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
#main program
game_Init()
