# Our First Program

In the past few lessons, we've learned about a number of useful parts of Python:

* Comparison and logical expressions
* Ternary operator ```if```...```else```
* Sequence types: strings, lists, tuples and ranges
* Multiple assignment operations
* Flow-control statements: ```if```, ```while``` and ```for```
* Defining functions

That's enough to be able to start doing some interesting programming. In this lesson, we'll put together a program that several of the things mentioned above.

* [Overview](#overview)
* [Functions for graphic primitive operations](#functions-for-graphic-primitive-operations)
* [Function to draw a graphic primitive](#function-to-draw-a-graphic-primitive)
* [Organizing the drawing data](#organizing-the-drawing-data)
* [Statements to draw the complete drawing](#statements-to-draw-the-complete-drawing)
* [Running the program](#running-the-program)
* [What's next](#whats-next)

## Overview

Our program will similate drawing an illustration with different graphic primitives. We won't actually display a graphic illustration in some canvas; we'll just use print statements to indicate the graphic operations that would take place.

We'll represent our drawing as a sequence of graphic-element groups, each of which can have several graphic primitives. And we'll define different functions for different levels of processing: from the complete drawing down to the individual kind of graphic primitive. It might sound complex, but we'll see it's actually fairly simple using the mechanisms we've learned.

We're assuming you're still working in interactive mode. Several things, like defining the functions will require multi-line entry. The longest multi-line statement will be 10 lines, if you omit comments or blank lines that we'll show to provide better clarity. We've provided a file with the sample code, [drawing.py](LessonSamples\Lesson9\drawing.py). If you want, you can copy fragments from there and paste them into your interactive mode session.

You can also enter fragments in interactive mode in the order presented below. In some sections in this page, we may describe a function step by-step. If you copy from this page and paste, you should copy the complete function definition that will be provided at the end of that section.

When you enter a multi-line statement (e.g., a function definition), make sure to press ```Enter``` at the end to get out of multi-line-edit mode and complete the statement (you want to get back to the ```>>>``` prompt).

## Functions for graphic primitive operations

We'll start at the bottom of the stack. We'll allow for two kinds of graphic primitives, circles and rectangles, and will define a function for drawing each. We'll also define a function to set the drawing position; this will need to be called before each of the drawing functions.

As mentioned above, we won't actually do real graphic operations in this sample; we'll just use ```print()``` statements to indicate the graphic operations we would be doing. These functions are the only parts of our program that will be "dumbed down" in this way.

We'll enforce a policy to limit an drawing position or primitive dimension to a certain range. For that, we'll define a function that clamps values:

```python
def clamp_dimension(val):
    max = 10
    # limit dimension to the range -max to +max
    if abs(val) > max:
        print("clamping", val, "to range")
        return max if val > 0 else -max
    else:
        return val
```

Here we're using an ```if``` statement to check if the magnitude (```abs()```) of the dimension passed is out of range. Then we use the ternary ```if```...```else``` operator to pass the clamped value, positive or negative as needed.

First, we define functions for drawing rectangles and circles:

```python
def draw_rect(length, width):
    # clamp sizes
    length = clamp_dimension(length)
    width = clamp_dimension(width)
    print("drawing rect:", length, "×", width)
    # do graphic operation
```

```python
def draw_circle(radius):
    #clamp size
    radius = clamp_dimension(radius)
    print("drawing circle:", radius)
    # do graphic operation
```

Next our function for setting the drawing position.

```python
def set_drawing_position(x, y):
    # clamp coords
    x = clamp_dimension(x)
    y = clamp_dimension(y)
    print("setting position: x =", x, ", y =", y)
    # do graphic operation
```

That's all of our primitive-operation functions defined.

## Function to draw a graphic primitive

Next, we'll define a function to draw each graphic primitive—each circle or rectangle. To draw each primitive, we need three parameters:

* A drawing position
* The kind of primitive to draw
* The primitive-specific specs

Our function definition will have three parameter values for these items.

```python
def draw_element(position, kind, spec):
```

The ```position``` parameter will be a coordinate-pair tuple; ```kind``` will be a string; and ```spec``` will be a number or tuple of numbers, according to what's required for the kind of primitive.

Next, we'll do a bit of validation for the ```position``` parameter to make sure the argument passed is a tuple with two elements. If not, we'll just exit early to ignore the call.

```python
    if not isinstance(position, tuple) or len(position) != 2:
        return
```

> To be more complete, we'd also validate that the `spec` parameter matched the `kind` of primitive to be drawn. That's left as an exercise for the reader!

Then we need to call ```set_drawing_position()``` to set the drawing position. To set up for that, we'll assign the tuple elements to separate variables for the function arguments.

```python
    x, y = position  # assign tuple elements
    set_drawing_position(x, y)
```

Finally we're ready to draw the primitive. We need to branch according to the kind of primitive.

```python
    if kind == "rect":
        l, w = spec  # assign tuple elements
        draw_rect(l, w)

    elif kind == "circle":
        draw_circle(spec)
```

Here's our complete function definition:

```python
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
```

## Organizing the drawing data

We're ready to design how we'll organize data for a drawing. From the top level:

* A drawing will be a sequence of graphic-element groups.
* Each group will be a sequence of graphic primitive specifications.

For each of these, we could use either a list or a tuple. Our program doesn't need to edit the sequences, so tuples would make sense. But for a little diversity in this sample, we'll use lists for both.

In designing the definition of ```draw_element()```, we already determined what would be required for each graphic primitive specification:

* drawing position—a tuple of two numbers
* primitive kind—a string
* kind-specific specs—a number or tuple of numbers.

We could use a single multi-line statement to define an entire drawing, but for easier entry we'll define each group separately and then assemble the overall drawing.

```python
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
```

Some of the dimensions we've used in the data will hit our policy on maximum size.

## Statements to draw the complete drawing

Now we can write the top-level statements needed to draw a complete drawing.

To start, we'll take ```drawing``` and iterate over the contained groups in a ```for``` loop.

For each group, we'll interate over the graphic primitive specifications using a nested ```for``` loop.

As we loop over each primitive specification, we need to get variables for the three components: the position, the kind, and the kind-specific details. We'll incorporate multiple variable assignment into the nested ```for``` statement.

Our statements to draw the complete drawing are as follows:

```python
for group in drawing:
    print("start group:")
    for p, k, s in group:  # get each primitive spec tuple and expand into components
        draw_element(p, k, s)
    print("end group\n")
```

That's it!

## Running the program

After you've completed entering the last statement above in interactive mode and pressed the final ```Enter```, the interpreter will run the entire program. You should see the following results:

```foo
start group:
setting position: x = 2 , y = -8
drawing circle: 3.6
setting position: x = 3 , y = 6
clamping 12 to range
drawing rect: 2 × 10
end group

start group:
clamping -16 to range
clamping -11 to range
setting position: x = -10 , y = -10
drawing rect: 4 × 3
setting position: x = 8 , y = -9
clamping 15 to range
drawing circle: 10
clamping 19 to range
setting position: x = 3 , y = 10
drawing rect: 5 × 6
end group
```

Congratulations! We've successfully written and run our first program.

## What's next
