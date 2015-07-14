from sample import *

def setup() :
    size(500, 600) 
    smooth() 
    background(16, 4, 75) 

    dotsX=0 
    dotsY=0 
    dotsSize=0 
    for i in range(20):
        dotsX=random(width) 
        dotsY=random(height) 
        dotsSize=random(3, 30) 
        fill(255, 255, 255) 
        ellipse(dotsX, dotsY, dotsSize, dotsSize) 
   
 

fgH=359 
fgChange=-3 

def draw():
    global fgH
    global fgChange
    #loop() 
    colorMode("HSB") 

    drawSide(fgH, 64, 97, 470, 0) 
    drawSide(fgH, 64, 97, 0, 0) 
    if (fgH+fgChange>=0) :
        fgH=fgH+fgChange 
    else:
        fgH=359 

    drawScallopedBorder() 
    """
    if (mousePressed) :
        fishSize=random(10, 70) 
        drawFish(mouseX, mouseY, fishSize)
        
    if (key == 'P' or key == 'p'):
        fgChange=0
    else:
        fgChange=-3
    """

def keyPressed():
    global fgChange
    if (key == 'P' or key == 'p'):
        fgChange=0
    else:
        fgChange=-3


def mousePressed():
    fishSize=random(10, 70) 
    drawFish(mouseX, mouseY, fishSize)

 

def drawSide(fgH, fgS, fgB, cornerX, cornerY):
    fill(fgH, fgS, fgB) 
    noStroke() 
    rect(cornerX, cornerY, 30, height) 

   

def drawFish(centerX, centerY, fishSize):
    colorMode("RGB") 
    fill(255, 64, 154) 
    ellipse(centerX, centerY, fishSize, fishSize/2.5) 
    strokeWeight(fishSize/12) 
    stroke(0) 
    #point(centerX-fishSize/4, centerY-fishSize/12) 
    noStroke() 
    triangle(centerX+fishSize/2, centerY, centerX+fishSize, centerY-fishSize/6, centerX+fishSize, centerY+fishSize/6) 
   

def drawScallopedBorder():
    smooth() 
    for i in range(20):
        ellipse(0+i*30, 0, 30, 30) 
        ellipse(0+i*30, height, 30, 30)

done()


