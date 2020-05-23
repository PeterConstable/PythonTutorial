# functions for graphic primative operations

def draw_rect(length, width):
    print("drawing rect:", length, "×", width)
    # do graphic operation

def draw_circle(radius):
    print("drawing circle:", radius)
    # do graphic operation

def set_drawing_position(x, y):
    print("setting position: x =", x, ", y =", y)
    # do graphic operation


# function to draw primative element

def draw_element(position, kind, spec):
    x, y = position  # assign tuple elements
    set_drawing_position(x, y)

    if kind == "rect":
        l, w = spec  # assign tuple elements
        draw_rect(l, w)
        
    elif kind == "circle":
        draw_circle(spec)


# create drawing

''' Drawing is a sequence of graphic-element groups.
    Each group has a sequence of graphic primitive specs. 
    Each graphic primitive spec has a drawing position, a primative
    kind, and specs for the primative, based on the kind.
'''
group_1 = [
    ((2, -8), "circle", 3.6),   # circle, radius 3, at (2, -8)
    ((3, 6), "rect", (2,2))     # rectangle, 2 × 2, at (3, 6)
    ]

group_2 = [
    ((-6, 11), "rect", (4,3)),  # rectangle, 4 × 3, at (-6, 11)
    ((8, -9), "circle", 6),     # circle, radius 6, at (8, -9)
    ((3, 19), "rect", (5,6))    # rectangle, 5 × 6, at (3, 19)
    ]

drawing = [group_1, group_2]

for group in drawing:
    print("start group:")
    for p, k, s in group:
        draw_element(p, k, s)
    print("end group\n")
