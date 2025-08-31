# Intro to Functions and Flow Control Statements

Functions and flow control statements are key tools in Python that you'll use a lot. This lesson provide an initial introduction to get you started using them. There are many details we'll save for later.

Python has three familiar flow control statements found in many languages: ```if```, ```while``` and ```for```. The ```if``` and ```while``` statements are similar to the corresponding statements in other languages. But the ```for``` statement in Python is somewhat different; we'll come back to it in [lesson 8](8_For.md).

Since we'll be covering the ```if``` flow control statement, this will also be a good time to introduce the ternary ```if```...```else``` operator construct, which is like a compact ```if``` block that's uses a single statement to return a value based on some condition.

Python doesn't have ```switch``` statement as in C and many other languages; the same functionality can be implemented using ```if```. In later lessons, we'll see other techniques that can also be used.

Up to now we've assumed you're trying things out in interactive mode. The mechanisms we'll be working with require writing several statements in order on multiple lines. That's possible in interactive mode, but not always easy. So, we'll keep examples in this lesson simple. After we've introduced modules in a later lesson, it will be easier to start working on longer statement sequences.

* [Overview](#overview)
* [Indentation](#indentation)
* [Functions](#functions)
* [The ```pass``` statement](#the-pass-statement)
* [The ```if``` statement](#the-if-statement)
* [The ternary ```if```... ```else``` operator](#the-ternary-if-else-operator)
* [The ```while``` statement](#the-while-statement)
* [What's next](#whats-next)

## Overview

In the previous lesson, there were a couple of examples that gave a preview of function definition and control statements. Here's a similar example with a complete function definition.

```python
def my_func(string1, string2):
    if len(string1) > len(string2):
        return string1
    else:
        return string2
```

The function takes in two strings, compares their length, and then branches the program flow based on that condition: if ```string1``` is longer, it returns ```string1```. Otherwise, it returns ```string2```. There are several key elements here.

First, at a higher level, there are elements that make up the function:

* A function definition statement that gives the function a name
* Parameters taken as input into the function and that impact what it does
* A block of statements that comprise what the function does
* Results that it returns to the caller

>Note: Within Python documentation, an execution block is referred to as a _suite_.

Within the function's implementation block, we find flow control statements that affect what operations will happen. The key elements are:

* Statements with flow control keywords (in this case, ```if``` and ```else```) that determine the nature of the control over execution
* A condition that gets evaluated to determine how the program flow proceeds
* Statement blocks for each of the different options in the flow

We'll go into more detail on these elements. But first, there are some syntactic things to point out.

## Indentation

Python uses indentiation as a means of determining groupings of statements into an organizational hierarchy. The same syntactic device is used for function definition and for flow control statements.

Some other languages use braces ```{...}``` or similar means to indicate grouping of statement. Python doesn't use braces; it only uses indentation. Each increase in indentation starts a new level of embedding, like a ```{```, and each decrease in indentation indicates the end of the grouping at that level, like a ```}```.

If you don't do proper indentation, you'll either have syntactic errors or end up with Python interpreting things in a way you didn't intend.

You can indent using either tabs or spaces, it doesn't strictly matter, though spaces are recommended (see [PEP8](https://peps.python.org/pep-0008/#tabs-or-spaces)). The amount of indendation to indicate a grouping level also doesn't strictly matter: you could use two spaces, four spaces... however many you want (four spaces is recommended—see [PEP8](https://peps.python.org/pep-0008/#indentation)). What _does_ matter, though, is that you need to use the same number of spaces or tabs consistently to indicate a given level of grouping.

Another thing to note from the example above is the terminating ```:``` on statements that precede a new grouping level.

```python
def my_funct(...):
```

```python
    if ... :
```

```python
    else:
```

The ```:``` is essential.

If you're coming to Python after working in another language like C or Javascript, these devices for grouping may seem strange, but you'll quickly get used to them.

## Functions

You start a function with a definition statement that defines the function name and the parameters it takes.

```python
def pick_the_longer_string(string1, string2):
```

A function doesn't have to have parameters, but the parentheses to indicate parameter are always required.

```python
def bake_cake():
```

Later when we learn about defining classes, we'll see cases in which the functions you define have certain required parameters. But apart from that, you have full control over what parameters your function takes based on what you need it to do.

### Optional parameters

Some languages allow you to define the same function name with different sets of parameters—overloading. You can't do exactly that in Python, but you can get the same functionality by having optional parameters. You specify a parameter as optional by specifying a default value for it in the parameter specification. For example:

```python
def pick_pet(kind, color="black"):
    print(color + " " + kind)
```

In this example, the caller has to pick a kind of pet, but the color choice is optional: if the caller doesn't pass a color argument, "black" will be used by default. So, the calling code might specify a colour argument:

```python
    my_pet = pick_pet("canary", "yellow")
```

In that case, the ```print()``` output would be "yellow canary". Or, the calling code could leave out a colour argument, like so:

```python
    my_pet = pick_pet("dog")
```

This time, the ```print()``` output would be "black dog".

There are lots of details regarding parameter specifications and ways to specify arguments when calling that we'll save for later. For now, a key point to know is that any optional parameters must come after required parameters.

### Returning a value

Depending on what your function does, it can return a value, or not. (Presumably if it doesn't return a value, it has still done something useful that's evident somewhere else.) To return a value, you use a ```return``` statement.

```python
def get_The_Answer():
    return 42
```

If your function doesn't need to return a value, you can still end the execution flow with a ```return``` statement, just without any value specified.

```python
def print_temp(temp):
    print("The current temperature:", temp)
    return
```

Whether you include the ```return``` statement like this or omit it, your function will do the same thing: it will return ```None```.

When the function is called, the calling code can either capture the returned value and do something with it, or it can simply ignore any returned value.

For example, this ambivalent code asks for The Answer but then doesn't pay attention to what The Answer is:

```python
    #Is there an answer? (We can ask, but we won't believe it anyway.)
    get_The_Answer()
```

The value returned by the function just goes into the "bit bucket".

In some other languages, when you declare a function, you specify whether and what of value it returns. And if you declare a return value, then you must ensure it always returns a value of that type, regardless of what branching of code flow is followed. Python is more lenient in this regard: you can have some paths end returning a value, but other paths that don't. For example:

```python
def pick_winning_number(day_of_week):
    if day_of_week != "Friday":
        print("We only pick a winner on Fridays.")
    else:
        return 42
```

So, suppose the calling code is as follows:

```python
    # intialize day
    day = "Monday"
    # do other stuff that might change the day
    winner = pick_winning_number(day)
    # do other stuff
```

What happens if the ```day``` argument still has the value "Monday" when the function is called? Within the function the code path taken will print something to the console but doesn't have a ```return``` statement. The end result in the calling code is that the ```winner``` variable will be assigned the value ```None```.

Functions will always return a value; in some cases, it might be ```None```. If you know that's a possibility, then you can check for that, as we learned in the previous lesson:

```python
    # intialize day
    day = "Monday"
    # do other stuff that might change the day
    winner = pick_winning_number(day)
    # might be None!!
    if is not None:
        # we can notify the winner
    else:
        # must be the wrong day...
```

## The ```pass``` statement

Python has a special statement keyword, ```pass```, that is simply a no-op (do nothing at this step). You can include a ```pass``` statement anywhere. Why would you want to do that? There are different situations in which it's useful.

Suppose you've decided you're going to define a function but aren't ready to create it's implementation. If you write a definition statement to start a function but don't have any indented statement block after it, that's considered a syntax error. If you're not ready to write the function implementation, you could comment out the definition statement, but maybe you needed it to be defined—for instance, if you're working on the code that will call it. You can temporarily add a ```pass``` statement as the execution block to get around the syntax error:

```python
def calculate_planck_constant():
    pass  # TO DO: find out how to do this
```

## The ```if``` statement

The ```if``` statement is used to create different branches of code execution flow for different conditions. It's structured as follows:

```python
    if <condition>:
        <execution block>
    elif <condition>:
        <execution block>
    else:
        <execution block>
```

The initial ```if``` statement, its condition, and a following execution block are required.

An ```elif``` statement is optional; there can also be multiple ```elif``` statements and corresponding execution blocks if multiple conditions need to be considered.

The ```else``` statement and corresponding execution block is also optional. There can only be one ```else``` statement for a given ```if```, and it must follow any ```elif```s.

We've already seen examples of it in use earlier in this lesson, though not with the different ```elif```/```else``` possibilities. Here are some other examples.

```python
def pick_winner(day_of_week)
    if day_of_week == "Friday":
        return 42
    elif day_of_week == "Tuesday":
        return 54
    elif day_of_week == "Sunday":
        return 7
    else:
        print("no winners today")
```

```python
def max_length(string1, string2):
    if len(string1) > len(string2):
        return len(string1)
    elif len(string1) < len(string 2):
        return len(string2)
    # no else: only to be called for strings wtih differentlength (else returns None)
```

In some situations, one of the possible conditions might not require any action. You could just ignore the condition, but you might want to list it explicitly to make the intent clear for later reference. But every ```if```, ```elif``` or ```else``` requires a following execution block; otherwise, you'll get a syntax error. This is one of those situations in which a ```pass``` statement can be useful.

```python
    if temp > 38.5:
        treatment_1()
    elif temp < 36.0:
        treatment_2()
    else:
        # continue monitoring without treatment
        pass
```

### Objects as ```if``` conditions

In [lesson 5](5_Bool_Comparisons.md#booleans—the-bool-type), we learned that objects can be converted to boolean values, ```True``` or ```False```. This can be done explicitly using the ```bool()``` function, but also can happen implicitly if an object is used in a context when a boolean value is expected. In particular, an object on its own can be used as a conditional expression in an ```if``` or ```elif``` statement.

This is illustrated in the following example:

```python
>>> def my_func(val):
...     if val:
...         print("true")
...     else:
...         print("false")
...
>>> my_func(42)
true
>>> my_func("")
false
>>> my_func(None)
false
```

The parameter variable ```val``` is used on its own as a condition. Arguments that are passed in will be coverted implicitly to ```True``` or ```False```. As we learned in lesson 6, very few objects convert to ```False```; empty strings and ```None``` happen to be two that do.

We can also have conditions involving logical expressions with objects as operands:

```python
>>> def my_func(val1, val2):
...     if val1 and val2:
...         print("true")
...     else:
...         print("false")
...
>>> my_func(42, 0)
false
>>> my_func(42, 10)
true
>>> my_func(42, "figs")
true
```

## The ternary ```if```... ```else``` operator

We'll temporarily digress from flow-control statements to cover the ternary ```if```... ```else``` operator. This is similar to the ```if``` flow control statement in that a condition is evaluated to choose different options. In this case, though, a single statement is used to return a value based on the condition.

You may have learned about a similar ternary operator in another language. For example:

```cs
    x > 0 ? 1 : -1
```

This evaluates a condition, ```x > 0```, and returns 1 if the condition is true, or -1 if the condition is false. In Python, this would be written as follows:

```python
    1 if x > 0 else -1
```

Note that the order of the pieces are different.

```python
    <result_if_true> if <condition> else <result_if_false>
```

If you're coming from a different language, the different order may take a little getting used to.

Here's an example of a function that uses the ternary operator construct to clamp a value to within a certain range:

```foo
>>> def clamp(val):
...     max = 10
...     # clamp to range -max to +max
...
...     if abs(val) > max:
...         return max if val > 0 else -max
...     else:
...         return val
...
>>> clamp(8)
8
>>> clamp(-16)
-10
```

## The ```while``` statement

While statements are supported in many languages for creating loops—repeating some sequence of steps while some condition remains true. The ```while``` statement in Python is similar to other languages, but with an optional ```else```. It's structured as follows:

```python
    while <condition>:
        <execution block>
    else:
        <execution block>
```

The condition is tested before the following block is executed, and then again. The ```while``` block will be repeatedly executed until the condition is no long true. So, something needs to happen within the block that will eventually make the condition false.

```python
    i = 0
    while i < 4:
        print(i)
```

It's fairly obvious what the intent was in that example: to print a sequence of integers up to 3. But nothing changes the value of ```i``` within the loop, and so it's an infinite loop. It should be something like this:

```python
    i = 0
    while i < 4:
        i += 1
        print(i)
```

>Note: In interactive mode, if you accidentally execute an infinite loop, you can press ```Ctrl-C``` to interrupt it.

The ```else``` block, if present, executes whenever the condition doesn't hold. That may occur the first time the condition is tested, or later after 1 or more passes through the loop. In this example, the loop executes a few times, then the ```else``` block executes:

```foo
>>> i = 0
>>> while (i < 4):
...     i += 1
...     print(i)
... else:
...     print(6)
...
1
2
3
6
```

But in this example, the loop block never executes:

```foo
>>> i = 10
>>> while (i < 5):
...     i += 1
...     print(i)
... else:
...     print(6)
...
6
```

You might notice that the previous example didn't really require use of an ```else``` statement: the following ```print()``` statement could have been raised out of the ```while``` construct as the next top-level statement:

```foo
>>> i = 10
>>> while (i < 5):
...     i += 1
...     print(i)
... print(6)
...
6
```

There's a signficant difference if a ```break``` statement is used within the loop, however. We'll cover that next.

### ```break```

In some situations, you may reach a state within a loop that qualifies as a different condition for ending the loop. You can use a ```break``` statement to exit the loop. If ```break``` is reached, nothing after it in the loop is executed, and the ```while``` condition is not tested again. If there is an ```else``` block, that is also skipped.

In this example, using ```True``` as a condition seems to be setting up for an infinite loop. But there's a ```break``` within the loop that will be reached after a few iterations.

```foo
>>> i = 0
>>> while True:
...     if i == 3:
...         break
...     else:
...         i += 1
...         print(i)
... else:
...     print(6)
...
1
2
3
```

Note that the ```else``` block was not executed.

### ```continue```

Within a loop, you may have situations, with secondary conditions, in which you want to skip the remainder of steps for that loop. The ```continue``` statement allows for that. If ```continue``` is reached, all the statements after it in the loop block are skipped, and the flow returns to the top of the loop with the condition tested again.

In this example, the ```if``` statemnt is checking whether ```i``` is even or odd. If even, ```continue``` is reached and the next loop begins. Hence, only odd numbers get printed.

```foo
>>> i = 0
>>> while i < 10:
...     i +=1
...     if i % 2 == 0:
...         continue
...     else:
...         print(i)
... else:
...     print("done")
...
1
3
5
7
9
done
```

Note that the ```else``` block gets executed: ```continue``` never causes that to be skipped.

## What's next

There's one more flow control statement we need to look at, the ```for``` statement. It's always used with sequences or objects with a certain sequence-like quality. So, in the [next lesson](7_List_Tuple_Range.md), we'll learn more about sequence types, then we'll cover ```for``` in the lesson after that.
