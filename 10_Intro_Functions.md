# Intro to Functions

In lessons 7 and 9, we were introduced to flow control using `if`, `while` and `for` statements. Functions are another important tool for organizing code and managing program flow that you'll use a lot. In this lesson, we'll learn several basics of working with functions.

* [Overview](#overview)
* [Structure of a function definition](#structure-of-a-function-definition)
* [Invoking a function](#invoking-a-function)
* [Optional parameters](#optional-parameters)
* [Returning a value](#returning-a-value)
* [Using the `pass` statement](#using-the-pass-statement)
* [What's next](#whats-next)

## Overview

In a nutshell, functions provide a specific bit of functionality. They can be used to divide a larger operation into smaller steps, making the larger flow easier to understand while also making it easier to focus on details in the smaller steps. They can also be used to provide re-usable functionality that can easily be invoked from several contexts. Later, when we learn to define classes, functions will be used to create methods with functionality specific to a class.

In some earlier lessons, there were some examples that gave a preview of a function definition:

```python
def my_func(val):
    if isinstance(val, str):
        # do appropriate stuff
```

In this example, `my_func` is a function that takes an argument, `val`, tests whether `val` is a string. Let's drill into defining and using functions in more detail.

## Structure of a function definition

You start a function with a definition statement that defines the function name and any parameters it takes.

```python
def longest(string1, string2):
```

At a minimum, a function is comprised of a `def` and an execution block. 

It's also recommended to include a _docstring_ that describe what the function does.

```python
def <function name>(<argument_list_>):
    """Basic structure of a function definition."""
    <execution block>
```

As described for other flow control statements (`if`, etc.), [indentation](7_Intro_Flow_Control.md#indentation) is used to demarcate the execution block of a function. Four spaces are recommended.

In this example, `my_func` is the function name, `val` is a parameter, and the execution block has a single `print` statement:

```python
def my_func(val):
    print(val)
```

> Terminology note: A distinction is sometimes made between _parameters_ and _arguments_. In a function definition, the variables for values that can be received when the function will be called are _parameters_. When a function is invoked, the values that are passed in are _arguments_.

In the `def` statement, a parameter list is optional. A function that performs an action without requiring any values to be passed to it can have an empty parameter list. The parentheses to indicate the parameter list are still required, however

```python
def greeting():
    print("Hello!")
```

Later when we learn about defining classes, we'll see cases in which the functions you define must have certain required parameters. But apart from that, you have full control over what parameters your function takes based on what you need it to do.

## Invoking a function

A function is invoked in other code (the _calling_ code) using the function name followed by any required arguments listed inside parentheses, `(...)`. The parentheses are required, even if the function is defined with no parameters.

```foo
>>> greeting()
Hello!
```

If parameters are required, but the function is called without all the required parameters, then an error will occur:

```python
def greeting(name):
    print("Hello, {}!".format(name))
```
```foo
>>> greeting("Sam")
Hello, Sam!
>>>
>>> greeting()
Traceback (most recent call last):
  File "<python-input-19>", line 1, in <module>
    greeting()
    ~~~~~~~~^^
TypeError: greeting() missing 1 required positional argument: 'name'
```

## Optional parameters

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

Suppose you don't want any default colour? You could make the default value an empty string, `""`, or `None`, and then test for that to adjust the operations as needed.

```python
def pick_pet(kind, color=""):
    if color=="":
        print(kind)
    else:
        print("{} {}".format(color, kind))
```
```foo
>>> pick_pet("pony", "brown")
brown pony
>>> pick_pet("pony")
pony
```

> Note! Any optional parameters must come after all required parameters.

There are lots of details regarding parameter specifications and ways to specify arguments when calling that we'll save for later.


## Returning a value

Depending on what your function does, it can return a value, or not. To return a value, you use a `return` statement.

```python
def get_The_Answer():
    return 42
```

If your function doesn't need to return a value, you can still end the execution flow with a return statement, just without any value specified.

```python
def print_temp(temp):
    print("The current temperature:", temp)
    return
```

When the function is called, the calling code can either capture the returned value and do something with it, or it can simply ignore any returned value.

For example, this ambivalent code asks for The Answer but then doesn't pay attention to what The Answer is:

```python
    #Is there an answer to The Question? (We can ask, but we'll just ignore it.)
    get_The_Answer()
```
The value returned by the function just goes into the "bit bucket".

That example seems silly. But sometimes a function can perform an action, as well as returning a value. In some situations, invoking the action might be all you need.

A function can also perform an action without returning any particular value:

```python
def my_func(val):
    if isinstance(val, str):
        print("val is a string")
    return
```

In this example, the `return` statement was explicit. But if no value needs to be returned, then it could be left out, leaving the return point implicitly after the last execution statement.

```python
def my_func(val):
    if isinstance(val, str):
        print("val is a string")
```

A `return` statement doesn't have to be at the end of the executiion block. It can also be used earlier if there are branches in the execution flow that reach an ending point:

```python
def my_func(val):
    if not isinstance(val, str):
        print("val is NOT a string")
        return
    # Val is a string: lots to do...
    # ...
    # Calculations are done:
    print(results)
    return
```

In this example, the lines following the `if` block could have been handled as the execution block for an `else:` clause in an `if... else` statement. If that were done, the first `return` statement in the `if` block wouldn't have been needed. But it also would have added an embedding level to all of the following code, which could have made everything harder to read. For instance, it would have been less clear that, if that first condition is `true`, then no further processing is done on `val`. Inserting an early `return` statement often makes things clearer.

In the above examples, no _specific_ value is returned to the caller. The `return` statement can take an operand, which is the value to return to the caller:

```python
def get_longest(string1, string2):
    if len(string1) > len(string2):
        return string1
    else:
        return string2
```

Functions always return a value! If there is no explicit `return` statement or `return` statements do not pass a specific value, the function will return `None`. In the following example, `get_longest` expects two string arguments, but non-string values could be passed in. If both arguments are strings, it will return the longer string. But if either argument is not a string, it will return `None`.

```python
def get_longest(string1, string2):
    if not isinstance(string1, str) or not isinstance(string2, str):
        print("Non-string arguments passed in!")
        return
    if len(string1) > len(string2):
        return string1
    else:
        return string2
```

[Lesson 6](6_Bool_Comparisons.md#comparison-with-none) introduced the comparisons `is None` and `is not None`. One use for this will be to test whether a function returned a particular value or not. For example:

```python
    # preceding operations yielded variables v1 and v2 from somewhere
    longest = get_longest(v1, v2)
    # make sure we got a string result
    if longest is None:
        print("Hmmm... v1 and v2 aren't both strings!")
    else:
        print("v1" if longest == v1 else "v2")
```

## Using the `pass` statement

In [lesson 7][7_Intro_Functions_Flow_Control.md#the-pass-statement], we were introduced to the `pass` statement, which is a no-op. This can be used in a function execution block if you've decided to create a function but aren't ready to create its implementation. If you write a `def` statement but don't have an indented statement block after it, that's considered a syntax error. You could comments out the `def` statement to avoid an error, but then you can't write other code to call that function. You can temporarily add a `pass` statement as the execution block to get around the syntax error:

```python
def calculate_planck_constant():
    pass # TO DO: find out how to do this!
```

## What's next
There's more to learn about functions and flow control, but we can do a lot with what we have learned so far. In the [next lesson](11_Sample_Program.md), we'll put things into practice with a sample program.