from sample import *

def setup():
    smooth()
    size(200,200)

def draw():
    if isMousePressed:
        ellipse(mouseX, mouseY, 100, 100)
done()
