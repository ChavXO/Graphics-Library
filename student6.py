from grph01 import *
size(1000,800) 
background(255) 

smooth() 
noStroke() 


fill(11,54,36) 
quad(400,520,1000,650,1000,880,400,680) 


fill(139,52,17) 
rect(0,0,700,200) 


fill(0) 
rect(700,0,200,200) 

stroke(15,95,43) 
strokeWeight(70) 
strokeCap("SQUARE") 
line(530,50,530,180) 

noStroke() 


fill(75,23,4) 
quad(455,80,1000,-20,1000,50,455,150) 


fill(250,243,103) 
triangle(400,520,1000,400,1000,650) 


fill(51,82,81) 
quad(400,200,900,230,900,420,400,520) 


fill(247,168,47) 
quad(900,230,1000,150,1000,440,900,420) 

fill(250,247,192) 
triangle(400,200,1000,150,900,230) 

stroke(15,95,43) 
strokeWeight(70) 
strokeCap("SQUARE") 
line(410,50,410,180) 

noStroke() 


fill(7,36,24) 
quad(400,150,400,200,1000,150,1000,50) 


fill(255,0,38) 
quad(800,400,830,435,800,500,780,444) 


fill(0) 
quad(650,500,680,490,700,560,630,560) 

fill(0) 
ellipse(680,490,40,25) 

stroke(15,95,43) 
strokeWeight(70) 
strokeCap("SQUARE") 


line(50,50,50,180) 
line(170,50,170,180) 
line(290,50,290,180) 

stroke(0) 
line(50,140,50,180) 
line(170,90,170,180) 
line(290,120,290,180) 

noStroke() 


fill(11,54,36) 
rect(0,200,400,320) 


stroke(0) 
strokeWeight(10) 
line(170,200,170,520) 
line(230,200,230,520) 


strokeWeight(100) 
line(80,230,80,480) 
line(320,230,320,480) 

noStroke() 

fill(130,137,134) 
rect(0,520,400,160) 


fill(53,96,106) 
quad(0,680,400,680,800,800,0,800) 

fill(255) 
beginShape() 
curveVertex(880,500) 
curveVertex(880,500) 
curveVertex(940,510) 
curveVertex(965,540) 
curveVertex(970,580) 
curveVertex(970,580) 
endShape()
#save("student.png")
done()
