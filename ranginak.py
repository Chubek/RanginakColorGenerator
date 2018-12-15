#############################################################################
###########################Ranginak Color Generator##########################
###########################Using Gizeh and Colrorsys#########################
###########################Copyright 2018 by Chubak Bidpaa###################
###########################No Licesne, free to use###########################
#############################################################################

#Read my blogpost: http://partlyshaderly.com/2018/12/15/ranginak-python-tri-shade-color-generator/


##########Color#########

import gizeh as gz
import colorsys
import random
import time


def generate_color(s_min, s_max):
    random.seed(time.time())
    h = random.randint(0, 100) / 100
    random.seed(time.time())
    v = random.randint(0, 100) / 100
    random.seed(time.time())
    s = random.randint(s_min, s_max) / 100
    color = colorsys.hsv_to_rgb(h, s, v)

    return color


def generate_color_master():
    color_master = []


    color_master.append(generate_color(1, 33))
    color_master.append(generate_color(33, 66))
    color_master.append(generate_color(66, 100))

    return color_master


def invert():
    inverted = []
    colors = generate_color_master()

    for color_tuple in colors:
        r = 1 - color_tuple[0]
        g = 1  - color_tuple[1]
        b = 1 - color_tuple[2]

        inverted.append((r, g, b))

    return inverted


def generate_shade_color(r, g, b, color_tuple):
    new_color = 0

    addition_r = (random.randint(1, random.randint(5, 9)) / 10) * r
    addition_g = (random.randint(1, random.randint(5, 9)) / 10) * g
    addition_b = (random.randint(1, random.randint(5, 9)) / 10) * b

    new_r = 0
    new_g = 0
    new_b = 0

    if r == 0:
        new_r = color_tuple[0] * 255
        new_g = color_tuple[1] + addition_g * 255
        new_b = color_tuple[2] + addition_b * 255
    elif g == 0:
        new_g = color_tuple[1] * 255
        new_r = color_tuple[0] + addition_r * 255
        new_b = color_tuple[2] + addition_b * 255
    elif b == 0:
        new_b = color_tuple[2] * 255
        new_g = color_tuple[1] + addition_g * 255
        new_r = color_tuple[0] + addition_r * 255


    if int(new_r) <= 255 and int(new_g) <= 255 and int(new_g <= 255):
        new_color = (new_r / 255, new_g / 255, new_b / 255)
    elif int(new_r) > 255:
        new_color = (1.00, new_g / 255, new_b / 255)
    elif int(new_g) > 255:
        new_color = (new_r / 255, 1.00, new_b / 255)
    elif (new_b) > 255:
        new_color = (new_r / 255, new_g / 255 , 1.00)



    return new_color


def generate_shade(r, g, b):
    colors = invert()
    bg = []
    mg = []
    fg = []

    for i in range(6):
        bg.append(generate_shade_color(r, g, b, colors[0]))
        mg.append(generate_shade_color(r, g, b, colors[1]))
        fg.append(generate_shade_color(r, g, b, colors[2]))


    return [bg, mg, fg]


#######Draw########

rect_w = 500
rect_h = 500

def generate_surface():
    surface = gz.Surface(width=int(rect_w * 7), height=int(rect_h * 3))

    return surface


def draw_sqr(color, x, y):
    sqr = gz.square(l=500, fill=color, xy=(x, y))


    r = int(color[0] * 255)
    g = int(color[1] * 255)
    b = int(color[2] * 255)
    string = "(" + str(r) + ", " + str(g) + ", " + str(b) + ")"
    text2 = gz.text(string, fontfamily="Tahoma", fontsize=24, fill=(0, 0, 0), xy=(x + 20, y + 20))
    text3 = gz.text(string, fontfamily="Tahoma", fontsize=23, fill=(1, 1, 1), xy=(x + 20, y + 20))

    return gz.Group([sqr, text2, text3])



def main_func(r, g, b):
    colors = generate_shade(r, g, b)
    original_color = generate_color_master()
    items = []

    bg = colors[0]
    mg = colors[1]
    fg = colors[2]

    items.append(draw_sqr(bg[0], 250, 250))
    items.append(draw_sqr(bg[1], 750, 250))
    items.append(draw_sqr(bg[2], 750 + 500, 250))
    items.append(draw_sqr(bg[3], 750 + 1000, 250))
    items.append(draw_sqr(bg[4], 750 + 1500, 250))
    items.append(draw_sqr(bg[5], 750 + 2000, 250))
    items.append(draw_sqr(original_color[0], 750 + 2500, 250))

    items.append(draw_sqr(mg[0], 250, 250 + 500))
    items.append(draw_sqr(mg[1], 750, 250 + 500))
    items.append(draw_sqr(mg[2], 750 + 500, 250 + 500))
    items.append(draw_sqr(mg[3], 750 + 1000, 250 + 500))
    items.append(draw_sqr(mg[4], 750 + 1500, 250 + 500))
    items.append(draw_sqr(mg[5], 750 + 2000, 250 + 500))
    items.append(draw_sqr(original_color[1], 750 + 2500, 250 + 500))

    items.append(draw_sqr(fg[0], 250, 250 + 1000))
    items.append(draw_sqr(fg[1], 750, 250 + 1000))
    items.append(draw_sqr(fg[2], 750 + 500, 250 + 1000))
    items.append(draw_sqr(fg[3], 750 + 1000, 250 + 1000))
    items.append(draw_sqr(fg[4], 750 + 1500, 250 + 1000))
    items.append(draw_sqr(fg[5], 750 + 2000, 250 + 1000))
    items.append(draw_sqr(original_color[2], 750 + 2500, 250 + 1000))


    return gz.Group(items)


if __name__ == "__main__":
    for i in range(12): #change this according to how many images you want
        group = main_func(0, 1, 1) #change this accordign to your color needs
        surface = generate_surface()
        group.draw(surface)
        surface.write_to_png("shade_" + str(i) + ".png")

