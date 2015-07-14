from sample import *


moveBoat=300  
moveBigFish=250
moveCloud = 100
cloudColor = 255
increasing = False
moveInc=1  
moveIncFish=1  

color1 = (random(0, 150), random(0, 150), random(0, 150))
color2 = (random(100, 255), random(100, 255), random(100, 255))  
def setup():
    size(600, 500)
    noStroke()
    frameRate(40)

def draw():
    global moveBoat
    global moveCloud
    global moveBigFish
    global moveIncFish
    global cloudColor
    global increasing
    background(190, 240, 245)  
    fill(30, 81, 229)  
    rect(0, 200, 600, 300)  
    fill(255, 255, 0)  
    ellipse(550, 50, 50, 50)  

    drawBoat(moveBoat)  
    moveBoat=moveBoat-moveInc

    drawCloud(moveCloud)
    moveCloud = moveCloud + moveInc

    if not increasing :
        cloudColor = cloudColor - 1
        if cloudColor < 0 :
            increasing = not increasing
            cloudColor = 0
    else :
        cloudColor = cloudColor + 1
        if cloudColor > 255 :
            increasing = not increasing
            cloudColor = 255
        
    drawBigFish(moveBigFish)  
    moveBigFish=moveBigFish+1  
    
    if moveBigFish >= 800:
        moveBigFish=-80  
    #print color1
    fill(color1)
    drawManyFish(500+moveIncFish, 400, 20, 20)  
    drawManyFish(450+moveIncFish, 270, 25, 25)  
    drawManyFish(480+moveIncFish, 290, 10, 10)
    #print color2
    fill(color2)
    drawManyFish(470+moveIncFish, 450, 30, 30)  
    drawManyFish(530+moveIncFish, 310, 15, 15)  
    drawManyFish(550+moveIncFish, 470, 24, 24)  
    moveIncFish=moveIncFish-1
    #print "done"

def drawBoat(moveX):
    noStroke()  
    smooth()   
    fill(255)  
    rect(moveX, 130, 200, 20)  
    fill(0)  
    rect(moveX, 150, 200, 50)  
    triangle(moveX-20, 150, moveX, 150, moveX, 200)  
    triangle(moveX+200, 150, moveX+220, 150, moveX+200, 200)  

    for i in range(moveX + 5, moveX + 190, 12):
        fill(245, 227, 0)  
        rect(i, 140, 5, 5)   
  
def drawCloud(moveX) :
    noStroke()
    fill(cloudColor)
    ellipse(moveX, 25, 25, 25)
    ellipse(moveX + 30, 25, 25, 25)

    for i in range(moveX + 10, moveX + 40, 10):
        #fill(0)
        ellipse(i, 35, 25, 25)
        ellipse(i, 15, 25, 25)
    
def keyPressed():
    global moveInc
    if key == 'P' or key == 'p' :
        moveInc=0  
    elif key == 'i':
        moveInc=moveInc+1  
    elif key=='d':
        moveInc = moveInc-1  

def mousePressed():
    global color1
    global color2
    color1 = (random(0, 150), random(0, 150), random(0, 150))  
    color2 = (random(100, 255), random(100, 255), random(100, 255))  
  
def drawBigFish(moveFish):
    #print "Big  Fish"
    noStroke()  
    smooth()  
    fill(134, 27, 22)  
    ellipse(moveFish+50, 350, 80, 80)  
    fill(30, 81, 229)  
    rect(moveFish+10, 350, 80, -50)  
    fill(134, 27, 22)  
    ellipse(moveFish-30, 330, 200, 130)  
    fill(255)  
    triangle(moveFish+50, 350, moveFish+60, 350, moveFish+55, 335)  
    triangle(moveFish+60, 350, moveFish+75, 350, moveFish+65, 325)  
    triangle(moveFish+75, 350, moveFish+88, 350, moveFish+85, 330)  
    fill(69, 137, 114)  
    triangle(moveFish-30, 320, moveFish-50, 300, moveFish-50, 340)  
    triangle(moveFish-130, 320, moveFish-160, 250, moveFish-160, 400)  
    triangle(moveFish-15, 270, moveFish-50, 230, moveFish-50, 270)  
    fill(255)  
    ellipse(moveFish+30, 310, 18, 18)  
    fill(0)  
    ellipse(moveFish+30, 310, 10, 10)  
    fill(134, 27, 22)  
    rect(moveFish+10, 300, 30, 10)
    #print "End Big Fish"

def drawManyFish(centerX, centerY, objWidth, objHeight):
    #print "Many Fish"
    noStroke()  
    smooth()  
    ellipse(centerX, centerY, objWidth, objHeight)  
    triangle(centerX+objWidth/2, centerY, centerX+objWidth, centerY-objHeight/2, centerX+objWidth, centerY+objHeight/2)
    #print "End Many Fish"

done()

