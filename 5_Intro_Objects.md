# Introduction to Objects

The aim of this section is introduce key concepts related to objects in Python, building on what we’ve learned in the previous lessons regarding numbers and strings. There will be other data types introduced in later lessons, including more on objects as a custom data type. But before exploring other data types, it will be helpful to be know some basics about objects. We’ll be making use of this in the very next lesson, on boolean values and comparisons. 

* [Object types](#object_types)
* [Object members](#object_members)
* [Sub-classes](#sub-classes)
* [A quick intro to `id()`](#a-quick-intro-to-id)
* [`None`](#none)
* [What’s next](#whats-next)

## Object types

In object-oriented programming, _objects_ are a mechanism that combines certain kinds of data with code that is applicable to that data. An object could hold one piece of data, such as a number; or it could combine multiple pieces of related data, such as the street, city, etc., that comprise a postal address. Every object has a _class_, which is like a template that specifies the pieces of data and the associated code. An individual object is said to be an _instance_ of that class.

Many programming languages make a distinction between simple data types, such as integers, versus classes and objects. But in Python, everything is an object. (_Really, everything!_) This includes all variables and literal values. All values have a type, but very type is, in fact, a class name. 

Python has a built-in function, `type()`, that tells you the type of whatever variable or value gets passed into it. Let’s review some of the types introduced in previous lessons, starting with integer literals:

```foo
>>> type(6)
<class 'int'>
```

Let's assign an integer value to a variable and then check the type of that variable:

```foo
>>> x = 6
>>> type(x)
<class 'int'>
```

The same goes for floating or complex values and strings.

```foo
>>> type(4.2)
<class 'float'>
>>>
>>> y = 3.14
>>> type(y)
<class 'float'>
```

```foo
>>> type("Hi!")
<class 'str'>
>>>
>>> s = "Eliza"
>>> type(s)
<class 'str'>
```

What about a single-character element from a string?

```foo
>>> type("Henry"[0])
<class 'str'>
```

We can also check the type of expressions. When an expressions is passed as an argument to a function, the expression gets evaluated before the function is called. So, the type of the expression will be the type of whatever the expression evaluates to.

```foo
>>> type(4 + 17)
<class 'int'>
>>>
>>> type(9 / 2)
<class 'float'>
```

## Object members

Objects can have many _members_, which are particular ways of interacting with an object to obtain certain information or perform certain operations. The members provided for an object are determined by its type. For example, the members of an `int` will be different from the members of a `string`. 

There are different kinds of members; two kinds that you will frequently use are _attributes_ and _methods_:

* Attributes provide access to information (data) contained in the object.
* Methods are operations (functions) that can be performed on an object or performed using the data in the object.

In the [previous lesson](4_More_Assignment_Numbers_Strings.md#converting-between-number-and-string-types), we were already introduced to attributes: with a `complex` value, the real and imaginary components can be obtained using the `.real` and `.imag` attributes:

```python
>>> c = (3+4j)
>>> type(c)
<class 'complex'>
>>>
>>> c.real
3.0
>>> c.imag
4.0
```

Strings have a number of methods for different string operations that can be performed. For example, the `.upper()` method produces a new string in which characters are mapped to their uppercase equivalent.

```python
>>> "ab".upper()
'AB'
```

Notice the different syntax used for attributes versus methods: methods always have parentheses after the method name, `(...)`, while attributes do not. The parentheses can be used to pass in additional values (or _arguments_) to the method; the arguments that can be accepted will depend on the particular method and object type. Every method has one implicit argument: the object itself.

In the `.upper()` method example, the value returned required some computational operation to be performed using the data contained in the object. Attributes, on the other hand, are obtained directly from the data items contained in the object.

## Sub-classes

Many programming languages allow a class to be derived from another class by adding additional capabilities or members, or by imposing certain limitations. This is the case in Python. For example, after we learn about defining custom classes, it would be possible to define a type `naturalnumber` that is based on the `int` type and that has all the same members but that limits values to non-negative integers.

Object sub-classes are a more advanced topic, and we won’t go into more detail just yet. But we will see an instance of a sub-class in the next lesson when we are introduced to the Boolean type, `bool`.

## A quick intro to `id()`

Every object has an ID—a _hash_ value that (when combined with its type) uniquely identifies it. You probably won't often need to work directly with object IDs (though it can sometimes be helpful in debugging). But it’s important to understand that the identity of an object and the value of an object are distinct concepts.

You can get the ID of an object using the build-in `id()` function.

Let's start by looking at an integer literal, such as "6": this evaluates to an object of type `int` with the value 6, and that object has its own ID:

```foo
>>> id(6)
140704550147904
```

> Note: the specific ID returned on one system will not necessarily be the same for another. The actual ID value has no significance beyond providing a unique ID for a particular object in the current Python session.

The `int` value 6 is a specific object. If we ask for the ID of an expression that evaluates to the same `int` value, then we’ll get the very same ID:

```foo
>>> id (4 + 2)
140704550147904
```

If we assign that `int` value to a variable, then the variable simply becomes a reference to that object, so asking for the ID of that variable will also return the same ID:

```foo
>>> x = 6
>>> id(x)
140704550147904
```

If we introduce other variables that get the same `int` value assigned to them, either directly or indirectly, they'll have the same ID, because each variable is just a reference to the same object.

```foo
>>> y = 6
>>> id(y)
140704550147904
>>>
>>> z = x
>>> id(z)
140704550147904
```

`int` objects are somewhat special in this regard: any occurrence or reference to an `int` of a particular value will always involve a single object. With other types, that’s often not the case: two things of the same type with the same value _might or might not_ have the same ID. Consider these examples:

```foo
>>> id(6.0)
2497399318800
>>> x = 6.
>>> id(x)
2497399318800
```

In this case, when the literal value was assigned to `x`, the variable ended up with the same ID as the literal. However, in the same session, when the same value was derived from an expression, the ID was different:

```foo
>>> id(2 + 4.)
2497399319408
```

```float```s with the same value will often have different IDs.

Strings are similar in this regard:

```foo
>>> id("hi")
2497399613936
>>> x = "hi"
>>> id(x)
2497399613936
>>>
>>> y = "phish"[1:3]
>>> id(y)
2497399614192
```

When we assign a string literal value to the variable `x`, the ID of the variable is the same as the ID of the literal. But if we derive the same string value as a slice from another string, that ends up with a different ID. Note that we started with a distinct string literal, `"phish"`, then took a slice from that value which was copied into a new string object. The variable `y` happens to end up with the same value as the variable `x`, but the objects have distinct IDs.

We've seen that objects with the same values don’t always have the same object ID. This is a bit abstract! In the next lesson, things will get even a bit _more_ abstract when we consider whether things that return the same ID are, in fact, the very same object. (Not necessarily!)

## `None`

Python has a special object that is used to mean, well, nothing at all. Really! It’s a built in constant represented by the symbol, `None`. This constant must be written exactly that way, with an initial capital followed by lowercase letters.

Strictly speaking, it's not really _nothing_ since it's a real object with its own special type.

```foo
>>> type(None)
<class 'NoneType'>
```

But it's used to represent the _idea of nothing_. When would it be used? Well, here are two situations:

* When an object is constructed, it could have an attribute that must take an object, but no “real” object has been specified yet. That attribute can get initialized to `None`.
* A function might be designed to return certain kinds of values, but under some condition it's not possible to determine a value of that kind. In that situation, the function might return ```None```.

Remember the Billy Preston song, “Nothin’ from nothin’ leaves nothin’”? Well, that doesn’t work for `None`: you can’t use `None` in arithmetic operations. The point is, `None` is not the same as `0`. It's also not the same as the empty string, "", or anything else, for that matter.

We’ll start seeing how `None` can be put to use in the next lesson.

## What’s next

In the [next lesson](6_Bool_Comparisons.md), we'll learn about Boolean values and comparison and logical expressions.
