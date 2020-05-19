# Some Basics

There are a few basic things to know before we get started.

## Interactive mode

Python is an interpreted language, which means that you don't need to compile to run your code. A common way to use Python is in _interactive mode_, which allows you to interact with the Python interpreter in a console session.

>In this section and in much of the tutorial, examples will assume we're working in an interactive mode console session.

The way you start interactive mode depends on the version of Python you have installed, or whether you're working in a console window or an IDE. A typical way to start it in a console window is to run ```py```:

```foo
> py
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

The '>>>' prompt indicates you're in interactive mode. To exit back out, enter ```quit()``` or ```Ctrl-Z```.

```foo
> py
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
>
```

When you type a statement in interactive mode and press ```enter```, it is immediately interpreted and the result (if any) is displayed:

```foo
>>> "Hello, world!"
'Hello, world!'
```

Note that the line with the result does not have the ">>>" prompt.

Interactive mode retains some history. You can use up or down arrow keys to find statements that were entered earlier.

If you start entering a statement and want to clear that without entering, use the ```Esc``` key.

### The "\_" variable

In interactive mode, the result of the last statement is stored in a special variable, ```_```. You can use that in the next statement.

```foo
>>> 6 + 2
8
>>> _ + 1
9
```

Note that the ```_``` variable is available in interactive mode, not in modules (.py script files).

### Multi-line statements

Many statements can be (and sometimes need to be) entered on multiple lines. The "..." prompt indicates that a statement is partially complete and that the interpreter is waiting for the rest:

```foo
>>> print(
...
```

If you try pressing ```enter` while in this state, it will start a new line but remain in this state:

```foo
>>> print(
...
...
```

If you want to get out of this state, you can press ```Ctrl-C``` to enter a keyboard interrupt:

```foo
>>> print(
...
KeyboardInterrupt
>>>
```

Of course, you can also complete the statement and enter it.

```foo
>>> print(
... 6)
6
>>>
```

## Comments

Single-line comments are entered using "#".

```foo
>>> 6 # A number
6
```

The comment runs to the end of the line. Python doesn't support inline comments, as in some other languages. For example:

```foo
>>> 6 /* a number */ + 2
  File "<stdin>", line 1
    6 /* a number */ + 2
       ^
SyntaxError: invalid syntax
```

Multi-line comments aren't really relevant for interactive mode, though you'll want to use them sometimes when writing Python modules. Multi-line strings that aren't otherwise used in Python statements can be added as comments.

```python
# my_module.py

""" This is a multiline comment that talks about an English et cetera,
    et cetera with brass candle-holders—I said etcetera etcetera
    because it saved me saying the full sentence which was a certain
    English rosewood upright piano with brass candle-holders. That's
    why I said etcetera etcetera, etcetera etcetera. Thought you might
    like to know. But what does this have to do with the module? Well,
    the module counts et ceteras that are found in 1950s radio comedy
    shows.
"""

    count = 0
    # et cetera
```

## A very quick intro to ```print()```

The built-in ```print()``` function (surprise!) prints things to console output. (You can also send output elsewhere, but that's for later.) For example:

```foo
>>>print(42)
42
```

You can provide multiple arguments, and ```print``` will add spaces between them:

```foo
>>> print(6, 9, 42)
6 9 42
```

Naturally, there's lots more to learn about ```print()```, but that's a later topic. This is enough to get us started.
