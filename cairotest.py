import cairo
 
w, h = 128, 128
 
# Setup Cairo
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, w, h)
ctx = cairo.Context(surface)
 
# Set thickness of brush
ctx.set_line_width(15)
 
# Draw out the triangle using absolute coordinates
ctx.move_to(w/2, h/3)
ctx.line_to(2*w/3, 2*h/3)
ctx.rel_line_to(-1*w/3, 0)
ctx.close_path()
 
# Apply the ink
ctx.stroke()
 
 #!/usr/bin/env python
import sys, cStringIO, pygame, pygame.locals, sys
 
pygame.init()
 
f = cStringIO.StringIO()
surface.write_to_png(f)
 
screen = pygame.display.set_mode((w, h))
screen.fill((255, 255, 255))
 
f.seek(0)
pic = pygame.image.load(f,'temp.png')#.convert_alpha()
 
clock = pygame.time.Clock()
i = -128
while True:
    if i > 127:
        i = -128
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    screen.blit(pic, (i, 0))
    i += 1
    pygame.display.flip()
    clock.tick(30)
