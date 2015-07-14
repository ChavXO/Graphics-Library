# TODO: handle negatives
import pygame
import math
import pygame.gfxdraw
import sys
import importlib
import types
import inspect
import cairo
import random as r

# ---------Drawing and event constants -------#

#screen is initally set to none so it can be initialised in the size function
screen = None
cr = None
ims = None
height = 600
width = 600
#contains a list of dictionaries of static drawing jobs to be processed
jobs = None
#contains a list of dictionaries of dynamic objects to be drawn
draw_list = []
frame_skip = 60
#sets to True if in drawing mode
drawing = False
setting = False
#keeps a count of the jobs
#I forgot why I made this - makes sure you add to the last index of the list
#considering using a linked list
job_count = None
draw_count = None
#animation clock
clock = pygame.time.Clock()


#------------Colour constants-------------#
noFill = False
colour_mode = "RGB"
colour = None
#fill_colour is white by default
fill_colour = (255, 255, 255)


#------------Shape constants ---------#
#TODO
smoothness = False
#says whether or not the user is currently drawing a compound shape
inShape = False
line_stroke = (0, 0, 0)
stroke_weight = 1
shape_border = True
v_params = []
curveParams = []
m = 3

# ----------key and mouse constants------------#
key = None
mouseX = None
mouseY = None
isMousePressed = None


#-----------setup methods --------------#
def size(w, h):
    global screen
    global jobs
    global job_count
    global draw_count
    global fill
    global cr
    global ims
    global stroke_weight
    global width
    global fill_colour
    global height
    global draw_list
    global set_list
    global shape_border
    shape_border = True
    height = h
    width = w
    stroke_weight = 1
    screen = pygame.display.set_mode([width, height]).convert_alpha()
    fill_colour = (255, 255, 255)
    screen.fill((204, 204, 204))
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, 400, 400)
    cr = cairo.Context(ims)
    jobs = []
    draw_list = []
    set_list = []
    job_count = 0
    draw_count = 0

def background(r, g = None, b = None, a = None):
    global screen
    global width
    global height
    colour = None
    if colour_mode == "RGB":
        if g == None and b == None:
            colour = (r, r, r)
        else:
            colour = (r, g, b)
    else:
        colour = convertToHSV(r, g, b)
    if a != None:
        screen.set_alpha(a)
    screen.fill(colour)
    


def done(setup=None,draw=None):
    """drawing loop"""
    
    # inspects gets a stack trace of methods and their calling order
    # the item at index one will always be the calling function and details
    # about it

    # this assumes that the student code and this module will
    # be in the same folder
    module = inspect.stack()[1][1]

    #finds the index of the last slash to cut out the path
    k = module.rfind("\\")
    if k == -1:
        k = module.rfind("/")
    module = module[k + 1: -3]
    mymod = None
    
    # runs the code only in the main function of the student module
    # prevents double running
    if __name__ == "sample":
        mymod =  __import__(module)
    all_functions = list_functions(mymod)
    mymod.height = height
    mymod.width = width
    
    if "setup" in all_functions:
        mymod.setup()

    do_draw = False
    mouse_pressed = False
    key_pressed = False

    # sets the above defined booleans to true if any of the functions
    # is overridden
    for function in all_functions:
        if function == "draw":
            do_draw = True
        if function == "keyPressed":
            global key
            key_pressed = True
        if function == "mousePressed":
            mouse_pressed = True
            
    while True:
        global frame_skip
        if do_draw:
            global draw_list
            global drawing
            global draw_count
            draw_count = 0
            drawing = True
            draw_list = []
            mymod.draw()
            drawing = False
        
        for event in pygame.event.get():
            key = "P"
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mymod.mouseX = pygame.mouse.get_pos()[0]
                mymod.mouseY = pygame.mouse.get_pos()[1]
                mymod.isMousePressed = True 
                if mouse_pressed:
                    mymod.mousePressed()
            elif event.type == pygame.MOUSEBUTTONUP:
                mymod.isMousePressed = False
            elif event.type == pygame.KEYDOWN:
                if key_pressed:
                    mymod.key = pygame.key.name(event.key)
                    mymod.keyPressed()
                    
        #process static objects
        draw_from_list(jobs)
        #process drawing list
        draw_from_list(draw_list)
        clock.tick(frame_skip)
        pygame.display.flip()    

def draw_from_list(alist):
    global fill
    global smoothness
    for job in alist:
        #processes all draw
        if job["name"] == "draw":
            #draws a rectangle
            if job["shape"] == "rect":
                x1 = job["points"][0]
                y1 = job["points"][1]
                x2 = job["points"][0] + job["width"]
                y2 = job["points"][1] + job["height"]
                pygame.draw.rect(screen, job["colour"], ([x1, y1], [job["width"], job["height"]]),job["thickness"])
            #draws triangle primi
            if job["shape"] == "triangle":
                if smoothness:
                    points = job["points"]
                    x1 = points[0][0]
                    y1 = points[0][1]
                    x2 = points[1][0]
                    y2 = points[1][1]
                    x3 = points[2][0]
                    y3 = points[2][1]
                    pygame.gfxdraw.aatrigon(screen, x1, y1, x2, y2, x3, y3, job["border"])
                    pygame.gfxdraw.filled_trigon(screen, x1, y1, x2, y2, x3, y3, job["colour"]) 
                else:
                    pygame.draw.polygon(screen, job["colour"],job["points"], job["width"])
            if job["shape"] == "ellipse":
                if not smoothness:
                    pygame.draw.ellipse(screen, job["colour"],job["points"], job["width"])
                    pygame.draw.ellipse(screen, job["outline_colour"],job["points"], job["border_width"])
                else:
                    pygame.gfxdraw.aaellipse(screen, int(job["points"][0] + job["points"][2]/2), int(job["points"][1] + job["points"][3]/2), int(job["points"][2]/2), int(job["points"][3]/2), job["outline_colour"])
                    pygame.gfxdraw.filled_ellipse(screen, int(job["points"][0] + job["points"][2]/2), int(job["points"][1] + job["points"][3]/2), int(job["points"][2]/2), int(job["points"][3]/2), job["colour"])
                    
            if job["shape"] == "line":
                if smoothness:
                    pygame.draw.aaline(screen, job["colour"],job["start"],job["end"], job["width"])
                else:
                    pygame.draw.line(screen, job["colour"],job["start"],job["end"], job["width"])

#-----------------methods that change the internal state of the objects--------------------#

def convertToHSV(r, g, b):
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
    return (red, green, blue)

def colorMode(mode, a = None, b = None, c = None):
    global colour_mode
    colour_mode = mode

def fill(r, g = None, b = None):
    global fill_colour
    colour = None
    if isinstance(r, types.TupleType):
        g = r[1]
        b = r[2]
        r = r[0]
    if colour_mode == "RGB":
        if g == None and b == None:
            colour = (r, r, r)
        else:
            colour = (r, g, b)
    else:
        colour = convertToHSV(r, g, b)
    fill_colour = colour
    

def noFill():
    global noFill
    noFill = True

def smooth():
    global smoothness
    smoothness = True

def stroke(r, g = None, b = None):
    global line_stroke
    colour = None
    if colour_mode == "RGB":
        if g == None and b == None:
            colour = (r, r, r)
        else:
            colour = (int(r), int(g), int(b))
    else:
        colour = convertToHSV(r, g, b)
    line_stroke = colour    

def noStroke():
    global shape_border
    strokeWeight(0)
    shape_border = False
    
def strokeWeight(n):
    global stroke_weight
    stroke_weight = n

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

#-------------draw shape primitives------------------------#
def rect(x, y, w, h):
    global job_count
    global draw_list
    global draw_count
    global set_list
    if drawing:
        draw_list.append({"name": "draw", "shape": "rect"})
        draw_list[draw_count]["points"] = [x,y]
        draw_list[draw_count]["colour"] = (fill_colour)
        draw_list[draw_count]["width"] = w
        draw_list[draw_count]["height"] = h
        draw_list[draw_count]["thickness"] = 0
        draw_list[draw_count]["border"] = shape_border
        draw_count += 1
        if draw_list[draw_count - 1]["border"]:
            draw_list.append({"name": "draw", "shape": "rect"})
            draw_list[draw_count]["points"] = [x,y]
            draw_list[draw_count]["colour"] = (0,0,0)
            draw_list[draw_count]["width"] = w
            draw_list[draw_count]["height"] = h
            draw_list[draw_count]["thickness"] = 1
            draw_count += 1
    else:    
        jobs.append({"name": "draw", "shape": "rect"})
        jobs[job_count]["points"] = [x,y]
        jobs[job_count]["colour"] = (fill_colour)
        jobs[job_count]["width"] = w
        jobs[job_count]["height"] = h
        jobs[job_count]["thickness"] = 0
        job_count += 1
        jobs.append({"name": "draw", "shape": "rect"})
        jobs[job_count]["points"] = [x,y]
        jobs[job_count]["colour"] = (0,0,0)
        jobs[job_count]["width"] = w
        jobs[job_count]["height"] = h
        jobs[job_count]["thickness"] = 1
        job_count += 1

def point(x, y):
    p = Point(x, y)
    p.draw(w)

def line(a,b,c,d):
    global job_count
    global draw_list
    global draw_count
    global line_stroke
    global strokeWeight
    if drawing:
        draw_list.append({"name": "draw", "shape": "line"})
        draw_list[draw_count]["start"] = [a,b]
        draw_list[draw_count]["end"] = [c,d]
        draw_list[draw_count]["colour"] = (line_stroke)
        draw_list[draw_count]["width"] = stroke_weight
        draw_count += 1
    else:
        jobs.append({"name": "draw", "shape": "line"})
        jobs[job_count]["start"] = [a, b]
        jobs[job_count]["end"] = [c, d]
        jobs[job_count]["colour"] = (line_stroke)
        jobs[job_count]["width"] = stroke_weight
        job_count += 1
    
def triangle(x1, y1, x2, y2, x3, y3):
    global job_count
    global fill_colour
    global drawing
    global draw_list
    global draw_count
    if drawing:
        draw_list.append({"name": "draw", "shape": "triangle"})
        draw_list[draw_count]["colour"] = fill_colour
        draw_list[draw_count]["points"] = [[x1,y1],[x2,y2],[x3,y3]]
        draw_list[draw_count]["width"] = 0
        draw_list[draw_count]["border"] = line_stroke
        draw_count += 1
        draw_list.append({"name": "draw", "shape": "triangle"})
        draw_list[draw_count]["colour"] = fill_colour
        draw_list[draw_count]["points"] = [[x1,y1],[x2,y2],[x3,y3]]
        draw_list[draw_count]["width"] = 1
        draw_list[draw_count]["border"] = line_stroke
        draw_count += 1
    else:
        jobs.append({"name": "draw", "shape": "triangle"})
        jobs[job_count]["colour"] = fill_colour
        jobs[job_count]["points"] = [[x1,y1],[x2,y2],[x3,y3]]
        jobs[job_count]["width"] = 0
        jobs[job_count]["border"] = line_stroke
        job_count += 1
        jobs.append({"name": "draw", "shape": "triangle"})
        jobs[job_count]["colour"] = fill_colour
        jobs[job_count]["points"] = [[x1,y1],[x2,y2],[x3,y3]]
        jobs[job_count]["border"] = line_stroke
        jobs[job_count]["width"] = 1
        job_count += 1
    

def ellipse(x, y, w ,h):
    global job_count
    global fill_colour
    global draw_list
    global draw_count
    a = b = c = d = 0
    a = int(x - w / 2)
    b = int(y - h / 2)
    c = int(x + w / 2)
    d = int(y + h / 2)
    if drawing:
        draw_list.append({"name": "draw", "shape": "ellipse"})
        draw_list[draw_count]["points"] = (a, b, w, h)
        draw_list[draw_count]["colour"] = fill_colour
        draw_list[draw_count]["outline_colour"] = line_stroke
        draw_list[draw_count]["border_width"] = stroke_weight
        draw_list[draw_count]["width"] = 0
        draw_count += 1

    else:
        jobs.append({"name": "draw", "shape": "ellipse"})
        jobs[job_count]["points"] = (a,b, w, h)
        jobs[job_count]["outline_colour"] = line_stroke
        jobs[job_count]["border_width"] = stroke_weight
        jobs[job_count]["colour"] = fill_colour
        jobs[job_count]["width"] = 0
        job_count += 1

def beginShape():
    global inShape
    global curveParams
    global v_params
    curveParams = []
    v_params = []
    inShape = True


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

#------------shape drawing helper methods--------------#

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

def is_mod_function(mod, func):
    """checks if the given function func is a user defined function
        and if it is in the given method."""
    return inspect.isfunction(func) and inspect.getmodule(func) == mod

def list_functions(mod):
    """returns a list of all the user defined functions in the given modules.
        Used to extract user functions from modules for the purposes of
        overrriding or implementing them."""
    return [func.__name__ for func in mod.__dict__.itervalues() 
            if is_mod_function(mod, func)]

#-----------------------processing functions------------------------------#

def random(a = None, b = None):
    if a == None and b == None:
        return r.random()
    elif b == None:
        return r.randrange(a)
    else:
        return int(r.uniform(a, b))

def frameRate(num):
    global frame_skip
    frame_skip = num
