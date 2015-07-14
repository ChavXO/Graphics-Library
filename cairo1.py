import math
from cairo import *
s = Surface()
cr = Context(s)
radial = cairo.RadialGradient(0.25, 0.25, 0.1,  0.5, 0.5, 0.5)
radial.add_color_stop_rgb(0,  1.0, 0.8, 0.8)
radial.add_color_stop_rgb(1,  0.9, 0.0, 0.0)

for i in range(1, 10):
    for j in range(1, 10):
        cr.rectangle(i/10.0 - 0.04, j/10.0 - 0.04, 0.08, 0.08)
cr.set_source(radial)
cr.fill()

linear = cairo.LinearGradient(0.25, 0.35, 0.75, 0.65)
linear.add_color_stop_rgba(0.00,  1, 1, 1, 0)
linear.add_color_stop_rgba(0.25,  0, 1, 0, 0.5)
linear.add_color_stop_rgba(0.50,  1, 1, 1, 0)
linear.add_color_stop_rgba(0.75,  0, 0, 1, 0.5)
linear.add_color_stop_rgba(1.00,  1, 1, 1, 0)

cr.rectangle(0.0, 0.0, 1, 1)
cr.set_source(linear)
cr.fill()
