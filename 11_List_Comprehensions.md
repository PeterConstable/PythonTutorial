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

In a list comprehension expression, we've seen that the first component on the left inside the ```[...]``` is an expression that gives the list element values. This expression could itself be a list comprehension generating embedded lists as the elements of the top-level list.

Here's a simple example:

```foo
>>> my_list = [ [x for x in range(3)] for y in range(4) ]
>>>
>>> my_list
[[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

Earlier, when we had multiple ```for``` expressions, the first formed an outer loop and the second an inner loop. Here, the ```[x for ...]``` comprehension is embedded and creates an inner loop, while the following ```for y``` forms an outer loop. This example does the same thing as the following:

```foo
>>> my_list = []
>>> for y in range(4):
...     element = [x for x in range(3)]
...     my_list.append(element)
...
>>> my_list
[[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
```

When reading code with a nested list comprehension, it's helpful to start with the ```for``` after the nested compehension expression to understand what the code does.

In the example above, the outer variable ```y``` wasn't referenced within the nested comprehension. Usually, it will get used within the nested comprehension.

```foo
>>> my_list = [ [x * y for x in range(1,4)] for y in range(1,5)]
>>>
>>> my_list
[[1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12]]
```

Nested comprehensions can be used to generate a table of data—a list of lists in which the embedded lists are uniform in size and kind of content. But you can also use nested comprehensions to generate a list of numbers if you use the embedded comprehension to create lists that are used as input to a numeric operation. For example, a triangular number sequence can be generated as follows:

```foo
>>> my_list = [ sum([x for x in range(1,y)]) for y in range(1,11) ]
>>>
>>> my_list
[0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
```

One way nested comprehensions can be used is to make changes to a table of data—an existing list of lists. Suppose you were trying to parse an HTML page to get information from a ```<table>``` within the page and ended up with data like the following:

```python
>>> table_rows
['\n', ['\n', '<tr>', '\n', ['<th>', '\n', 'First name', '\n', '</th>'], '\n', ['<th>', '\n', 'Last name', '\n', '</th>'], '\n', '</tr>'], '\n', ['\n', '<tr>', '\n', ['<td>', '\n', 'Eliza', '\n', '</td>'], '\n', ['<td>', '\n', 'Doolittle', '\n', '</td>'], '\n', '</tr>'], '\n']
```

The parse has, unfortunately, preserved new-line characters from the source file as siblings of begin or end tags and content, which is not what you want. Ultimately, you're after just the text within the cells; but to get there, we first need to get rid of the new-line cruft. Data that looked like the following (prettified for clarity) would be a step in the right direction:

```python
[
  ['<tr>',
    ['<th>', 'First name', '</th>'],
    ['<th>', 'Last name', '</th>'],
  '</tr>'],
  ['<tr>',
    ['<td>', 'Eliza', '</td>'],
    ['<td>', 'Doolittle', '</td>']
  '</tr>']
]
```

> If you need to parse HTML source content to extract data, there are libraries like [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) that do that. When parsing tables, though, you'll probably need to create some of your own logic to massage data into the format you want. This example is similar to what might be needed using BeautifulSoup, but without details specifically related to it.

We can start by cleaning up the first layer, getting rid of the false rows.

```python
>>> cleaner_rows = [row for row in table_rows if row != '\n']
>>>
>>> cleaner_rows
[['\n', '<tr>', '\n', ['<th>', '\n', 'First name', '\n', '</th>'], '\n', ['<th>', '\n', 'Last name', '\n', '</th>'], '\n', '</tr>'], ['\n', '<tr>', '\n', ['<td>', '\n', 'Eliza', '\n', '</td>'], '\n', ['<td>', '\n', 'Doolittle', '\n', '</td>'], '\n', '</tr>']]
```

That got rid of three new-lines at the top layer of the hierarchy. But now we need to tackle the next layer: each row being a list of "cells". To clean this up, we'll use a nested comprehension:

```python
>>> even_cleaner_rows = [
...     [cell for cell in row if cell != '\n']
...     for row in cleaner_rows
... ]
>>>
>>> even_cleaner_rows
[['<tr>', ['<th>', '\n', 'First name', '\n', '</th>'], ['<th>', '\n', 'Last name', '\n', '</th>'], '</tr>'], ['<tr>', ['<td>', '\n', 'Eliza', '\n', '</td>'], ['<td>', '\n', 'Doolittle', '\n', '</td>'], '</tr>']]
>>>
```

We have one more layer in the hierarchy to clean up. That means one more level of nesting.

```python
>>> clean_table = [
...     [
...         [item for item in cell if item != '\n']
...         for cell in row
...     ]
...     for row in even_cleaner_rows
... ]
>>>
>>> clean_table
[[['<', 't', 'r', '>'], ['<th>', 'First name', '</th>'], ['<th>', 'Last name', '</th>'], ['<', '/', 't', 'r', '>']], [['<', 't', 'r', '>'], ['<td>', 'Eliza', '</td>'], ['<td>', 'Doolittle', '</td>'], ['<', '/', 't', 'r', '>']]]
```

Oops! We split up tag strings like ```'<tr>'``` into lists of characters. We need to add a ternary condition in the middle layer so that we only use the innermost comprehension when ```cell``` is a list, not a string.

```python
>>> clean_table = [
...     [
...         [item for item in cell if item != '\n']
...         if isinstance(cell, list) else cell
...         for cell in row
...     ]
...     for row in even_cleaner_rows
... ]
>>>
>>> clean_table
[['<tr>', ['<th>', 'First name', '</th>'], ['<th>', 'Last name', '</th>'], '</tr>'], ['<tr>', ['<td>', 'Eliza', '</td>'], ['<td>', 'Doolittle', '</td>'], '</tr>']]
```

Yay! We got there.

Now, we did this in three steps: clean up top, second and third levels one after the other. Combining into a single, combined statement isn't much more complicated, now that we know how:

```python
>>> clean_table = [
...     [
...         [item for item in cell if item != '\n']
...         if isinstance(cell, list) else cell
...         for cell in row if cell != '\n'
...     ]
...     for row in table_rows if row != '\n'
... ]
>>>
>>> clean_table
[['<tr>', ['<th>', 'First name', '</th>'], ['<th>', 'Last name', '</th>'], '</tr>'], ['<tr>', ['<td>', 'Eliza', '</td>'], ['<td>', 'Doolittle', '</td>'], '</tr>']]
```

Nesting of comprehensions can be very useful, but watch out you don't make code hard to read! Keep these principles in mind:

* Simple is better than complex.
* Complex is better than complicated.
* Flat is better than nested.
* Readability counts.

The data in our example imposed a level of nesting we had to work with. By writing the code across multiple lines and indented, it shouldn't be hard for someone to read the code later if they're familiar with list comprehensions _and they know the data is a list of lists of lists_. Adding comments to explain that would help.

Let's consider one more example of a nested list comprehension. This is taken from [The Python tutorial](https://docs.python.org/3.8/tutorial/datastructures.html#nested-list-comprehensions). Suppose we have an object representing a 3 × 4 matrix:

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]
```

Now suppose we want to transpose this to a 4 × 3 matrix. We can use a nested comprehension:

```python
transposed = [
    [row[i] for row in matrix]
    for i in range(4)
]
```

This is simpler than the previous example in the sense that it has less nesting and fewer lines of code. But you might not find it easier to reason over.

Start with the outermost ```for```: We have an outer loop that will generate a top-level list of 4 items.

Now consider the nested comprehension. Keep in mind that this is an inner loop, and so the value of ```i``` is fixed while this inner loop iterates. It may help to consider a particular value:

```[row[2] for row in matrix]```

This is iterating over the row items in ```matrix```, taking the third element from each row. So, it will generate a list, ```[3, 7, 11]```.

When you want to write code using nested comprehensions, you'll probably find it helpful to reason from the outer layer inward. _What is needed at the outermost layer?_ Start by writing the (still incomplete) code for that, and include comments:

```python
transposed = [
    # nested comprehension to generate a transposed row
    for i in range(4) # transposed matrix will have 4 rows
]
```

Then work on the inner layer, having a fixed value for the variable from the outer layer in mind.

```python
# nested comprehension to generate a transposed row
[
    # transposed[2] row takes the third item from each row in matrix
    row[2] for row in matrix
]
```

Now generalize that and integrate with the outer layer

```python
transposed = [
    # nested comprehension to generate a transposed row
    [row[i] for row in matrix] # row n takes nth item from each row in matrix
    for i in range(4) # transposed matrix will have 4 rows
]
```

When massaging data in a multi-level hierarchy, as we did for the HTML table data example, work in steps: start with the top (outer) layer, figuring out what's needed for that. Then work through subsequent layers down (inward).

## What's next
