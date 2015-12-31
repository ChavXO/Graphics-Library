from sample import *

size(720, 580)

colorMode("HSB")

for i in range(580):
  stroke(200, 200, i*0.2)
  line(0, i, 720, i)


colorMode("RGB")

smooth()
stroke(0)

rect(60, 20, 120, 40)
rect(100, 60, 80, 40)
rect(120, 100, 60, 40)

fill(0)

triangle(60, 60, 70, 70, 180, 60)
triangle(100, 100, 110, 110, 180, 100)
triangle(120, 140, 130, 150, 180, 140)

fill(255)
rect(180, 140, 60, 40)
rect(180, 180, 80, 40)
rect(180, 220, 120, 40)
rect(180, 260, 140, 40)
rect(180, 300, 160, 40)
rect(180, 340, 180, 40)
rect(160, 380, 180, 40)
rect(140, 420, 180, 40)
rect(120, 460, 180, 40)
rect(100, 500, 180, 50)

fill(0)
triangle(340, 380, 360, 380, 340, 420)
triangle(320, 420, 340, 420, 320, 460)
triangle(300, 460, 320, 460, 300, 500)
triangle(280, 500, 300, 500, 280, 550)

noStroke()
fill(70, 163, 232)
triangle(420, 540, 440, 540, 420, 560)
triangle(420, 520, 480, 560, 420, 540)

fill(34, 117, 178)
triangle(720, 380, 640, 560, 720, 560)

fill(247, 211, 65)
ellipse(540, 140, 180, 180)

fill(0)
triangle(538, 140, 542, 140, 540, 60)

stroke(0)
line(600, 140, 620, 140)
line(540, 200, 540, 220)
line(480, 140, 460, 140)

done()


