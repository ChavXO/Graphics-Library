try:
    from tkinter import *
except:
    from Tkinter import *
import math
_root = Tk()
_root.withdraw()
_root.resizable(width=False, height=False)

class MyCanvas(Canvas):
    def __init__(self, width, height):
        master = Toplevel(_root)
        Canvas.__init__(self, master, width= width, height=height)
        _root.geometry(str(width) + "x" + str(height))
        self.pack()
        self.items = []
        #_root.after(100, MyCanvas.hello)
        _root.update()

    def hello(self):
        print "hi"

    def addItem(self, shape):
        self.items.append(shape)

class Drawable(object):
    options = {"width":1, "fill":"white", "outline":"black"}
    def __init__(self):
        self.canvas = None
        self.id = None

    def draw(self, mycanvas):
        self.canvas = mycanvas
        self.obj = self._draw(mycanvas)
        mycanvas.addItem(self.obj)
        _root.update()

    def _draw(self, canvas):
        pass

class Point(Drawable):
    def __init__(self, x, y):
        Drawable.__init__(self)
        self.x = x
        self.y = y
        

    def _draw(self, canvas):
        ep = 1
        x2 = self.x + ep
        y2 = self.y + ep
        return canvas.create_line(self.x, self.y, x2, y2)

class Line(Drawable):
    options = {"width":1}
    def __init__(self, x1, y1, x2, y2):
        Drawable.__init__(self)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def _draw(self, canvas):
        return canvas.create_line(self.x1, self.y1, self.x2, self.y2, Line.options)
    

class Rectangle(Drawable):
    def __init__(self, points):
        Drawable.__init__(self)
        self.points = points

    def _draw(self, canvas):
        return canvas.create_polygon(self.points, Drawable.options)

class Arc(Drawable):
    def __init__(self):
        pass

class Ellipse(Drawable):
    def __init__(self, points):
        Drawable.__init__(self)
        self.points = points

    def _draw(self, canvas):
        return canvas.create_oval(self.points, Drawable.options)

class Circle(Ellipse):
    def __init__(self):
        pass

class Polygon(Drawable):
    def __init__(self, points):
        Drawable.__init__(self)
        self.points = points

    def _draw(self, canvas):
        return canvas.create_polygon(self.points, Drawable.options)

class Triangle(Drawable):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        Drawable.__init__(self)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.points=[x1,y1,x2,y2,x3,y3]

    def _draw(self, canvas):
        return canvas.create_polygon(self.points, Drawable.options)

class Quad(Drawable):
    def __init__(self, points):
        Drawable.__init__(self)
        self.points = points

    def _draw(self, canvas):
        return canvas.create_polygon(self.points, Drawable.options)

w = None    
colour = None
colour_mode = "RGB"
inShape = False

def size(width, height):
    global w
    w = MyCanvas(width=width, height=height)
    colour = '#%02x%02x%02x' % (204, 204, 204)
    w.config(background=colour)

def background(r, g = None, b = None):
    colour = None
    if colour_mode == "RGB":
        if g == None and b == None:
            colour = '#%02x%02x%02x' % (r, r, r)
        else:
            colour = '#%02x%02x%02x' % (r, g, b)
    else:
        h = s = v = c = x = m = None
        h = r
        s = g
        v = b

        c = v * s
        x = c * (1 - abs(((h / 60) % 2) - 1))
        m = v - c
        d = e = f = None
        if h >= 0 and h < 60:
            (d, e, f) = c, x, 0
        elif h >= 60 and h < 120:
            (d, e, f) = x, c, 0
        elif h >= 120 and h < 180:
            (d, e, f) = 0, c, x
        elif h >= 180 and h < 240:
            (d, e, f) = 0, x, c
        elif h >= 240 and h < 300:
            (d, e, f) = x, 0, c
        elif h >= 300 and h < 360:
            (d, e, f) = c, 0, x
        red = green = blue = None
        (red, green, blue) = (d + m) * 255, (e + m) * 255, (f + m) * 255
        colour = '#%02x%02x%02x' % (red, green, blue)
    w.config(background = colour)

def getShapes():
    for item in w.items:
        w.move(item, 50, 50)

def point(x, y):
    p = Point(x, y)
    p.draw(w)
    
def fill(r, g = None, b = None):
    colour = None
    if colour_mode == "RGB":
        if g == None and b == None:
            colour = '#%02x%02x%02x' % (r, r, r)
        else:
            colour = '#%02x%02x%02x' % (r, g, b)
    else:
        h = s = v = c = x = m = None
        h = (r / 360.0) * 360
        s = g / 255.0
        v = b / 255.0

        c = v * s
        x = c * (1 - abs(((h / 60) % 2) - 1))
        m = v - c
        d = e = f = None
        if h >= 0 and h < 60:
            (d, e, f) = c, x, 0
        elif h >= 60 and h < 120:
            (d, e, f) = x, c, 0
        elif h >= 120 and h < 180:
            (d, e, f) = 0, c, x
        elif h >= 180 and h < 240:
            (d, e, f) = 0, x, c
        elif h >= 240 and h < 300:
            (d, e, f) = x, 0, c
        elif h >= 300 and h < 360:
            (d, e, f) = c, 0, x
        red = green = blue = None
        (red, green, blue) = (d + m) * 255, (e + m) * 255, (f + m) * 255
        colour = '#%02x%02x%02x' % (red, green, blue)
    Drawable.options["fill"] = colour

def noFill():
    Drawable.options["fill"] = None

def line(a,b,c,d):
    l = Line(a,b,c,d)
    l.draw(w)
    
def triangle(x1, y1, x2, y2, x3, y3):
    t = Triangle(x1, y1, x2, y2, x3, y3)
    t.draw(w)

def stroke(r, g = None, b = None):
    colour = None
    if colour_mode == "RGB":
        if g == None and b == None:
            colour = '#%02x%02x%02x' % (r, r, r)
        else:
            colour = '#%02x%02x%02x' % (r, g, b)
    else:
        h = s = v = c = x = m = None
        h = (r / 360.0) * 360
        s = g / 255.0
        v = b / 255.0
        c = v * s
        
        x = c * (1 - abs(((h / 60.0) % 2) - 1))
        m = v - c
        d = e = f = None
        if h >= 0 and h < 60:
            (d, e, f) = c, x, 0
        elif h >= 60 and h < 120:
            (d, e, f) = x, c, 0
        elif h >= 120 and h < 180:
            (d, e, f) = 0, c, x
        elif h >= 180 and h < 240:
            (d, e, f) = 0, x, c
        elif h >= 240 and h < 300:
            (d, e, f) = x, 0, c
        elif h >= 300 and h < 360:
            (d, e, f) = c, 0, x
        red = green = blue = None
        (red, green, blue) = min(255, (d + m) * 255), min(255, (e + m) * 255), min(255, (f + m) * 255)
        #print red, green, blue
        colour = '#%02x%02x%02x' % (red, green, blue)
    Drawable.options["outline"] = colour
    Line.options["fill"] = colour
    

def noStroke():
    Drawable.options["width"] = 0
    Drawable.options["outline"] = ""
    Line.options["width"] = 0

def strokeWeight(n):
    Line.options["width"] = n
    Drawable.options["width"] = n

def strokeCap(cap):
    if cap == "ROUND":
        Line.options["capstyle"] = ROUND
    elif cap == "SQUARE":
        Line.options["capstyle"] = BUTT
    elif cap == "PROJECT":
        Line.options["capstyle"] = PROJECTING

def strokeJoin(join):
    if join == "BEVEL":
        Drawable.options["joinstyle"] = BEVEL
    elif join == "MITER":
        Drawable.options["joinstyle"] = MITER
    elif join == "ROUND":
        Drawable.options["joinstyle"] = ROUND
    

def smooth():
    #Drawable.options["smooth"] = True
    Line.options["smooth"] = True
    Line.options["capstyle"] = ROUND
    pass
    
def rect(x1,y1,width,height):
    x2 = y2 = x3 = y3 = x4 = y4 = 0
    x2 = x1 + width
    y2 = y1
    x3 = x2
    y3 = y1 + height
    x4 = x1
    y4 = y3
    points = [x1,y1,x2,y2, x3, y3, x4, y4]
    
    r = Rectangle(points)
    r.draw(w)

def ellipse(x, y, width ,height):
    a = b = c = d = 0
    a = x - width/2
    b = y - height/2
    c = x + width/2
    d = y + height/2
    points = [a,b,c,d]
    e = Ellipse(points)
    e.draw(w)

v_params = []
def beginShape():
    global inShape
    global curveParams
    global v_params
    curveParams = []
    v_params = []
    inShape = True

m = 3
def endShape(c = None):
    global inShape
    inShape = False
    global m
    m = 3
    if curveParams != []:
        if c == None:
            knot = StandardKnot()
            if len(knot) == 0:
                return
            x = curveParams[0][0]
            y = curveParams[0][1]
            t = 0.0
            step = 0.1
            L = len(curveParams)
            ppoints = []
            while t <= L - m  + 1:
                p = P(t,knot,Nopen)
                #l = Line(x, y, p[0], p[1])
                #l.draw(w)
                ppoints.append([x,y,p[0],p[1]])
                x = p[0]
                y = p[1]
                t = t + step
            poly = Polygon(ppoints)
            poly.draw(w)                 
        else:
           L = len(curveParams)
           knot = range(L) 
           p = P(0.0,knot,Nclosed)
           x = p[0]
           y = p[1]
           step = 0.1
           t = step
           L = len(points)
           while t <= L:
               p = P(t,knot,Nclosed)
               l = Line(x, y, p[0], p[1])
               l.draw(w)
               x = p[0]
               y = p[1]
               t = t + step
    if v_params != []:
        print v_params
        q = Polygon(v_params)
        q.draw(w)

def Nclosed(k,m,t,knot):
    L = len(curveParams)
    z = mod(t-k,L)
    if z <= 0:
        z += L
    return Nopen(0,m,z,knot)

def P(t,knot,Ncycle):
    L = len(curveParams)
    SumX = 0.0
    SumY = 0.0
    for k in range(L):
        n = Ncycle(k,m,t,knot)
        SumX = SumX + n * curveParams[k][0]
        SumY = SumY + n * curveParams[k][1]
    return [SumX,SumY]

def mod(a,b):
    return ( a % b)

def StandardKnot():
    m = 3
    knot = []
    L = len(curveParams) - 2
    if L <= m -2 :
        print 'make more points than m'
        return []
    for i in range(m - 1):
        knot.append(0)
    for i in range(L - m + 3):
        knot.append(i)
    for i in range(m):
        knot.append(L - m + 3)
    return knot

def Nopen(k,m,t,knot):
    if m <= 1:
        if t < knot[k] or t >= knot[k + 1]:
            Sum = 0.0
        else:
            Sum = 1.0
    else:
        d = knot[k+m-1]-knot[k]
        if d <> 0:
            Sum = (t-knot[k])*Nopen(k,m-1,t,knot)/d
        else:
            Sum = 0.0
        d = knot[k+m] - knot[k+1]
        if d <> 0:
            Sum = Sum + (knot[k+m] - t)*Nopen(k + 1,m-1,t,knot)/d
    return Sum

curveParams = []
def curveVertex(x, y):
    global curveParams
    curveParams.append([x,y])

def vertex(x, y):
    global v_params
    v_params.append([x,y])

def quad(x1, y1, x2, y2, x3, y3, x4, y4):
    points = [x1, y1, x2, y2, x3, y3, x4, y4, x1, y1]
    q = Quad(points)
    q.draw(w)

def colorMode(mode):
    global colour_mode
    colour_mode = mode
"""
def save(file_name):
    w.postscript(file="circles.eps")
    from PIL import Image
    img = Image.open("circles.eps")
    img.save(filename, "png")
"""
def done():
    _root.mainloop()
