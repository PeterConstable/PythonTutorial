# Flow Control Using ```for```

[sof]:/sof
In [lesson 6](6_Intro_Functions_Flow_Control.md#sof) we learned about ways to control execution flow using ```if``` and ```while``` statements. In this lesson, we'll cover Python's ```for``` statement.

## ```for``` is for sequences

In other programming languages, ```for``` statements are frequently used in a pattern something like this:

```cs
    for (int i = 0; i < numItems; i++)
    {
        item = collection_of_items[i];
        // do something with item
    }
```

There are certainly other ways ```for``` could be used in those languages, but probably the vast majority of uses look like that: index over some numeric range, _start_, _start + 1_, ... and access items from some sequence collection.

Note that the same thing could also be done easily using a ```while``` loop.

Also note that the pattern above uses _two_ variables in the loop: the counter, ```i```, and ```item```. ```item``` is what you want to manipulate in each loop; ```i``` is only used to access the item. What if there was a way to achieve the same thing with just one variable?

Welcome to Python's ```for``` statement! In Python, ```for``` is designed specifically to work with sequences, and allows you to loop through items in a sequence without needing a separate variable just to index the items.

A ```for``` statement is structured like this:

```python
    for <vars> in <sequence_object>:
        <execution block>
    else:
        <execution block>
```

We'll start with the simplest form:

```python
    for <var> in <sequence_object>:
        <execution block>
```

Earlier we learned about ```in``` as a comparison operator for testing if something is contained in a sequence. This is another use for ```in```: to access the elements of a sequence within a ```for``` loop.

The sequence object can be any sequence-type object, or container-like object that supports iterating through contained items sequentially. You can use whatever variable name you want. On each loop, an element from the sequence is assigned to the variable, and execution block is executed.

The following example steps through the characters in a string:

```foo
>>> for char in "abc":
...     print(char)
...
a
b
c
```

It works the same way using a list or tuple.

```foo
>>> x = ["cat", "dog", "tarantula"]
>>> for pet in x:
...     print(pet)
...
cat
dog
tarantula
```

### ```for``` and ranges

In the previous lesson, we learned that ranges are a special kind of sequence. Ranges are immutable, like tuples, but they're much more limited: they can only hold sequences of numbers with a regular step interval. Ranges are mainly intended for use in ```for``` statements.

```foo
>>> for x in range(1,5):
...     print(x, "squared is", x**2)
...
1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
```

When needed, we can use a range to provide a counter sequence and access items from a collection by index, as in ```for``` loops in other languages.

```foo
>>> x = ["cat", "dog", "tarantula"]
>>> for i in range(len(x)):
...     pet = x[i]
...     print(pet)
...
cat
dog
tarantula
```

### Using ```pass```

A ```for``` loop must have a non-empty execution block; otherwise, you'll get an error. If for some reason you need to write a ```for``` statement but don't have an execution block, you can add a ```pass``` statement to avoid an error.

```python
    for x in range(10):
        pass
```

## Changing a sequence within the loop

In some situations, you may need to step through a list but then make changes to it without the loop. In any programming language, doing this kind of thing is bug prone and can be tricky to get right. In particular, as you step through a sequence, if you add or remove an item, then your counter gets out of sync with the sequence contents.

In Python, the sequence in the ```for``` statement is evaluated only once, before the first iteration. If an element is added within the loop, the runtime can get end up operating on the same element repeatedly. Or if an element is removed, then a following element in the sequence may be skipped.

Consider this example:

```foo
>>> my_list = [1,2,3,4,5]
>>>
>>> for x in my_list:
...     my_list.remove(x)
...
>>> print(my_list)
[2, 4]
```

On the first iteration, ```1``` is removed. At that point, the current position within the sequence is pointing at the following element, ```2```. The, for the second iteration, the runtime advances to the next element, which is ```3```. So, ```2``` gets skipped.

To avoid these kinds of problems, use a copy of the sequence in the ```for``` statement.

```foo
>>> my_list = [1,2,3,4,5]
>>>
>>> for x in list(my_list):
...     my_list.remove(x)
...
>>> print(my_list)
[]
```

## Nested loops

A common situation is to have a list of lists (or other type of sequence). You might need to loop through all the elements in each second-level list. That's easy to do by nesting a ```for``` loop inside a ```for``` loop.

```foo
>>> my_list = [[1,2], "cat", (3,4)]
>>> for x in my_list:
...     for y in x:
...         print(y)
...
1
2
c
a
t
3
4
```

In this example, the top-level list contains three sequence-type objects (that happen to be of different types). In the top-level ```for``` loop, ```x``` is assigned an element from the top-level sequence. And because ```x``` is a sequence object, it can be used as the sequence that is stepped through in the second-level ```for``` loop.

You can nest ```for``` loops as many levels deep as you need. But watch that you don't try to iterate over elements of an object that isn't a sequence. In the following example, one element in ```my_list``` is a sequence but the other is not. When the second element, ```42``` gets used in the second-level ```for``` loop as though it were a sequence, an error occurs:

```foo
>>> my_list = ["dog", 42]
>>> for x in my_list:
...     for y in x:
...         print(y)
...
d
o
g
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'int' object is not iterable
```

To handle that situation, we can add logic to check whether an element is a sequence or not:

```foo
>>> my_list = ["cat", 42]
>>> for x in my_list:
...     if isinstance(x, (list, tuple, str)):
...         for y in x:
...             print(y)
...     else:
...         print(x)
...
c
a
t
42
```

## ```for```... ```else```

## ```break``` and ```continue```

## Using multiple variables

## What's next
