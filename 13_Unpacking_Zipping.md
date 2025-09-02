# Unpacking and Zipping Sequences

Sometimes you might have a sequence object, such as a list, but need to use it in a context in which the individual elements are needed, not the sequence object. _Unpacking_ provides a convenient way to get the sequence of elements from the sequence object.

There can also be situations in which you'd like a convenient way to group sequential things together to use in a context where that grouping is expected. For example, you might have two separate lists, `['a','b']` and `[1,2]`, but it would be convenient to have them combined into a list of pairs, `[('a',1), ('b',2)]`. The built-in `Zip()` function makes that easy.

Unpacking and zipping have been mentioned in relation to sequences but, more generally, they can be used with any iterable types.

## Unpacking function arguments

In some situations, you'll want to call a function that requires multiple arguments, but you have those combined into an object such as a tuple. 

For example, suppose you have a list and need to perform different operations on different sub-ranges of that list. You might have a list of tuples with start and end indices for these sub-ranges:

```
runs = [(0, 3), (2, 5), (1, 4)]
```

For each of these tuples, you might want to create a `range` to provide indices for the elements in the list to be modified. However, you can't pass a tuple into the `range()` constructor:

```foo
>>> range((0,3))
Traceback (most recent call last):
  File "<python-input-43>", line 1, in <module>
    range((0,3))
    ~~~~~^^^^^^^
TypeError: 'tuple' object cannot be interpreted as an integer
```

You could work around this by explicitly referencing the separate elements in the tuple:

```foo
>>> run = (0,3)
>>> range(run[0], run[1])
range(0, 3)
```

But a simpler way would be to unpack the tuple. This is done using the `*` operator:

```foo
>>> range(*run)
range(0, 3)
```

> Note: `*` is also used as an arithmetic operator. The arithmetic operators works only with two numeric operands. The unpacking operator works only on a single, iterable operable, and numbers are not iterable. Thus, the two usage contexts for the `*` symbol are distinct.

The effect of unpacking can be clearly illustrated using the `print()` function. We've seen that the `print()` function can take multiple arguments, in which case it prints them in order with a space in between.

```foo
>>> print('a', 1)
a 1
```

If we pass a list, `print()` will display it as a list with elements surrounded by square brackets, "[...]". However, if we unpack the list argument using the `*` operator, it will be as though all of the list elements were passed (in order) as separate arguments:

```foo
>>> print([43, 19])
[43, 19]
>>>
>>> print(*[43, 19])
43 19
```

We've seen that a `range` object is an iterable that can generate a sequence of values. If we pass a `range` object as an argument, `print()` will reflect how the `range` is defined rather than the sequence of values. But we can use `*` to unpack the range, which will cause the sequences of generated values to be passed as separate arguments:

```foo
>>> print(range(3))
range(0, 3)
>>>
>>> print(*range(3))
0 1 2
```

Unpacking works the same way on string arguments as on lists: the character elements within the string are pass as separate arguments:

```foo
>>> print("Eliza Doolitle")
Eliza Doolitle
>>>
>>> print(*"Eliza Doolitle")
E l i z a   D o o l i t l e
```

Unpacking can be applied at multiple levels of nesting. If you have a sequence object that itself contains other sequence elements, you can unpack the nested sequence elements as well as the parent sequence.

```foo
>>> print(*['ab', (1,2), [3,4]])
ab (1, 2) [3, 4]
>>> print(*[*'ab', *(1,2), *[3,4]])
a b 1 2 3 4
```

## Implicit sequence unpacking

In [lesson 8](8_List_Tuple_Range.md#tuples), we saw that a tuple, list or string can be used in a multiple assignment statement, assigning values to multiple variables:

```foo
>>> x, y = (12, 62)
>>> x
12
>>> y
62
>>>
>>> x, y = ['a', 3]
>>> x
'a'
>>> y
3
>>>
>>> x, y, z = "cat"
>>> x
'c'
>>> y
'a'
>>> z
't'
```

Also, in [lesson 10](10_Intro_Functions.md#returning-multiple-values), we saw that a function can return multiple values with a single `return` statement:

```python
def return_pair():
    return 17, 24
```
```foo
>>> x, y = return_pair()
>>> x
17
>>> y
24
```

We also saw something similar in [lesson 9](9_For.md#using-multiple-element-variables), with multiple variables referenced in a `for` loop:

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

In all of these situations, Python is doing implicit tuple unpacking.

When multiple values are listed in a function `return` statement, they are implicitly combined into a tuple, and a single tuple is returned. This can be checked by testing the type of the return value, or by simply printing the return value:

```foo
>>> type(return_pair())
<class 'tuple'>
>>>
>>> print(return_pair())
(17, 24)
```

You can also assign the returned value to a single variable:

```foo
>>> print(return_pair())
(17, 24)
>>> pair = return_pair()
>>> type(pair)
<class 'tuple'>
>>> pair[0]
17
>>> pair[1]
24
```

When you use the function call directly in a multiple assignment statement, such as this,

```foo
>>> x, y = return_pair()
```

the runtime is implicitly unpacking the tuple into a sequence of the separate values. It's equivalent to doing the following, but without the extra steps and variable:

```foo
>>> pair = return_pair()
>>> x = pair[0]
>>> y = pair[1]
```

In the case of the `for` statement from lesson 9, the `for` loop was operating over a list of tuples. We saw that we could get each tuple and reference its elements individually:

```foo
>>> a = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> for x in a:
...     print("item", x[0], 'is a', x[1])
```

Or we could get each tuple element do multiple assignment to two variables (which would also implicitly unpack the tuple):

```foo
>>> a = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> for x in a:
...     t1, t2 = x  # multiple variable assignment
```

But Python allows us to do everything directly in the `for` statement, without any extra variables:

```foo
>>> a = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> for t1, t2 in a:
```

All of these cases involved a multiple assignement, in which multiple variables are assigned values at once using a sequence value. A requirement in all of these cases is that the number of variables must exactly match the length of the sequence. Otherwise, you'll get an error.

> If you have a function that can return a variable number of values depending on certain conditions, you won't be able to call the function in a multiple assignment statement. Instead, you can assign the returned value to a single variable, and then inspect the variable to determine what was returned.

## Zipping sequences

Consider again the case above involving a `for` statement with multiple variables:

```foo
>>> a = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> for t1, t2 in a:
```

There are often situations in which you want a `for` loop in which you make use of a combination of values. Having these as a sequence of n-tuples is very convenient since it allows you to write a concise `for` statement like that shown above. But the data might not start out as a sequence of n-tuples organized in the required way. Rather, you might start out with separate lists that have corresponding values in order. For example,

```python
>>> first_names = ['John', 'Sally', 'Walter']
>>> last_names = ['Jones', 'Smith', 'White']
```

We could work with the data organized this way:

```python
>>> first_names = ['John', 'Sally', 'Walter']
>>> last_names = ['Jones', 'Smith', 'White']
>>> for i in range(3):
...     print("{} {}".format(first_names[i], last_names[i]))
...
John Jones
Sally Smith
Walter White
```

But often it will be much more convenient if we could easily combine the corresponding values into n-tuples, such as this:

```python
>>> names = [('John', 'Jones'), ('Sally', 'Smith'), ('Walter', 'White')]
>>> for first, last in names:
...     print("{} {}".format(first, last))
...
John Jones
Sally Smith
Walter White
```

Python has a built-in function that does just this: `zip()`. Zip takes multiple iterable objects, and iterates over them in parallel.

```python
>>> for first, last in zip(first_names, last_names):
...     print("{} {}".format(first, last))
...
John Jones
Sally Smith
Walter White
```

To be more precise, `zip()` takes one or more iterables and returns an iterator of tuples with elements from the argument iterables combined into the tuples. The elements from the source interables are combined into tuples in the order the argument iterables are listed. The following example illustrates this more clearly:

```python
>>> for item in zip([30, 60, 100], ['slow', 'medium', 'fast']):
...     print(item)
...
(30, 'slow')
(60, 'medium')
(100, 'fast')
```

Notice how the two lists are combined, and that the _i_-th item printed combines the _i_-th element from the first list followed by the _i_-th item from the second list. 

Also, notice that each `item` is a `tuple` object. Let's modify the `print` statement to show that:

```python
>>> for item in zip([30, 60, 100], ['slow', 'medium', 'fast']):
...     print("{}: {}".format(type(item), item))
...
<class 'tuple'>: (30, 'slow')
<class 'tuple'>: (60, 'medium')
<class 'tuple'>: (100, 'fast')
```

It's important to understand that the object returned by `zip()` is not, itself, a list or tuple. For example, if you passed it directly as an argument to `print()`, you won't see the tuples:

```python
>>> print(zip([30, 60, 100], ['slow', 'medium', 'fast']))
<zip object at 0x000001D6069D6100>
```

However, it is an iterator, so it can generate a sequence _when used in a context that causes it to iterate_. In this regard, it's very much like a `range` object. Earlier, we saw that we can unpack a `range` using `*` to get the list of values it can generate. We can do the same with a `zip` object:

```foo
>>> print(*zip([30, 60, 100], ['slow', 'medium', 'fast']))
(30, 'slow') (60, 'medium') (100, 'fast')
```

Unpacking the zip in this case has the effect of passing each tuple as a separate argument to `print()`.

Now, you might be wondering what will happen if the iterables passed into `zip()` do not have the same length. By default, `zip()` will stop when the shortest iterable is exhausted. 

Since Python version 3.10, the `zip()` function also has an optional, named parameter, `strict`: if set to `True`, it will raise an error if the code tries to iterate past the length of the shortest iterable:

```python
>>> for item in zip([1,2], ['a', 'b', 'c'], strict=True):
...     print(item)
...
(1, 'a')
(2, 'b')
Traceback (most recent call last):
  File "<python-input-122>", line 1, in <module>
    for item in zip([1,2], ['a', 'b', 'c'], strict=True):
                ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: zip() argument 2 is longer than argument 1
```

**Note:** A `zip` iterator object can be iterated over only once! After it has been consumed, it can't be reset and could appear to be empty. For example:

```python
>>> zipped = zip([1,2,3], ['a','b','c'])
>>> list(zipped)
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> list(zipped)
[]
```

For this reason, a `zip` object is often created at the point where the generated tuple sequence will be used.

If you want to use zipped data more than once, you can recreate it where needed, or you could use the `zip` object once to generate a tuple or list object which can be re-used:

```python
>>> zipped = list(zip([1,2,3], ['a','b','c']))
>>> zipped
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> zipped
[(1, 'a'), (2, 'b'), (3, 'c')]
```

## Unzipping

One way to think about what `zip()` does is that it turns rows into columns and columns into rows. Because of this, just as you can use `zip()` to combine two sequences, you can also use it on the combined sequences to get back the original—_"unzipping"_, as it were. Let's see how this works.

First, we need to keep in mind the earlier note, that a `zip` object can only be iterated on once. So, for this part, when we use `zip()` to combine the original sequences, we will create a `list` from the result so that it can be iterated over more than once.

```python
>>> zipped = list(zip([30, 60, 100], ['slow', 'medium', 'fast']))
>>> print(zipped)
[(30, 'slow'), (60, 'medium'), (100, 'fast')]
```

If we think of the two lists that were passed in as two rows of a matrix, what `zip()` has provided are the columns. We should be able to call it again passing the columns and get back the rows.

The `zip()` function requries iterable arguments. The `zipped` object is a single `list` object, but it contains three tuples, and tuples are iterable. If we apply the `*` operator to `zipped` and pass that combination into `zip()`, we will be passing three tuples into `zip()`.

> The syntax for this can look a little unusual: you use the `zip()` function in conjunction with the unpacking operator, `*`, applied to the argument.

```python
>>> unzipped = zip(*zipped)
>>> list(unzipped)
[(30, 60, 100), ('slow', 'medium', 'fast')]
```

The sequence types may be different from what we started with (tuples rather than lists), but we have gotten back the same sequences we started with.

Note that the sequences are always returned as tuples, regardless of what type of iterables were originally passed as arguments.

```python
>>> zipped = zip(range(3), ['a','b','c'])
>>> list(zip(*zipped))
[(0, 1, 2), ('a', 'b', 'c')]
```

## Using `zip()` to transpose a matrix

Since we can think of `zip()` as turning rows into columns, we see that it provides an easy way to transpose a matrix. This was seen implicitly in the previous section, but let's look at it more specifically as performing a matrix operation.

Suppose you have a 3 &#xd7; 4 matrix represented as a list of three elements for rows, each of which is a list of four elements for columns within a row.

```python
    matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]
    ]
```

The lists representing rows are iterables, so can be passed as arguments into `zip()`. Let's pass `matrix` into the `zip()` function, using `*` to unpack its rows:

```python
    transposed = list(zip(*matrix))
```

Now let's see the result:

```python
    print(transposed)
```
```
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

The result is a list with four elements, each of which is a 3-tuple, and represents 4 &#xd7; 3 matrix that is the transpose of the original matrix.

