from grph01 import *
size(1100, 850)
background(71, 206, 54)
smooth()

fill(0)
rect(0, 0, 135, 725)
rect(155, 0, 110, 625)
rect(825, 0, 110, 625)
rect(965, 0, 135, 725)

stroke(0)
strokeWeight(50)
strokeCap("SQUARE");
line(290, -50, 550, 515)
line(530, -50, 700, 400)
line(650, -50, 400, 500)
line(725, -50, 490, 500)

noStroke()

fill(255, 153, 0)
triangle(275, 275, 500, 60, 820, 275)

fill(155, 82, 27)
rect(300, 275, 480, 310)

fill(0)
rect(400, 360, 160, 225)

fill(255, 0, 0)
rect(600, 360, 130, 130)

fill(255, 208, 137)
ellipse(665, 455, 65, 65)

stroke(0)
strokeWeight(10)
strokeCap("SQUARE")
line(630, 430, 700, 430)

fill(0)
triangle(650, 430, 665, 390, 680, 430)

noStroke()

fill(251, 255, 44)
ellipse(350, 315, 60, 60)
ellipse(550, 315, 60, 60)
ellipse(740, 315, 60, 60)
ellipse(350, 470, 60, 60)
ellipse(600, 545, 60, 60)
ellipse(740, 545, 60, 60)

fill(144, 226, 255)
ellipse(350, 390, 60, 60)
ellipse(350, 545, 60, 60)
ellipse(455, 315, 60, 60)
ellipse(650, 315, 60, 60)
ellipse(670, 545, 60, 60)

fill(44, 116, 255)
triangle(250, 760, 365, 570, 460, 760)

fill(252, 176, 231)
triangle(400, 825, 510, 630, 600, 825)

done()
