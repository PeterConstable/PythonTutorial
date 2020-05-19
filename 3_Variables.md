# Intro to Variables

In the previous section, we introduced numeric an string values, but only showed them used as literals. That's fine if you want to use interactive mode as a basic calculator. But for anything more (or even a decent calculator), you'll want to use variables.

If you've used any other programming language, variables may seem straight forward: just assign a value to a variable expression, and then use that variable again later.

```foo
>>> x = "Hello!"
>>> print(x)
Hello!
```

That much is straightforward. But there's definitely more about variables you'll need to know. In this section, we'll go over some key points.

Along the way, we'll introduce some addtional built-in functions, ```id()``` and ```isinstance()```.

## Assignment and compound assignment operators

The example above introduced a familiar operator, the assignment operator ```=```. This is used to assign a value to a named variable.

Later on, we'll learn about comparison operators and their use in program control. We won't go into that now, other than to say that ```=``` is _not_ an equality comparison operator. As in many other languages, the Python equality operator is ```==```. But we're getting ahead of ourselves. Back to assignment.

Like several other languages, Python supports compound (or _in-place_) assigment operators that evaluate an expression and assign the result. For example:

```foo
>>> x = 6
>>> x += 5
>>> print(x)
11
```

In the second statement, the expression ```x + 5``` is evaluated, and the result is assigned back to ```x```. It's convenient shorthand for ```x = x + 5```.

Other numeric operators can be combined with ```=``` in the same way. Follow along this sequence of statements:

```foo
>>> x = 4
>>> x -= 1
>>> x
3
>>> x *= 2
>>> x
6
>>> x **= 2
>>> x
36
>>> x //= 4
>>> x
9
>>> x %= 5
>>> x
4
>>> x /= 2
>>> x
2.0
```

>Note: some languages support ```=+``` and ```=-``` as well as ```+=``` and ```-=```, with slightly different effects in loop conditions. In Python, ```=+``` and ```=-``` are meaningul, but they're not compound assignment operators! They're simply the assignment operator ```=``` with the following ```+``` and ```-``` interpreted as prefixes to the following number. For example,
>
>```foo
>>>> x =- 5
>```
>
>means exactly the same thing as
>
>```foo
>>>> x = -5

In string operations, ```+=``` can be used as a compound concatenation-assignment operator.

```foo
>>> x = "boo"
>>> x += "hoo"
>>> x
'boohoo'
```

OK, if you've worked with other programming languages, everything so far is probably familiar. Let's get into some less obvious stuff.

## Variables, types, and underlying objects

As mentioned in the previous section, everything in Python is an object and has a class type. That's true as well for variables. You don't declare the type of variables in advance; the type of a variable is determined dynamically when a value is assigned to it.

Let's start with a new interactive mode session and try to use a varible that hasn't yet been assigned—an error will occur:

```foo
> py
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

Now let's immediately assign a value to that variable name, get the interpreter to evaluate the variable, and then check its type using the ```type()``` function:

```foo
>>> x = 5
>>> x
5
>>> type(x)
<class 'int'>
```

After the assignment statement, the variable is defined and can be evaluated, and it has a type, ```int```.

Python is said to be _strongly typed_, and it is in the sense that every variable has one specific type. Because of that, the operations you can do with a variable are limited by its type. For example, just as a number literal can't be concatenated to a string, so also a number variable can't be concatenated.

```foo
>>> x = "The answer is "
>>> y = 42
>>> x + y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

However, Python does dynamic typing, and a new assignment can result in a variable name taking on a new type.

```foo
>>> x = 5
>>> type(x)
<class 'int'>
>>>
>>> x = "hi"
>>> type(x)
<class 'str'>
```

Now, there are some subtleties going on here, and it will be helpful to understand them.

In other languages, you might think of a variable such as ```x``` as a slot that takes a value, and a type declaration determines what type of values can go into that slot.

In Python, a variable ```x``` is a name that gets created and associated to an _object_ when an object (such as the number ```5```) is assigned to it. A new assignment statement can assign that name to _a different object_. When we use the ```type()``` function to get the type of a variable, we're actually asking for the type of the _object_ assigned to that variable name. It's the underlying objects that have a type, not the name.

The built-in ```id()``` function will help us understand what's going on. Every object in Python as a unique numeric ID (its _hash_). For example, the literal ```6``` evaluates to an object of type ```int``` with the value 6, and that object has an ID. When we pass that literal to the ```id()``` function, we get the ID of the object it resolves to:

```foo
>>> id(6)
140704550147904
```

If a numeric expression evaluates to the integer value 6, then asking for the ID of that expression will return the very same ID:

```foo
>>> id (4 + 2)
140704550147904
```

The ```id()``` function is telling us that the expression _result_ is the very same object as the result of evaluating the literal.

OK, let's apply this to variables: if we assign the integer ```6``` to a variable, then ask for the ID of that variable, we'll get the ID for the integer object assigned to the variable:

```foo
>>> x = 6
>>> id(x)
140704550147904
```

If we assign a different value to that variable, it gets associated with a different object that will have a different ID:

```foo
>>> id(42)
140704550149056
>>> x = 42
>>> id(x)
140704550149056
```

So, each of the objects has a fixed type and ID that never change. But the type and ID associated with the variable name depends on the object assigned to that variable name. And that can change dynamically.

```foo
>>> x = 42
>>> type(x)
<class 'int'>
>>> id(x)
140704550149056
>>>
>>> x = "hi"
>>> type(x)
<class 'str'>
>>> id(x)
2054141314608
```

If you're coming to Python from a language like C or Pascal in which _variables are strongly typed_, this is a aspect of Python that may take getting used to. 

When the type of an object assigned to a variable really matters, the built-in ```isinstance()``` function can be useful. It takes two arguments, an object and a type, and returns a boolean value ```True``` or ```False``` depending on whether the object is of that type. The object can be referred to using a literal expression, but more typically you'll pass a variable.

```foo
>>> isinstance("hi", str)
True
>>> x = "hi"
>>> isinstance(x, str)
True
>>> isinstance(x, int)
False
```

As with ```type()```, ```isinstance()``` is telling us about the object assigned to the variable name, not about the variable name itself.

## (Im)mutability

A key concept for variables is mutability: once a value is assigned to a variable, can it be changed or not? 

In Python, numeric and string _objects_ are immutable: they can't be changed. For numeric objects, this seems obvious: the object for the integer value 6 is simply a different object from that for the integer value 7.

But you might be thinking about mutability of _variables_. That's not really the right question to ask: as we've seen, variables are simply names with objects assigned to them, and a name can easily be reassigned with a different object. So, an underlying numeric object may be immutable, but the object assigned to a given variable can certainly change.

So, numeric objects can't change. For strings, things are a bit less obvious. Strings are sequences of characters. In the previous lesson, we had a brief peek at the sequence nature of strings, and saw that the individual character elements within a string literal can be referenced by index. The same is true for strings assigned to a variable:

```foo
>>> x = "cats and dogs"
>>> x[2]
't'
```

 So that raises a question for string variables: _Are the character elements within a string variable mutable or immutable?_

The answer for Python is that the elements of a string are immutable, including for strings assigned to a variable: character elements in a string cannot be changed. If you try, you'll get an error:

```foo
>>> x[2] = 'r'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

If you need to change any characters in a string, a new string object will be needed.

It was certainly a reasonable question to ask. Later, we'll learn about other sequence types in Python, and some of these are mutable in the sense of allowing elements in the sequence to be changed. But strings are not like that.

## Review

In this lesson, we learned about the assignment operator, ```=```, that is used to assign an object to a variable. We also learned about compound assignment operators that are a shorthand way to write a simple operation followed by an assignment using single operator:

* ```+=```: with numbers, addition / assignment; with strings, concatenation / assignment
* ```-=```: subtraction / assignment
* ```*=```: multiplication / assignment (for numbers, not strings)
* ```/=```: division / assignment
* ```//=```: integer division / assignment
* ```%=```: modulo (remainder) / assignment
* ```**```: exponentiation / assignment

We also learned that variables are names that get objects assigned to them. Every object has a specific type and a unique ID which can't change. But the object that a given variable name refers to can be changed, and so the variable can dynamically be associated with a different type.

We learned about the built-in ```id()``` function that provides a glimpse into the identify of the objects assigned to variables. We also learned about the ```isinstance()``` function that, like ```type()``` tells us about the type of the object assigned to a variable.

Finally, we learned that Python strings objects are immutable—in particular, that the character elements within a string cannot be changed.
