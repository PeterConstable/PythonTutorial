# Some Basics

[sof]
There are a few basic things to know before we get started.

* [Interactive mode](#interactive-mode)
* [Comments](#comments)
* [A very brief intro to ```print()```](#a-very-brief-intro-to-print)
* [What's next](#whats-next)

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

### History

Interactive mode retains some history. You can use up or down arrow keys to find statements that were entered earlier, allowing you to repeat a statement without re-typing it. When you retrieve a statement from the history, you'll be able to make changes before entering; that will add the revised statement at the end of the history, but the earlier statement will still be in the history in its original form.

With multi-line statements, the entire statement might be treated as a complete unit the history, or as separate lines. It will depend on your console or IDE. If handled as a unit, then the entire statement will appear at once as you arrow-key through the history. To make changes, press left arrow to enter edit mode; then you'll be able to use up and down arrow keys to get to other lines without scrolling in the history.

### Errors

If you enter a statement that has a syntax error or that generates a runtime error, the interpreter will present an error statement.

```foo
>>> 6 = x
  File "<stdin>", line 1
SyntaxError: cannot assign to literal
```

It will show what the specific error is and provide a call stack to help see where in code the error occurred. This may generate several lines. In the following example, functions ```foo``` and ```bar``` are defined, with the implementation of ```bar``` making a call to ```foo```. Then ```bar(6)``` is entered, but inside ```foo``` that results in an error.

```foo
>>> def foo(val):
...     print(len(val))
...
>>> def bar(val):
...     foo(val)
...
>>> bar(6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in bar
  File "<stdin>", line 2, in foo
TypeError: object of type 'int' has no len()
```

The call traceback shows the execution flow, revealing that the error occurred at line 2 in ```foo```.

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

## A very brief intro to ```print()```

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

Naturally, there's lots more to learn about ```print()```, but this is enough to get us started.

## What's next

In the [next lesson](2_Numbers_Expressions_Variables.md#sof), we'll start learning about working with numbers.
