import pygame_functions as pg

pg.screenSize(900,900,50,50)
pg.setBackgroundImage("wooden_tabletop.jpg")
pg.setAutoUpdate(False)

# put screen elements here, so they are global
infoLabel = pg.makeLabel("Nim Game",40,530,120,"black","Alex Brush")
pg.showLabel(infoLabel)
button = pg.makeSprite("button.png")
pg.moveSprite(button,400,100,centre=True)
pg.showSprite(button)
tokens=[]
nimToken = pg.makeSprite("nim_token.png")
paper_bg = pg.makeSprite("paper1.jpg")
pg.moveSprite(paper_bg,500,100)
pg.showSprite(paper_bg)

#for label in labelList:
    #pass

def drawScreen(piles):
    # code to draw the stones
    global tokens
    x = 100
    y = 800
    pg.clearShapes()
    for t in tokens:
        pg.hideSprite(t)
    tokens = []
    for num in range(len(piles)):
        for tokenNum in range(piles[num]):
            tokens.append(pg.makeSprite("nim_token.png"))
            pg.moveSprite(tokens[-1],x,y,centre=True)
            pg.showSprite(tokens[-1])
        
            x += 70
        y -= 200
        x =100



    #paper = pg.makeSprite("paper.jpg")
    #pg.moveSprite(paper)
    pg.updateDisplay()

def setupGame():
    # create the data structure for a new game
    nim_tokens = [7,5,3,1]
    return nim_tokens


def playerMove():
    # code to track mouse movements and do actions, then return their move
    moveMade = False
    while not moveMade:
        if pg.spriteClicked(button):
            pg.changeLabel(infoLabel, f"Button clicked")
        elif pg.mousePressed():
            pg.changeLabel(infoLabel, f"Clicked at {pg.mouseX()} , {pg.mouseY()}")

        
        pg.updateDisplay()
        pg.tick(50)
    return 1

# main game
nim_tokens = setupGame()
drawScreen(nim_tokens)
gameRunning = True
while gameRunning:
    move = playerMove()
