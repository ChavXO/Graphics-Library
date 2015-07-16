# TODO: handle negatives
import pygame
import math
import pygame.gfxdraw
import sys
import importlib
import types
import array
import inspect
import cairo
import colorsys
import random as r

# ---------Drawing and event constants -------#

#screen is initally set to none so it can be initialised in the size function
screen = None
cr = None
dc = None
ims = None
d_ims = None
height = 600
width = 600
frame_skip = 60
#sets to True if in drawing mode
drawing = False
#animation clock
clock = pygame.time.Clock()


#------------Colour constants-------------#
noFill = False
colour_mode = "RGB"
colour = None
#fill_colour is white by default
fill_colour = (255, 255, 255, 255)
r_scale = 255.0
b_scale = 255.0
g_scale = 255.0
a_scale = 255.0

#------------Shape constants ---------#
#TODO
smoothness = False
#says whether or not the user is currently drawing a compound shape
inShape = False
line_stroke = (0, 0, 0, 255)
stroke_weight = 2
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
    global d_ims
    global ims
    global dc
    global data
    global stroke_weight
    global width
    global fill_colour
    global height
    global draw_list
    global set_list
    global shape_border
    global no_fill
    global line_stroke
    colour_mode = "RGB"
    line_stroke = (0,0,0,255)
    height = h
    no_fill = False
    width = w
    stroke_weight = 2
    screen = pygame.display.set_mode([w, h])
    fill_colour = (255, 255, 255, 255)
    screen.fill((204, 204, 204))
    data = array.array('c', chr(0) * w * h * 4)
    pixels = pygame.surfarray.pixels2d(screen)
    d_ims = cairo.ImageSurface.create_for_data(
	pixels.data, cairo.FORMAT_ARGB32, w, h)
    ims = cairo.ImageSurface.create_for_data(
	pixels.data, cairo.FORMAT_ARGB32, w, h)
    
    cr = cairo.Context(ims)
    dc  = cairo.Context(d_ims)

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
        colour = convertToHSV(r, g, b, 255)
    if a != None:
        screen.set_alpha(a)
    screen.fill(colour)
    


def done(setup=None,draw=None):
    """drawing loop"""
    global drawing
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
    print module
    mymod = None
    
    # runs the code only in the main function of the student module
    # prevents double running
    
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
    
    global cr
    global d_ims
    
    while True:
        global frame_skip
        screen.fill
        
        if do_draw:
            global draw_list
            global drawing
            global draw_count
            global dc
            draw_count = 0
            drawing = True
            draw_list = []
            mymod.draw()
            drawing = False
            
        for event in pygame.event.get():
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
        
        clock.tick(frame_skip)
        pygame.display.flip()
        
        
        

def draw_from_list(alist):
    global fill
    global screen
    global smoothness
    for job in alist:
        #processes all draw
        p = sorted(job.keys())
        pic = job[p[2]]
        x = job[p[0]]
        y = job[p[1]]
        #print pic
        screen.blit(pic, (x, y))
        

#-----------------methods that change the internal state of the objects--------------------#

def convertToHSV(r, g, b, a):
    temp = colorsys.hsv_to_rgb(r / 255.0, g / 255.0, b / 255.0)
    color = []
    for i in range(len(temp)):
        color.append(temp[i] * 255)
    color.append(a)
    return color

def colorMode(mode, a = None, b = None, c = None):
    global colour_mode
    colour_mode = mode

def fill(r, g = None, b = None, a = None):
    global fill_colour
    colour = None
    if isinstance(r, types.TupleType):
        g = r[1]
        b = r[2]
        try:
            a = r[3]
        except:
            pass
        r = r[0]
    if a == None:
        a = 255
    if colour_mode == "RGB":
        if g == None and b == None:
            colour = (r, r, r, a)
        elif b == None:
            colour = (r, r, r, g)
        else:
            colour = (r, g, b, a)
    else:
        colour = convertToHSV(r, g, b, a)
    fill_colour = colour
    

def noFill():
    global no_fill
    no_fill = True

def smooth():
    global smoothness
    smoothness = True

def stroke(r, g = None, b = None, a = None):
    global line_stroke
    colour = None
    if isinstance(r, types.TupleType):
        g = r[1]
        b = r[2]
        try:
            a = r[3]
        except:
            pass
        r = r[0]
    if a == None:
        a = 255
    if colour_mode == "RGB":
        if g == None and b == None:
            colour = (r, r, r, a)
        elif b == None and a == None:
            colour = (r, r, r, b)
        else:
            colour = (r, g, b, a)
    else:
        colour = convertToHSV(r, g, b, a)
    line_stroke = colour    

def noStroke():
    global shape_border
    stroke(0, 0, 0, 0)
    
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
    global line_stroke
    global width
    global persis
    global height
    if drawing:
        dc.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
        dc.set_line_width(stroke_weight)
        dc.rectangle(x, y, w, h)
        dc.stroke_preserve()
        dc.set_source_rgba(fill_colour[0] / r_scale, fill_colour[1] / g_scale, fill_colour[2] / b_scale, fill_colour[3] / 255.0)
        dc.fill()
    else:
        cr.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
        cr.set_line_width(stroke_weight)
        cr.rectangle(x, y, w, h)
        cr.stroke_preserve()
        cr.set_source_rgba(fill_colour[0] / r_scale, fill_colour[1] / g_scale, fill_colour[2] / b_scale, fill_colour[3] / 255.0)
        cr.fill()

def point(x, y):
    cr.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
    cr.set_line_width(stroke_weight)
    cr.move_to(x, y)
    cr.line_to(x + 1, y + 1)
    cr.stroke()

def line(a,b,c,d):
    global job_count
    global draw_list
    global draw_count
    global line_stroke
    global strokeWeight
    if drawing:
        dc.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
        dc.set_line_width(stroke_weight)
        dc.move_to(a, b)
        dc.line_to(c,d)
        dc.stroke()
    else:
        cr.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
        cr.set_line_width(stroke_weight)
        cr.move_to(a, b)
        cr.line_to(c,d)
        cr.stroke()
    
def triangle(x1, y1, x2, y2, x3, y3):
    global job_count
    global fill_colour
    global drawing
    global draw_list
    global line_stroke
    global draw_count
    if drawing:
        dc.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
        dc.set_line_width(stroke_weight)
        dc.move_to(x1, y1)
        dc.line_to(x2, y2)
        dc.line_to(x3, y3)
        dc.close_path()
        dc.stroke_preserve()
        dc.set_source_rgba(fill_colour[0] / 255.0, fill_colour[1]/255.0, fill_colour[2] / 255.0, fill_colour[3] / 255.0)
        dc.move_to(x1, y1)
        dc.line_to(x2, y2)
        dc.line_to(x3, y3)
        dc.close_path()
        dc.fill()
    else:
        #include alpha
        cr.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
        cr.set_line_width(stroke_weight)
        cr.move_to(x1, y1)
        cr.line_to(x2, y2)
        cr.line_to(x3, y3)
        cr.close_path()
        cr.stroke_preserve()
        cr.set_source_rgba(fill_colour[0] / 255.0, fill_colour[1]/255.0, fill_colour[2] / 255.0, fill_colour[3] / 255.0)
        cr.move_to(x1, y1)
        cr.line_to(x2, y2)
        cr.line_to(x3, y3)
        cr.close_path()
        cr.fill()
    
        
    

def ellipse(x, y, w ,h):
    global job_count
    global fill_colour
    global draw_list
    global line_stroke
    global draw_count
    a = b = c = d = 0
    a = int(x - w / 2)
    b = int(y - h / 2)
    c = int(x + w / 2)
    d = int(y + h / 2)
    if drawing:
        dc.save()
        dc.translate(a + w / 2., b + h / 2.)
        dc.scale (w / 2., h / 2.)
        dc.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
        dc.set_line_width(stroke_weight)
        dc.set_line_width(stroke_weight * 0.04)
        dc.arc(0., 0., 1., 0., 2 * math.pi)
        dc.stroke_preserve()
        
        dc.set_source_rgba(fill_colour[0] / 255.0, fill_colour[1]/255.0, fill_colour[2] / 255.0, fill_colour[3] / 255.0)
        dc.fill()
        dc.restore()

    else:
        cr.save()
        cr.translate(a + w / 2., b + h / 2.)
        cr.scale (w / 2., h / 2.)
        cr.set_source_rgba(line_stroke[0] / r_scale, line_stroke[1] / g_scale, line_stroke[2] / b_scale, line_stroke[3] / 255.0)
        cr.set_line_width(stroke_weight)
        cr.set_line_width(stroke_weight * 0.04)
        cr.arc(0., 0., 1., 0., 2 * math.pi)
        cr.stroke_preserve()
        
        cr.set_source_rgba(fill_colour[0] / 255.0, fill_colour[1]/255.0, fill_colour[2] / 255.0, fill_colour[3] / 255.0)
        cr.fill()
        cr.restore()

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
    try:
        return [func.__name__ for func in mod.__dict__.itervalues() 
                if is_mod_function(mod, func)]
    except:
        return []

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


