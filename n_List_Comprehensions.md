# List Comprehensions

[sof]:/sof

In [lesson 7](7_List_Tuple_Range.md#ranges), we saw that the ```range()``` function generates a sequence of numbers, and that we could use ```list(range(n))``` to create a ```list``` object with the sequence of numbers. In this lesson, we'll learn about _list comprehensions_ which are a more general and flexible way to generate lists.

* [Basic list comprehensions](#basic-list-comprehensions)
* [```for``` expression with multiple element variables](#for-expression-with-multiple-element-variables)
* [Using multiple ```for``` expressions](#using-multiple-for-expressions)
* [Nested comprehensions](#nested-comprehensions)
* [What's next](#whats-next)

## Basic list comprehensions

Consider the technique mentioned above to generate a list:

```foo
>>> list(range(4, 11))
[4, 5, 6, 7, 8, 9, 10]
```

This is fine if we want a sequence of consecutive numbers. We could also include a step value for a different interval:

```foo
>>> list(range(4, 20, 3))
[4, 7, 10, 13, 16, 19]
```

But using ```range()``` we can only generate arithmetic sequences with a fixed additive interval. What if we wanted a sequence that varied a different way, such as a geometric sequence, or sequence of cubes?

We could use a ```while``` or ```for``` loop with any kind of expression to compute values for elements in the sequence.

```foo
>>> my_list = []
>>> for x in range(6):
...     my_list.append(x * 7 + 2)
...
>>> my_list
[2, 9, 16, 23, 30, 37]
```

A list comprehension provides a more concise way to achieve this kind of result:

```foo
>>> my_list = [x * 7 + 2 for x in range(6)]
>>>
>>> my_list
[2, 9, 16, 23, 30, 37]
```

The basic components in this list comprehension are:

* brackets ```[...]```
* an expression for the list elements, ```x * 5 + 2```
* a ```for``` expression that produces the starter values for the expression, ```for x in range(6)```

These elements were all present in the earlier approach. As we work on more complex list comprehensions, it will be helpful to think of the components if we had used a for loop.

Now, suppose we wanted a list like above except that we need to exclude any multiples of 10. With a ```for``` loop, we would have added an ```if``` statement, as follows:

```foo
>>> my_list = []
>>> for x in range(6):
...     val = x * 7 + 2
...     if val % 10 != 0:
...         my_list.append(val)
...
>>> my_list
[2, 9, 16, 23, 37]
```

Similarly, we can add an ```if``` conditional expression in the list comprehension to filter the values that get included in the resulting list.

```foo
>>> my_list = [ x * 7 + 2 for x in range(6) if (x * 7 + 2) % 10 != 0 ]
>>>
>>> my_list
[2, 9, 16, 23, 37]
```

In these examples, we have used ```range()``` as the starting source for the sequence values. But we could use anything that can provide sequential values (technically, an _iterator_). For example, we could use a string:

```foo
>>> ['f' + c for c in "aeiou"]
['fa', 'fe', 'fi', 'fo', 'fu']
```

Or we could use another list or sequence-type object. The following example takes a tuple of objects of various kinds and extracts the ```str``` objects as a list.

```foo
>>> tup_a = (24, 'cat', [65, 33], "fog", "hue", 2.6, (3, -2))
>>>
>>> [x for x in tup_a if isinstance(x, str)]
['cat', 'fog', 'hue']
```

## ```for``` expression with multiple element variables

In [lesson 8](8_For.md#using-multiple-element-variables), we saw that we could have a ```for``` statement with multiple element variables when iterating over a sequence in which the members are multi-element sequence objects.

```foo
>>> a = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> for t1, t2 in a:
...     print("got item", t1)
...     print("it's a", t2, "\n")
...
got item 1
it's a cat

got item 2
it's a toad

got item 3
it's a mouse

```

A list comprehension can also have multiple element variables in the ```for``` expression when iterating over a sequence with multi-element sequence elements. But, they must be merged or reduced into a single object for the generated list. Let's consider a few examples.

```foo
>>> list_in = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> [ (t2, 'a', t1) for t1, t2 in list_in if len(t2) == 4]
[('toad', 'a', 2)]
```

In this example, ```t1``` and ```t2``` come from the members of each of the tuple pairs in ```list_in```. For the generated list, ```t1``` and ```t2``` are combined in a different way in three-element lists.

```foo
>>> list_in = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> [ t2 + str(t1) for t1, t2 in list_in]
['cat1', 'toad2', 'mouse3']
```

In this example, ```t1``` and ```t2``` are used in an expression to form simple-value elements.

## Using multiple ```for``` expressions

Consider the nested ```for``` loops in this example:

```foo
>>> my_list = []
>>> for x in range(3):
...     for y in range(4):
...         my_list.append((x, y))
...
>>> my_list
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
```

We can similarly use a list comprehension with multiple ```for``` expressions:

```foo
>>> my_list = [(x, y) for x in range(3) for y in range(4)]
>>> my_list
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]
```

Note that the ```for``` expressions in the comprehension work the same way as in the nested ```for``` loops: ```for x``` is mentioned first, and is used for the outer loop, with ```for y``` in the inner loop.

Also note that the comprehension generated a list of tuples, ```(x, y)```. In this situation, the parentheses to indicate the tuple are required.

Each ```for``` expression can have its own ```if``` filter condition:

```foo
>>> my_list = [(x, y)
...     for x in range(5) if x % 2 == 0
...     for y in range(6) if y % 2 != 0
...     ]
>>>
>>> my_list
[(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]
```

Here, we've written the comprehension across multiple lines for easier reading. Note that this executes just like this nested ```for``` loop with added ```if``` statements:

```foo
>>> my_list = []
>>> for x in range(5):
...     if x % 2 == 0:
...         for y in range(6):
...             if y %2 != 0:
...                 my_list.append((x, y))
```

Also notice that, with the nested ```for``` loops, if we had used ```y``` in the outer loop's ```if``` statement, we would have gotten an error:

```foo
>>> for x in range(3):
...     if (x + y) % 2 == 0:
...         for y in range(4):
...             my_list.append((x, y))
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: name 'y' is not defined
```

The same would apply in the equivalent list commprehension:

```foo
>>> my_list = [ (x, y)
...     for x in range(3) if (x + y) % 2 == 0
...     for y in range(4)
...     ]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in <listcomp>
UnboundLocalError: local variable 'y' referenced before assignment
```

However, in the inner-loop ```if``` expression, both ```x``` and ```y``` can be used since both are defined in that scope:

```foo
>>> my_list = [ (x, y)
...     for x in range(3)
...     for y in range(4) if (x + y) % 2 == 0
...     ]
>>> 
>>> my_list
[(0, 0), (0, 2), (0, 4), (1, 1), (1, 3), (1, 5), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3), (3, 5), (4, 0), (4, 2), (4, 4)]
```

## Nested comprehensions

## What's next
