# functions for graphic primitive operations

def draw_rect(length, width):
    # clamp sizes
    length = clamp_dimension(length)
    width = clamp_dimension(width)
    print("drawing rect:", length, "×", width)
    # do graphic operation

def draw_circle(radius):
    #clamp size
    radius = clamp_dimension(radius)
    print("drawing circle:", radius)
    # do graphic operation

def set_drawing_position(x, y):
    # clamp coords
    x = clamp_dimension(x)
    y = clamp_dimension(y)
    print("setting position: x =", x, ", y =", y)
    # do graphic operation

def clamp_dimension(val):
    max = 10
    # limit dimension to the range -max to +max
    if abs(val) > max:
        print("clamping", val, "to range")
        return max if val > 0 else -max
    else:
        return val

# function to draw primitive element

def draw_element(position, kind, spec):
    # validate position parameter
    if not isinstance(position, tuple) or len(position) != 2:
        return
    
    # set position
    x, y = position  # assign tuple elements
    set_drawing_position(x, y)
    
    if kind == "rect":
        l, w = spec  # assign tuple elements
        draw_rect(l, w)
    
    elif kind == "circle":
        draw_circle(spec)


# create drawing

''' Drawing is a sequence of graphic-element groups.
    Each group has a sequence of graphic primitive specifications. 
    Each graphic primitive spec has a drawing position, a primitive
    kind, and specs for the primitive, based on the kind.
'''
group_1 = [
    ((2, -8), "circle", 3.6),   # circle, radius 3, at (2, -8)
    ((3, 6), "rect", (2,12))    # rectangle, 2 × 2, at (3, 6)
    ]

group_2 = [
    ((-16, -11), "rect", (4,3)), # rectangle, 4 × 3, at (-16, -11)
    ((8, -9), "circle", 15),     # circle, radius 15, at (8, -9)
    ((3, 19), "rect", (5,6))     # rectangle, 5 × 6, at (3, 19)
    ]

drawing = [group_1, group_2]


# draw the drawing!

for group in drawing:
    print("start group:")
    for p, k, s in group:  # get each primitive spec tuple and expand into components
        draw_element(p, k, s)
    print("end group\n")
