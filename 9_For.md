# Flow Control Using ```for```

In [lesson 6](6_Intro_Functions_Flow_Control.md) we learned about ways to control execution flow using ```if``` and ```while``` statements. In this lesson, we'll cover Python's ```for``` statement.

* [```for``` is for sequences](#for-is-for-sequences)
* [Changing a sequence within the loop](#changing-a-sequence-within-the-loop)
* [Nested loops](#nested-loops)
* [```for```... ```else```](#for-else)
* [```break``` and ```continue```](#break-and-continue)
* [Using multiple element variables](#using-multiple-element-variables)
* [What's next](#whats-next)

## ```for``` is for sequences

In other programming languages, ```for``` statements are frequently used in a pattern something like this:

```cs
    for (int i = 0; i < numItems; i++)
    {
        item = collection_of_items[i];
        // do something with item
    }
```

There are certainly other ways ```for``` could be used in those languages, but probably the majority of uses look like that: index over some numeric range, _start_, _start + 1_, ... and access items from some sequence collection.

Note that the same thing could also be done easily using a ```while``` loop.

Also note that the pattern above uses _two_ variables in the loop: the counter, ```i```, and ```item```. ```item``` is what you want to manipulate in each loop; ```i``` is only used to access the item. What if there was a way to achieve the same thing with just one variable?

Welcome to Python's ```for``` statement! In Python, ```for``` is designed specifically to work with iterable objects such as sequences, and allows you to loop through items sequentially without needing a separate variable just to index the items.

> Iterables were introduced briefly in the previous lesson: any object that can return its members one at a type. Strings, lists, tuples and ranges are all iterables. There are other built-in types that we haven't looked at yet that are also interables, including dictionaries and file objects.
> 
A ```for``` statement is structured like this:

```python
    for <var> in <iterable_object>:
        <execution block>
    else:
        <execution block>
```

We'll start with the simplest form:

```python
    for <var> in <iterable_object>:
        <execution block>
```

Earlier we learned about ```in``` as a comparison operator for testing if something is contained in a sequence. This is another use for ```in```: to access the elements of a sequence within a ```for``` loop.

The `iterable_object` can be any sequence-type object or other iterable object. You can use whatever variable name you want. On each loop, an element from the sequence is assigned to the variable, and the execution block is executed.

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

In some situations, you may need to step through a list but then make changes to it within the execution loop. In any programming language, doing this kind of thing is bug prone and can be tricky to get right. In particular, as you step through a sequence, if you add or remove an item, then your counter gets out of sync with the sequence contents.

In Python, the sequence reference in the ```for``` statement is evaluated only once, before the first iteration. But it's identifying the sequence object at that point, not all the elements in the sequence. The implementation is stepping through elements by position. So, if the elements change while a loop is executed, the implementation knows what position it's at, but not that the elements are changing. If an element is added within the loop, the runtime can end up operating on the same element repeatedly. Or if an element is removed, then a following element in the sequence may be skipped.

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

When the `for` statement is executed, `my_list` is evaluated as an iterator. On the first iteration, the iterator index is 0, so it points at `1`. When the block is executed, ```1``` is removed. Right at that point, the iterator index is still 0, which is now pointing at the  ```2```. Then, for the next iteration, the runtime advances to the next element (at index 1), which is ```3```. So, ```2``` gets skipped. On the third iteration, it gets the third element from the modified list, which is `5`, and removes that; `4` is skipped. 

> Note: The runtime implementation recognizes when the iterator has run out of elements, so it doesn't attempt to execute the loop a fourth time.

To avoid these kinds of problems, you can create a copy of the sequence in the ```for``` statement.

```foo
>>> my_list = [1,2,3,4,5]
>>>
>>> for x in list(my_list):
...     my_list.remove(x)
...
>>> print(my_list)
[]
```

Instead of `list(my_list)`, you could also request a _slice_ comprised of the whole list, `my_list[:]`.

>_Q: Why did using a copy of the list work?_
>
> The ```.remove()``` method takes an _object reference_, not a _position_ in the sequence. But the runtime implementation of ```for``` is stepping through elements by position. In the original case without creating a copy, after ```1``` was removed, the objects referred to at each position changed. But in the second case, using a copy, removing ```1``` from my_list doesn't affect the object references at each position of the copy. So the loop will execute once for all five elements. In each pass, ```.remove()``` will get an object reference and will look for that object within ```my_list```, regardless of what position it's in at that point.

## Nested loops

A common situation is to have a list of lists (or other type of sequence). You might need to loop through all the elements in each second-level list. That's easy to do by nesting a ```for``` loop inside a ```for``` loop.

```foo
>>> my_list = [[1,2], "cat", (3,4)]
>>>
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
>>>
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
>>>
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

> This allows for the sequence types `list`, `tuple` and `str`, but not other iterable types. There is a way to generalize this to any iterable object, but in some Python versions (3.3 and later) it requires using a library module, [collections.abc](https://docs.python.org/3/library/collections.abc.html). Importing from other modules will be covered in a future lesson.

## ```for```... ```else```

In Python, a ```for``` statement can have a following ```else```. The ```else``` block is executed after the ```for``` loop has completed.

```foo
>>> for x in [1,2,3]:
...     print(x)
... else:
...     print("done!")
...
1
2
3
done!
```

If it turns out the sequence in the ```for``` statement is empty, the ```else``` block will still be executed.

```foo
>>> a = ""
>>> for x in a:
...     print(x)
... else:
...     print("done!")
...
done!
```

You might notice that the previous example could have been implemented without using ```else``` by raising the following ```print()``` statement out of the ```for``` construct as the next top-level statement.

```foo
>>> a = ""
>>> for x in a:
...     print(x)
... print("done!")
...
done!
```

There's a signficant difference if a ```break``` statement is used within the loop, however. We'll cover that next.

## ```break``` and ```continue```

In the [previous lesson](6_Intro_Functions_Flow_Control.md#the-while-statement), we saw that a ```while``` loop can include ```break``` or ```continue``` statements to alter the flow. These can also be used in ```for``` loops.

A ```break``` statement can be used within the ```for``` loop to exit early out of the loop if some condition is met. Any statements within the execution block that come after ```break``` are skipped. If there is an ```else``` block, that will also be skipped.

In the next example, the ```for``` statement is set up to loop over a long sequence of numbers. But within the loop, a condition is used to ```break``` out of the loop early.

```foo
>>> for x in range(1000):
...     if x == 3:
...         break
...     else:
...         print(x)
... else:
...     print("done!")
...
0
1
2
```

Note that the ```else``` block was not executed.

Within the loop, ```continue``` can be used to skip the remainder of the loop _for that iteration_. Flow will return to the top of the loop and continue with the next sequence element (if there is one).

The following example loops over a range and prints each number, but skip any number that is a multiple of 3.

```foo
>>> for x in range(10):
...     if x % 3 == 0:
...         continue
...     else:
...         print(x)
... else:
...     print("done!")
...
1
2
4
5
7
8
done!
```

Note that the ```else``` block gets executed: ```continue``` never causes that to be skipped.

## Using multiple element variables

Earlier we looked at using nested loops to interate over a list of lists. In some situations, you may have a list of sequences of some size, and want to operate all of the elements in those sequences together in the same loop, not one-by-one in separate loops. Consider this example:

```foo
>>> a = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> for x in a:
...     print("item", x[0], 'is a', x[1])
...
item 1 is a cat
item 2 is a toad
item 3 is a mouse
```

The elements in list ```a``` are tuples. In the ```for``` statement, each tuple element gets assigned to ```x```. Then within the loop, we index into the tuple to access elements as needed. A different way we could have done things is to use a multiple assignment statement within the loop to assign the tuple elements to different variables.

```foo
>>> a = [(1, 'cat'), (2, 'toad'), (3, 'mouse')]
>>>
>>> for x in a:
...     t1, t2 = x  # multiple variable assignment
...
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

But notice we've used a spare variable, ```x```, just as a means to get to assign the tuple elements to ```t1``` and ```t2```.

In Python, we can avoid that extra variable and do the multiple assignment directly in the ```for``` statement.

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

On each iteration of the loop, a tuple element is obtained from ```a``` and the elements are assigned to the tuple of variables ```t1, t2```.

Our example has used a list of tuple elements, but any sequence type could be used.

**Note, however:** the number of variables and the length of each sequence object within the top-level sequence must always be the same. Otherwise, you'll get an error.

## What's next

We've learned about three common mechanisms in Python for organizing code and flow control. In the [next lesson](10_Intro_Functions.md), we'll learn about one more you'll use a lot, functions.
