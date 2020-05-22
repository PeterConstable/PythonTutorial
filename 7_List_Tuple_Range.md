# Sequence Types: Lists, Tuples and Ranges

[sof]
We've learned about several basic types in Python: numbers, booleans and strings. There was one important way that strings differed from the others: strings are a container-like type, and specifically a _sequence type_. In this lesson, we'll learn about some other sequence types, ```list```, ```tuple``` and ```range```.

There are several operations that can be performed on any sequence type. We'll introduce each type first, and the go over the common operations.

* [Lists](#lists)
* [Tuples](#tuples)
* [Ranges](#ranges)
* [Common sequence operations](#common-sequence-operations)
* [Lists are mutable](#lists-are-mutable)
* [Converting between sequence types](#converting-between-sequence-types)
* [Tuples as returned values](#tuples-as-returned-values)
* [What's next](#whats-next)

## Lists

A ```list``` is a mutable sequence—an ordered set—of objects. The objects can be of any type, and can mix different types. Lists are represented using square brackets, ```[...]```, with zero or more elements delimited with commas.

```foo
>>> [1, 29, 13]
[1, 29, 13]
```

You can assign a list to a variable, and the variable will become an instance of the ```list``` type.

```foo
>>> x = [3.14, "spam"]
>>> isinstance(x, list)
True
```

When learning about strings, we were introduced to the ```len()``` function. It can be used with lists, or any container-like type, to get the number of elements.

```foo
>>> len(x)
2
```

You can initialize a variable as an empty list. (You'll be able to add elements later.) Just assign ```[]```.

```foo
>>> x = []
>>> len(x)
0
```

The ```list()``` constructor function can also be used to create a list object from another sequence object. This would be a new list; so this is a way to copy a list into a new object.

```foo
>>> x = [3.14, "spam"]
>>> y = list(x)
>>> y
[3.14, 'spam']
>>> y is x
False
```

Unlike strings, list objects are mutable—that is, the elements of a list sequence can be changed without needing to create a new list object. We'll return to this below, after discussing common sequence operations.

## Tuples

A ```tuple``` is an immutable sequence of objects. As with a list, a tuple can have zero or more objects of any type, including a mixture of different types. Tuples are represented using parentheses, ```(...)```, with commas separating the elements.

```foo
>>> (1, 29, 13)
(1, 29, 13)
```

Note that the elements can be any type of object, including lists or any other kind of container-like object. In the following example, ```x``` is a tuple consisting of a string followed by a list.

```foo
>>> x = ("cats", [1, 29, 13])
>>> x
('cats', [1, 29, 13])
>>> len(x)
2
```

A tuple can be empty:

```foo
>>> x = ()
>>> len(x)
0
```

Tuples can be constructed in a few different ways. We've seen examples above using ```(...)```. You can also use the ```tuple()``` constructor function, passing in a sequence object. But you can also simply write out two or more items, separated with commas, without needing to use parentheses:

```foo
>>> x = "spam", "eggs"
>>> x
('spam', 'eggs')
>>> type(x)
<class 'tuple'>
```

In [lesson 4](4_More_Assignment_Numbers_Strings.md#multiple-assignment), we learned how to assign values to multiple variables in a single statement.

```foo
>>> x, y = 42, "hey, there!"
>>> x
42
>>> y
'hey, there!'
```

We can see now that the mechanism involved is to assign a tuple of values, ```42, "hey, there!"```, to a tuple of variables, ```x, y```.

Singleton tuples need some special consideration. If you simply write a single value inside parentheses or on it's own, it will be interpreted as that object, not as a tuple containing that object.

```foo
>>> x = (5)
>>> type(x)
<class 'int'>
```

If you need something to be interpreted as a singleton tuple, then you need to add a comma after:

```foo
>>> x = 5,
>>> x
(5,)
>>> y = ("cat",)
>>> y
('cat',)
```

## Ranges

The ```range``` type is a special sequence type. Range objects are sequences of integers. They are immutable (elements can't be changed) and can only be constructed using the ```range()``` constructor function. For example, ```range(5)``` returns a range with a sequence of five numbers, 0 to 4.

Ranges behave like lists in many ways, but not in every way. One difference is in how they're represented as a result.

```foo
>>> x = [0,1,2,3]
>>> y = range(4)
>>> x
[0, 1, 2, 3]
>>> y
range(0, 4)
```

In this example, ```x``` and ```y``` have the same numbers as elements; but they're different types of objects. The easiest way to see that is to use the ```list()``` function to convert the range to a list:

```foo
>>> list(y)
[0, 1, 2, 3]
```

To construct a range, the ```range()``` can take one, two or three parameters. We've seen examples for ```range()``` taking one parameter, which indicates the _end_ or _length_ of the range: the range sequence will begin at 0 and end _one before_ the _end_ value.

(This is simlar to the range specifications we saw to get a slice from a string: ```mystring[:5]``` will have 5 elements starting at index 0 and ending _before_ index 5.)

Note: if _end_ is less than or equal to 0, you'll get an empty range.

```foo
>>> x = range(0)
>>> len(x)
0
>>> list(x)
[]
```

```range()``` can also take two parameters, _start_ and _end_. The range sequence will have _end_ - _start_ elements, beginning at _start_ value and ending _one before_ the _end_ value.

```foo
>>> x = range(5, 10)
>>> len(x)
5
>>> list(x)
[5, 6, 7, 8, 9]
```

If _end_ is less than or equal to _start_, you'll get an empty range.

```foo
>>> x = range(17, 13)
>>> len(x)
0
>>> list(x)
[]
```

With one or two parameters, the elements always increase by +1. ```range()``` can take a third parameter, _step_, which allows you to specify a different step size. For example:

```foo
>>> x = range(10, 20, 3)
>>> list(x)
[10, 13, 16, 19]
```

The number of elements will be (_end_ - _start_) // _step_ + 1.

Up to now, the range examples have all had sequences that are increasing. We can construct a range with _decreasing_ numbers if _end_ is less than _start_ **and** _step_ is less than 0.

```foo
>>> x = range(5, 0, -1)
>>> list(x)
[5, 4, 3, 2, 1]
```

```foo
>>> x = range(10, -5, -3)
>>> list(x)
[10, 7, 4, 1, -2]
```

Note that _step_ must not be 0; if it's 0, you'll get an error.

## Converting between sequence types

In discussing ranges, we've made use of the ```list()``` function to convert ranges to lists. Conversions between the different sequence types is possible in some directions, but not others. And of the conversions that _are_ possible, only some are particularly useful.

```list``` and ```tuple``` are really very similar to one another, the key difference being that lists are mutuble while tuples are immutable. You can convert between ```list``` and ```tuple``` in either direction, and get sequences with the same elements.

```foo
>>> list((1,2,3))
[1, 2, 3]
>>> tuple([1,2,3])
(1, 2, 3)
```

If ```x``` is a list, then ```list(tuple(x)) == x``` will always be ```True```. Similarly, if ```x``` is a tuple, then ```tuple(list(x)) == x``` will always be ```True```.

These conversions can be useful. For instance, if you have a tuple and need to get a copy but with some elements changed, you can convert to a list, make changes to elements in the list, and then convert that back to a tuple.

We've seen that a range can be converted to a list; it can also be converted to a tuple. You'll get sequences with the same elements.

```foo
>>> x = range(3, 8)
>>> list(x)
[3, 4, 5, 6, 7]
>>> tuple(x)
(3, 4, 5, 6, 7)
```

This may sometimes be useful. It's a way to see the elements in the range, as we used above; and converting from a range may also be a useful way to initialize a list with a sequence of numbers.

You can't convert a list or a tuple to a range, however. The _only_ way to get a range us using the ```range()``` function in the ways discussed above.

We've mentioned that ```str``` is also a sequence type. You can convert a string to either a list or a tuple, and you'll get a sequence of the characters from the string.

```foo
>>> list("spam")
['s', 'p', 'a', 'm']
>>> tuple("spam")
('s', 'p', 'a', 'm')
```

This isn't often going to be useful, though. For instance, there isn't anything that you can do with a tuple of the character sequence that you couldn't do with the string. Converting to a list could allow you to edit elements in the character sequence; but as we'll see next, you can't get back to a ```str``` object with the value you'd want.

You _can_ convert a list or tuple of characters to a string, but the result probably isn't quite what you'd expect. For example:

```foo
>>> x = list("fig")
>>> str(x)
"['f', 'i', 'g']"
```

The resulting string includes all the brackets, quote marks and commas, as well as the original characters. That's probably not something you'll often want.

Keep in mind that lists and tuples can be sequences of _any types of objects_. But elements of a string can only be Unicode characters. Converting a list or tuple to a string requires coercing any kind of object to a sequence of characters. In the general case, we can't expect something useful.

We run into exactly that limitation if we try to convert a range to a string you just get something like "range(0, 5)".

So, summarizing:

* conversion between ```list``` and ```tuple``` is useful and can round-trip
* conversion _from_ ```range``` _to_ ```list``` or ```tuple``` is possible and _may sometimes_ be useful
* other conversions between ```str```, ```range```, ```list```, ```tuple``` are either not possible or rarely useful

>Note: Later in this lesson we will learn about a way that _is useful_ for getting a string from a list or tuple of characters/strings.

## Conversion to ```bool```

While talking about conversions, we should cover conversions to ```bool```. Recall from [lesson 5](5_Bool_Comparisons.md#booleans—the-bool-type) that any object can be explicitly converted to a boolean value using the ```bool()``` function, or converted implicitly if used in a context where a ```bool``` is expected. And in [lesson 6](6_Intro_Functions_Flow_Control.md#objects-as-if-conditions) we saw that applied by using objects alone as conditions in ```if``` statements. This works for sequence objects as well.

The following example is taken from lesson 6, but shows a ```list``` object getting used as a condition:

```python
>>> def my_func(val):
...     if val:
...         print("true")
...     else:
...         print("false")
...
>>> my_func([1,2,3])
true
```

For all sequence types, including ```str```, ```list```, ```tuple``` and ```range```, an object ```x``` converts to ```True``` if the object has content—i.e., it's a non-empty sequence. But empty sequences (length is 0) convert to ```False```.

```python
>>> my_func("")
false
>>> my_func([])
false
>>> my_func(())
false
>>> my_func(range(0))
false
```

## Common sequence operations

In [lesson 3](3_Intro_Strings.md#strings-as-character-sequences), we learned about several ways to work with sequence elements in strings. All of those can be used with any sequence type. In the next sub-section, we'll review those.

### ```len()```, indexing and slices

We'll review operations we learned about earlier use the following in examples:

```foo
>>> her_name = "Eliza Doolittle"
>>> my_list = ["eggs", "jam", "tea", "raisins"]
```

Use ```len()``` to get the count of elements in a sequence:

```foo
>>> len(her_name)
15
>>> len(my_list)
3
```

Use index notations (base 0) to refer to individual elements in the sequence:

```foo
>>> her_name[3]
'z'
>>> my_list[3]
'raisins'
```

Use _start_ and _end_ indices to get a slice from the sequence:

```foo
>>> her_name[0:5]
'Eliza'
>>> my_list[1:3]
['jam', 'tea']
```

You can include a _step_ in the range specification for a slice:

```foo
>>> her_name[0:8:2]
'EiaD'
>>> my_list[0:3:2]
['eggs', 'tea']
```

>Remember: indices in the sequence range specifications show above and ```range()``` parameters work the same way.

Use negative indices to index from the end of the sequence:

```foo
>>> her_name[-6 : -2]
'litt'
>>> my_list[-3:-1]
['jam', 'tea']
```

You can omit _start_ and will get a slice from the beginning of the sequence:

```foo
>>> her_name[ : 8]
'Eliza Do'
>>> my_list[:3]
['eggs', 'jam', 'tea']
```

You can omit _end_ and will get a slice that goes to the end of the sequence:

```foo
>>> her_name[-5 : ]
'ittle'
>>> my_list[1:]
['jam', 'tea', 'raisins']
```

### Concatenation

We also learned about concatenation of strings. You can also concatenate lists or tuples:

```foo
>>> ["dog", 3] + [2.0, 3-2j]
['dog', 3, 2.0, (3-2j)]
```

```foo
>>> (3, "cat", 42, 'x') + (3.14,)
(3, 'cat', 42, 'x', 3.14)
```

Note that you can only concatenate sequences of the same type. You can't concatenate a list and tuple, for example. (But you can easily convert a list operand to a tuple and then concatenate the tuples, or vice versa.)

You can also use ```*``` concatenation to repeat a list or tuple sequence:

```foo
>>> ["spam"] * 5
['spam', 'spam', 'spam', 'spam', 'spam']
>>> 4 * (1,2)
(1, 2, 1, 2, 1, 2, 1, 2)
```

You can't concatenate ranges, but you can convert ranges using ```list()``` or ```tuple()``` and then concatenate using either of those types.

>Note: When concatenating immutable sequence types, a new object is always created. If you build up a string or tuple sequence with many repeated concatenations, that could have a noticeable performance impact. For ```str``` or ```tuple``` objects, you can avoid that using a list. We'll return to this later in this lesson.

### Membership

In [lesson 5](5_Bool_Comparisons.md#membership), we introduced the ```in``` comparison operator for checking if a given character was contained in a string. We can use ```in``` to test for membership with any sequence type.

```foo
>>> 'o' in her_name
True
>>> "tea" in my_list
True
>>> [1,2] in ([1,2], 9, [3,5]) # tuple of objects
True
>>> 5 in range(8)
True
```

### Counting occurrences

The built-in sequence types have a ```.count()``` method that can be used to count the number of occurrences of something within a sequence.

```foo
>>> her_name.count('o')
2
>>> my_list.count(42)
0
>>> ((3,8) * 4).count(3)
4
>>> range(8).count(8)
0
```

>Note: make sure not to confuse ```.count()``` and ```len()```!

### Finding items

... _[under construction]_

### Aritmetic functions

There are some other sequence operation we didn't discuss for strings. If you have a list or tuple of numbers (```int``` or ```float```, but not ```complex```), then you can use the built-in ```max()``` and ```min()``` functions to get the largest or smallest number. And you can use the ```sum()``` function to add all the numbers in the sequence:

```foo
>>> x = [2, 9, 4.8, 18, 7.0]
>>> max(x)
18
>>> min(x)
2
>>> sum(x)
40.8
```

With these functions, all of the elements in the sequence must be either ```int``` or ```float```; if there's an object of any other type, you'll get an error.

## Lists are mutable

... _[under construction]_

## Tuples as returned values

One situation in which tuples can be very useful is when defining a function that needs to return multiple values: you can write a ```return``` statement that returns a tuple of values.

```python
>>> def get_squares_to_25():
...     return 1, 4, 16, 25
...
>>> get_squares_to_25()
(1, 4, 16, 25)
```

This can be very handy situations in which you need a function to gather and return a number of objects. For example, a function that parses a data structure from a binary file can return all the member values—however many—as a tuple.

When calling such a function, you can assign the result to a variable and then access individual elements as needed.

```python
>>> def my_func():
...     x = get_squares_to_25()
...     if len(x) > 0:
...         # print the third element (16)
...         print(x[2])
...
>>> my_func()
16
```

Instead of assigning the result to a single variable, you can write a tuple of variables for the individual values.

```python
    ...
    startCharCode, endCharCode, startGlyphID = parseRecord()
    ...
```

Note, though, that you must have exactly the same number of variables as the number of values that will be returned. Otherwise, you'll get an error.

If you need to allow for the possibility that the function will return different numbers of values in different situations, one technique you could use is to have first element of the returned tuple indicate the number of following elements, or some similar technique to establish the contract.

```python
def parseRecord():
    ...
    if format == 2:
        # record had three values
        start = 24
        end = 32
        startGlyph = 17
        return 3, start, end, startGlyph
    ...
```

```python
    ...
    fields = parseRecord()
    if fields[0] == 3:
        startCharCode, endCharCode, startGlyphID = fields[1:4]
    ...
```

These are just some of the possibilities.

A function might be defined to return a tuple with a variable number of elements based on some input parameter or other factor. You'll probably encounter this at some point using Python modules developed by others. If you know that a function is returning a singleton tuple, then you can do one of two things. One option is to assign the tuple result to a variable _as a tuple object_, and then access the single element within the tuple variable:

```python
    ...
    result = get_squares(1)
    # singleton result: get the first element
    print(result[0])
    ...
```

Or, you could write a tuple of variables comprised of one variable followed by comma, then use that variable as needed.

```python
    ...
    result, = get_squares(1)
    print(result)
    ...
```

If you're coming from another language and the syntax seems odd, you might find it gives greater clarity to write the tuple for the variable with parentheses:

```python
    ...
    (result,) = get_squares(1)
    print(result)
    ...
```

## What's next

In the previous lesson, we went over the traditional flow control statements ```if``` and ```while```. But we held off on discussing ```for``` because, in Python, the ```for``` statement and sequence types work closely together. There are still some other sequence types that we haven't yet covered, byte sequences; we'll get to those later. We've now got a solid start on sequences; the [next lesson](8_For.md#sof) will introduce Python's ```for``` statements.
