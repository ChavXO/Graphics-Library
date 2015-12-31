from sample import *
sunCount=10 
startPointSun=10 
incX=1 

FoxCount=0 
startPointFox=10 
sunSize=100 

moonCount=0 
startPointMoon=10 
moonSize=70 


def setup():
    size(600, 600) 
    background(184, 236, 255) 
    smooth() 
    noStroke()
    
isDay = True 
isNightOver = False 


def draw ():
    global isDay
    global sunCount
    global moonCount
    global FoxCount
    if isDay:
        background(184, 236, 255) 
        fill(50, 100, 30) 
        rect(0, 0.7 * height, width, height) 
        drawSun(200+sunCount, 150, sunSize) 
        sunCount= sunCount+incX 
        drawFox(200+FoxCount, 550, 100, 100, isDay) 
        drawFox(210+FoxCount, 480, 100, 100, isDay) 
        drawFox(270+FoxCount, 500, 100, 100, isDay) 
        FoxCount=FoxCount+incX 
    else:
        background(0, 0, 0) 
        fill(0, 0, 0) 
        rect(0, 0.7 * height, width, height) 
        drawMoon(-moonSize/2+moonCount, 150, moonSize) 

        drawFox(200, 550, 100, 100, isDay) 
        drawFox(210, 480, 100, 100, isDay) 
        drawFox(270, 500, 100, 100, isDay) 
        moonCount= moonCount+incX
  
    
  
    if (200+sunCount-sunSize/2> width and isDay):
        isDay = False 
    elif (not isDay) and (-moonSize/2+moonCount> width):
        isNightOver = True 
    else:
        where = -moonSize/2+moonCount 
 



def drawSun (localX, localY, localRad):
    fill(255, 170, 0) 
    ellipse(localX, localY, localRad, localRad) 


def drawMoon(localX, localY, localSize):
    fill(255, 255, 255) 
    ellipse(localX, localY, localSize, localSize) 


def drawFox(centerX, centerY, objWidth, objHeight, day):

    noStroke()
    headSize = objHeight/2
    headX = centerX + 3/2 * objWidth/5
    headY = centerY - objHeight/4
    if (day):
        fill(106, 59, 59)
        ellipse(headX, headY, headSize, headSize)

    fill(0)
    ellipse(headX+headSize/6, headY-headSize/6, headSize/4, headSize/4)
    fill(255)
    ellipse(headX+headSize/6, headY-headSize/6, headSize/8, headSize/8)
    fill(0)
    ellipse(headX-headSize/6, headY-headSize/6, headSize/4, headSize/4)
    fill(255)
    ellipse(headX-headSize/6, headY-headSize/6, headSize/8, headSize/8)

done()
