#Lucas Williams
#learn how to change colors
#learn to draw shapes
#learn how to control objects on the screen with key
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
import pygame
import time,sys,os

from pygame.draw import rect
print(sys.path)
pygame.init() #Initalize the game
purple=[200,0,200]
white=[255,255,255]
red=[200,25,0]
green=[0,200,50]
WIDTH=500
HEIGHT=600
os.system('clr')
#create object to open window
screen=pygame.display.set_mode((WIDTH,HEIGHT)) # declare our screen or window

BG=pygame.image.load("Images\sci-fi-level[still-].png")
II=pygame.image.load("Images\\atom2.png")
pygame.time.delay(100)  #delay in milliseconds
pygame.display.set_caption("Lucas' Game")
x=10
y=10
xI=10
yI=10
w_box=20
h_box=20
rad=0
rect1 = pygame.Rect(x,y,w_box,h_box) #x,y,w,h
rect2 = pygame.Rect(x,y,w_box,h_box) #x,y,w,h
#Variables to control our rect
speed=5
jump=10
jumpCheck=False
jumpI=10
jumpCheckI=False
pygame.display.update()
#you must always ... ALWAYS
check = True
while check:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            check = False
    
    KB=pygame.key.get_pressed() #Checking is a key has been pressed
    if KB[pygame.K_RIGHT]:
        rect1.x += speed #move rectangle two pixels to the right
    if KB[pygame.K_LEFT]:
        rect1.x -= speed #move rectangle two pixels to the left
    # if KB[pygame.K_SPACE]:
    #     jumpCheck=True
    #     rect1.y -=(jump*abs(jump))/2
    #     jump -= 1
    # else:
    #     jumpCheck=False
    #Code for Jumping
    if not jumpCheck:
        if KB[pygame.K_UP]:
            rect1.y -= speed #move rectangle two pixels up
        if KB[pygame.K_DOWN]:
            rect1.y += speed #move rectangle two pixels down
        if KB[pygame.K_SPACE]:
            jumpCheck= True
    else:
        if jump >= -10:
            rect1.y -= (jump*abs(jump))/2
            jump -= 1
        else:
            jump = 10
            jumpCheck=False

    if KB[pygame.K_d]:
        rect2.x += speed #move rectangle two pixels to the right
    if KB[pygame.K_a]:
        rect2.x -= speed #move rectangle two pixels to the left

    if KB[pygame.K_w]:
        rect2.y -= speed #move rectangle two pixels up
    if KB[pygame.K_s]:
        rect2.y += speed #move rectangle two pixels down

    if KB[pygame.K_w]:
        rad += speed
    if KB[pygame.K_s]:
        rad -= speed
    #attempt at controlling II
    KB=pygame.key.get_pressed() #Checking is a key has been pressed
    if KB[pygame.K_h]:
        xI += speed #move rectangle two pixels to the right
    if KB[pygame.K_f]:
        xI -= speed #move rectangle two pixels to the left
    # if KB[pygame.K_SPACE]:
    #     jumpCheck=True
    #     rect1.y -=(jump*abs(jump))/2
    #     jump -= 1
    # else:
    #     jumpCheck=False
    #Code for Jumping
    if not jumpCheckI:
        if KB[pygame.K_t]:
            yI -= speed #move rectangle two pixels up
        if KB[pygame.K_g]:
            yI += speed #move rectangle two pixels down
        if KB[pygame.K_b]:
            jumpCheckI= True
    else:
        if jump >= -10:
            yI -= (jumpI*abs(jumpI))/2
            jumpI -= 1
        else:
            jumpI = 10
            jumpCheckI=False


        #control limits
    if rect1.x <0: rect1.x=0
    if rect1.x >WIDTH-w_box: rect1.x=WIDTH-w_box
    if rect1.y <0: rect1.y=0
    if rect1.y >HEIGHT-h_box: rect1.y=HEIGHT-h_box

    if rect2.x <0: rect2.x=0
    if rect2.x >WIDTH-w_box: rect2.x=WIDTH-w_box
    if rect2.y <0: rect2.y=0
    if rect2.y >HEIGHT-h_box: rect2.y=HEIGHT-h_box

    if xI <0: xI=0
    if xI >WIDTH-w_box: xI=WIDTH-w_box
    if yI <0: yI=0
    if yI >HEIGHT-h_box: yI=HEIGHT-h_box

    if rad <0: rad=1
    if rad > WIDTH/2: rad= WIDTH/2
    if rect1.colliderect(rect2):
        rect1.x -= 10
        rect2.x += 10
    screen.fill(purple)
    screen.blit(BG,(0,200))
    screen.blit(II,(xI,yI))
    pygame.draw.rect(screen,red,rect1)
    pygame.draw.rect(screen,red,rect2)
    pygame.draw.circle(screen, (white),(WIDTH/2,HEIGHT/2), rad, 2)
    pygame.display.update()
    pygame.time.delay(30)
print("Goodbye")
pygame.time.delay(100)  #delay in milliseconds
pygame.quit()