import pygame , sys , math , os
import pygame.freetype 
import pygame.font

from pygame.locals import *

WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
DARKGREEN=(0,100,0)
BLACK=(0,0,0)
GRAY=(127,127,127)
LIGHTGRAY=(211,211,211)
YELLOW=(255,255,0)
DISPLAY_W=1000
DISPLAY_H=800
GAMEPLAY_W=600
GAMEPLAY_H=600
PLAYER1=1
PLAYER2=2

pygame.init()
surf = pygame.display.set_mode ((DISPLAY_W,DISPLAY_H))
titreFont = pygame.freetype.Font("28 Days Later.ttf", 50)
playerFont = pygame.freetype.Font("airstrikegrad.ttf", 35)
resultFont = pygame.freetype.Font("28 Days Later.ttf", 75)

run = True
clock=pygame.time.Clock()
img_cross = pygame.image.load("cross.png")
img_circle = pygame.image.load("circle.png")

Matrix = None
vx = 0  
wMatrix, hMatrix = 0, 0
player = 0 
winner = 0 
 

def init():
    global player
    global wMatrix
    global hMatrix 
    global Matrix
    global vx
    wMatrix, hMatrix = 3, 3
    Matrix = [[0 for x in range(wMatrix)] for y in range(hMatrix)] 
    player = PLAYER1
    vx = 1
    winner = 0 

def drawbackground():
    global surf
    global DISPLAY_W
    global DISPLAY_H
    global GAMEPLAY_W
    global GAMEPLAY_H
    global wMatrix
    global hMatrix 
    surf.fill(BLACK)
    pygame.draw.rect(surf, LIGHTGRAY, (10,(DISPLAY_H-GAMEPLAY_H)/2,(DISPLAY_W-GAMEPLAY_W)/2 - 20,GAMEPLAY_H))
    pygame.draw.rect(surf, LIGHTGRAY, ((DISPLAY_W-GAMEPLAY_W)/2 + GAMEPLAY_W +10,(DISPLAY_H-GAMEPLAY_H)/2,(DISPLAY_W-GAMEPLAY_W)/2 - 20,GAMEPLAY_H))


    pygame.draw.rect(surf, WHITE, ((DISPLAY_W-GAMEPLAY_W)/2,(DISPLAY_H-GAMEPLAY_H)/2,GAMEPLAY_W,GAMEPLAY_H))
    for x in range (wMatrix):
        pygame.draw.line(surf,BLUE,((DISPLAY_W-GAMEPLAY_W)/2+((GAMEPLAY_W/wMatrix)*(x+1)) ,(DISPLAY_H-GAMEPLAY_H)/2),
        ((DISPLAY_W-GAMEPLAY_W)/2+((GAMEPLAY_W/wMatrix)*(x+1)),((DISPLAY_H-GAMEPLAY_H)/2) + GAMEPLAY_H),2)
    for y in range (hMatrix):
        pygame.draw.line(surf,BLUE,((DISPLAY_W-GAMEPLAY_W)/2,((DISPLAY_H-GAMEPLAY_H)/2) + (GAMEPLAY_H/hMatrix)*(y+1)),
        (DISPLAY_W - (DISPLAY_W-GAMEPLAY_W)/2,((DISPLAY_H-GAMEPLAY_H)/2) + (GAMEPLAY_H/hMatrix)*(y+1)),2)

    text, rect = titreFont.render("Tic Tac Toe", YELLOW)
    surf.blit(text, text.get_rect(center = (DISPLAY_W / 2 ,(DISPLAY_H-GAMEPLAY_H)/4)))


def displayPlayer():
    global player
    global DISPLAY_W
    global DISPLAY_H
    global GAMEPLAY_W
    global GAMEPLAY_H
    global img_cross
    global img_circle
    textplayer1, rectplayer1 = playerFont.render("PLAYER1", DARKGREEN if player == PLAYER1 else GRAY)
    textplayer2, rectplayer2 = playerFont.render("PLAYER2", DARKGREEN if player == PLAYER2 else GRAY)
    surf.blit(textplayer1, textplayer1.get_rect(center = ((DISPLAY_W-GAMEPLAY_W)/4 ,(DISPLAY_H - GAMEPLAY_H)/2 + 20)))
    surf.blit(textplayer2, textplayer2.get_rect(center = (DISPLAY_W - (DISPLAY_W-GAMEPLAY_W)/4 ,(DISPLAY_H - GAMEPLAY_H)/2 + 20 )))

    small_img_cross = pygame.transform.scale(img_cross, (75 , 75))
    small_img_circle = pygame.transform.scale(img_circle, (75 , 75)) 
    surf.blit( small_img_cross,small_img_cross.get_rect(center = ((DISPLAY_W-GAMEPLAY_W)/4 ,(DISPLAY_H - GAMEPLAY_H)/2 + 75)))
    surf.blit(small_img_circle,small_img_circle.get_rect(center = (DISPLAY_W - (DISPLAY_W-GAMEPLAY_W)/4 ,(DISPLAY_H - GAMEPLAY_H)/2 + 75 )))





def changePlayer():
    global player                
    if (player == PLAYER1) : 
        player = PLAYER2
    else :
        player = PLAYER1


def checkResult():
    global player
    global Matrix
    global winner 
    winner = 0
    #check line
    for y in range (hMatrix):
        checklineplayer1 = True ; 
        checklineplayer2 = True ; 
        for x in range(wMatrix):
            if Matrix[y][x] != PLAYER1 :checklineplayer1 = False ; 
            if Matrix[y][x] != PLAYER2 :checklineplayer2 = False ; 
        if checklineplayer1 : winner = PLAYER1 
        if checklineplayer2 : winner = PLAYER2
    #check column
    for x in range (wMatrix):
        checkcolplayer1 = True ; 
        checkcolplayer2 = True ; 
        for y in range(hMatrix):
            if Matrix[y][x] != PLAYER1 :checkcolplayer1 = False ; 
            if Matrix[y][x] != PLAYER2 :checkcolplayer2 = False ; 
        if checkcolplayer1 : winner = PLAYER1 
        if checkcolplayer2 : winner = PLAYER2
    #check diag1
    checkxyplayer1 = True ; 
    checkxyplayer2 = True ; 
    for xy in range (wMatrix):
        if Matrix[xy][xy] != PLAYER1 :checkxyplayer1 = False ; 
        if Matrix[xy][xy] != PLAYER2 :checkxyplayer2 = False ; 
    if checkxyplayer1 : winner = PLAYER1 
    if checkxyplayer2 : winner = PLAYER2
    checkxyplayer1 = True ; 
    checkxyplayer2 = True ; 
    for xy in range (wMatrix):
        if Matrix[xy][(wMatrix-1) - xy] != PLAYER1 :checkxyplayer1 = False ; 
        if Matrix[xy][(wMatrix-1) - xy] != PLAYER2 :checkxyplayer2 = False ; 
    if checkxyplayer1 : winner = PLAYER1 
    if checkxyplayer2 : winner = PLAYER2

    full=True 
    for y in range(hMatrix):
        for x in range (wMatrix):
            if Matrix[y][x] == 0 : 
                full = False

    endOfGame = False ; 
    if (winner != 0):
        textEndOfGame = "Winner is PLAYER "+ str(winner)
        print (textEndOfGame)
        endOfGame = True 
    elif (full) : 
        textEndOfGame = "You lost !"
        print (textEndOfGame)
        endOfGame = True 

    if (endOfGame):
        resultSurface = pygame.Surface ((GAMEPLAY_W * 2 / 3, GAMEPLAY_H * 1 / 3),pygame.SRCALPHA)
        resultSurface.fill(GRAY)
        text,rect  = titreFont.render(textEndOfGame, YELLOW)
        resultSurface.blit(text, text.get_rect(center = (GAMEPLAY_W * 2 / 6 ,GAMEPLAY_H * 1 / 6)))
        rotated_resultSurface = pygame.transform.rotate(resultSurface, 20)
        surf.blit(rotated_resultSurface, ((DISPLAY_W - GAMEPLAY_W ) / 2 + (GAMEPLAY_W /6), (DISPLAY_H - GAMEPLAY_H ) / 2 + (GAMEPLAY_H /6)))
        pygame.display.flip()
        pygame.event.clear()
        wait = True ; 
        while wait:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                    wait = False ; 
            elif event.type == pygame.MOUSEBUTTONDOWN  :
                 wait = False ; 
            elif event.type == KEYDOWN:
                wait = False ; 
        init()




    



    


init()
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            x, y = pygame.mouse.get_pos()
            indexx =math.floor((x - ((DISPLAY_W-GAMEPLAY_W)/2)) / (GAMEPLAY_W / wMatrix))
            indexy =math.floor((y - ((DISPLAY_H-GAMEPLAY_H)/2)) / (GAMEPLAY_H / hMatrix))
            if pygame.mouse.get_pressed() == (1,0,0) :
                print ("clic bouton gauche")
                if (Matrix[indexy][indexx] == 0):
                    Matrix[indexy][indexx] = player 
                    checkResult()
                    changePlayer()
                
            if pygame.mouse.get_pressed() == (0,0,1) :
                print ("clic bouton droit")
                Matrix[indexy][indexx] = 0

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                print ("vous avez appuyé sur la touche espace")
            elif event.key == pygame.K_a :
                print ("vous avez appuyé sur la touche A")
            elif event.key == pygame.K_RETURN :
                print ("vous avez appuyé sur la touche Entrée")
            else :
                print ("vous avez appuyé sur une touche")
    clock.tick(60)
    drawbackground()
    displayPlayer()
    for x in range (wMatrix):
        for y in range (hMatrix):
            posX = (DISPLAY_W-GAMEPLAY_W)/2+((GAMEPLAY_W/wMatrix)*(x))
            posY = (DISPLAY_H-GAMEPLAY_H)/2+((GAMEPLAY_H/hMatrix)*(y))
            if (Matrix[y][x] == PLAYER1):
                surf.blit(img_cross,(posX,posY))
            elif (Matrix[y][x] == PLAYER2):
                surf.blit(img_circle,(posX,posY))
            
    pygame.display.flip()
pygame.quit()