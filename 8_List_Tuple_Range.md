# Sequence Types: Lists, Tuples and Ranges

We've learned about several basic types in Python: numbers, booleans and strings. There was one important way that strings differed from the others: strings are a container-like type, and specifically a _sequence type_. In this lesson, we'll learn about some other sequence types, ```list```, ```tuple``` and ```range```.

There are several operations that can be performed on any sequence type. We'll introduce each type first, and then go over the common operations.

There are also other operations that are specific to strings, or specific to lists and other mutable sequence types; we'll save those topics for later lessons.

* [Lists](#lists)
* [Tuples](#tuples)
* [Ranges](#ranges)
* [Multiple assignment of sequence elements](#multiple-assignment-of-sequence-elements)
* [Converting between sequence types](#converting-between-sequence-types)
* [Common sequence operations](#common-sequence-operations)
* [Mutating list operations](#mutating-list-operations)
* [Tuples as returned values](#tuples-as-returned-values)
* [What's next](#whats-next)

## Lists

A ```list``` is a mutable sequence (or _ordered set_) of objects. The objects can be of any type, and can be a mix different types. Lists are represented using square brackets, ```[...]```, with zero or more elements delimited by commas.

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

Lists can contain any type of object, including another list or any other container-like object. In the following example, ```x``` is a list that contains a string followed by another list.

```foo
>>> y = "cats"
>>> z = [1,2,3]
>>> x = [y, z]
>>>
>>> x
['cats', [1, 2, 3]]
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

Unlike strings, list objects are mutable—that is, the elements of a list sequence can be changed without needing to create a new list object. For example:

```foo
>>> x[0] = 42
>>> x
[42, 'spam']
```

There are a number of ways that list objects can be changed—adding, removing or changing sequence elements. We'll leave most details to a later lesson. One thing we'll cover later in this lesson that involves updating a list sequence is concatenation.

## Tuples

A ```tuple``` is an immutable sequence of objects. As with a list, a tuple can have zero or more objects of any type, including a mix of different types. Tuples are represented using parentheses, ```(...)```, with commas separating the elements.

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

The ```range``` type is a special sequence type. Range objects produce sequences of integers. They are immutable (elements can't be changed) and can only be constructed using the ```range()``` constructor function. For example, ```range(5)``` returns a range with a sequence of five numbers, 0 to 4.

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

>For the duration of this lesson, when we want to show the sequence contained in a range object, we'll convert to a list as a convenient way to get a better representation of the contained sequence.

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

## A brief intro to iterables

Later in this lesson, we'll need to mention objects that are _iterables_. An iterable object is capable of producing a sequence. It can be a sequence itself, in the sense of containing elements; but it might not be. To qualify as an iterable, it just needs to be able to _provide a sequence_ when used in contexts that expect a sequence.

The ```str```, ```list``` and ```tuple``` types are iterable types that are also sequences.

On the other hand, a ```range``` is not actually a sequence: it doesn't contain elements. But it is an iterable and can produce a sequence. This accounts for why it behaves like a sequence in some contexts but not in others, such as how a range object is represented as a result:

```foo
>>> y = range(4)
>>> y
range(0, 4)
```

For now, this covers what we need to know about iterables. We'll explore iterables in more detail in a later lesson.

## Multiple assignment of sequence elements

In [lesson 4](4_More_Assignment_Numbers_Strings.md#multiple-assignment), we learned how to assign values to multiple variables in a single statement.

```foo
>>> x, y = 42, "hey, there!"
>>> x
42
>>> y
'hey, there!'
```

We mentioned above that tuples can be written as items separated by commas without any surrounding parentheses. With that in mind, we can see now that the mechanism involved in the multiple-assignment example is to assign a tuple of values, ```42, "hey, there!"```, to a tuple of variables, ```x, y```.

Note, though, that we haven't assigned the tuple of variables to a named tuple variable. So, we can refer to variables ```x``` and ```y```, but we don't have any variable that refers to the tuple ```(x, y)```. (But we can always assign such a variable later, or just write ```(x, y)```.)

Now, in the example above, the operand on the right was a tuple. The tuple elements were written out in the statement as literals, but we could also have used a tuple variable.

```foo
>>> t = (42, "hey, there!")
>>> x, y = t
>>>
>>> x
42
>>> y
'hey, there!'
```

The right-hand assignment operand could also be a list.

```foo
>>> my_list = [3.14, "pies"]
>>> x, y = my_list
>>>
>>> x
3.14
>>> y
'pies'
```

This also works with any other sequence types, including strings or ranges.

```foo
>>> x, y = "ab"
>>> x
'a'
>>> y
'b'
```

```foo
>>> x,y = range(2)
>>> x
0
>>> y
1
```

**Note!** When assigning sequence elements to a tuple of variables, the number of variables must be the same as the number of sequence elements. Otherwise, you'll get an error.

## Converting between sequence types

In discussing ranges, we've made use of the ```list()``` function to convert ranges to lists. Conversions between the different sequence types is possible in some directions, but not others. And of the conversions that _are_ possible, only some are particularly useful.

```list``` and ```tuple``` are really very similar to one another, the key difference being that lists are mutuble while tuples are immutable. You can convert between ```list``` and ```tuple``` in either direction, and get sequences with the same elements.

```foo
>>> list((1,2,3))
[1, 2, 3]
>>>
>>> tuple([1,2,3])
(1, 2, 3)
```

If ```x``` is a list, then ```list(tuple(x)) == x``` will always be ```True```. Similarly, if ```x``` is a tuple, then ```tuple(list(x)) == x``` will always be ```True```.

These conversions can be useful. For instance, if you have a tuple and need to get a copy but with some elements changed, you can convert to a list, make changes to elements in the list, and then convert that back to a tuple.

We've seen that a range can be converted to a list; it can also be converted to a tuple. You'll get sequences with the same elements.

```foo
>>> x = range(3, 8)
>>>
>>> list(x)
[3, 4, 5, 6, 7]
>>>
>>> tuple(x)
(3, 4, 5, 6, 7)
```

This may sometimes be useful. It's a way to see the elements in the range, as we used above; and converting from a range may also be a useful way to initialize a list with a sequence of numbers.

You can't convert a list or a tuple to a range, however. The _only_ way to get a range us using the ```range()``` function in the ways discussed above.

We've mentioned that ```str``` is also a sequence type. You can convert a string to either a list or a tuple, and you'll get a sequence of the characters from the string.

```foo
>>> list("spam")
['s', 'p', 'a', 'm']
>>>
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
>>>
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

Since `in` is a comparison operator, it returns a `bool`. You can combine that with the `not` boolean operator (`not in`) to check that a value is not in the sequence.

```foo
>>> 'z' not in her_name
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

The built-in sequence types have a ```.index()``` method that can be used to locate an element within a sequence. You give the element you're searching for as an argument, and (if contained) it returns the index for the first occurence of that element in the sequence.

```foo
>>> her_name.index('o')
7
>>> my_list.index("tea")
2
>>> (2, 13, 5, 42, 5, 68).index(5)
2
>>> range(8, 15).index(11)
3
```

You can include a second argument to indicate a starting index to search from:

```foo
>>> her_name.index('l')
1
>>> her_name.index('l', 2)
9
>>> (2,13,5,42,5,68).index(5, 3)
4
```

You can also include both _start_ and _stop_ indices to limit the range within the sequence over which to search.

```foo
>>> her_name.index('l', 11, 15)
13
```

As with other range specifications, the element at the _stop_ index is excluded from the range.

Using ```.index()``` with two indices is nearly the same as getting a slice and then searching within that slice. An important difference, though, is that the one will give you an index from the start of the entire string, while the other will give an index from the start of the slice.

```foo
>>> her_name[11:15].index('l')
2
```

As with other range specifications, you can use negative indices to indicate positions from the end of the sequence. The index returned will still be for the first occurrence _from the start_ of the sequence.

```foo
>>> her_name.index('l', -6, -2)
9
```

Some sequence types—but not all—also have an ```.rindex()``` method that searches from the _end_ of the sequence. The index returned is still an index from the start of the sequence, but it will be for the _last_ occurrence within that sequence. The ```.rindex()``` method isn't available for lists, tuples or ranges, but it is available for strings.

```foo
>>> her_name.rindex('l')
13
>>> her_name.rindex('l', 1, 6)
1
```

Note that, if the object you're searching for isn't contained in the sequence (or sequence range), ```.index()``` or ```.rindex()``` will raise an error.

```foo
>>> (2,13,5,42,5,68).index(9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: tuple.index(x): x not in tuple
```

```foo
>>> her_name.index('l', 2, 9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

In a later lesson, we'll learn about the ```try``` statement that could be used to handle an anticipated error like this. For now, one thing we can do is to check first to see if the object is contained before trying to get its index.

```foo
>>> if 'l' in her_name[2: 9]:
...     print("index is:", her_name.index('l', 2, 9))
... else:
...     print("not found")
...
not found
```

For strings, there's another option available. Some sequence types—but not all—also have a ```.find()``` method you can use instead that doesn't raise an error in this situation. Instead, it returns -1 if the item isn't found. This isn't supported for lists, tuples or ranges, but it is supported for strings.

```foo
>>> her_name.find('l', 2, 9)
-1
```

You may still need to add logic to handle the situation, but this may be more convenient than other approaches.

The examples up to now have been searching for a single element, not a sub-sequence of elements. For strings, the ```.find()``` and ```.index()``` methods allow you to search for substrings as well as individual characters.

```foo
>>> her_name.index("li")
1
>>> her_name.index("le")
13
```

This isn't available for lists, tuples or ranges, however.

If you're working with strings a lot, you'll probably want to make use of regular expressions to search for substring patterns. We'll save more string-specific stuff for a later lesson.

### Arithmetic functions

If you have a list or tuple of numbers (```int``` or ```float```, but not ```complex```), then you can use the built-in ```max()``` and ```min()``` functions to get the largest or smallest number. And you can use the ```sum()``` function to add all the numbers in the sequence:

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

You can also use these functions with a range object. For example, you can easily add integers from 1 to 99 as follows:

```foo
>>> sum(range(1, 100))
4950
```

These functions don't work with strings, however.

### Immutable types and copying

Operations that result in copying objects can have performance impacts, so it's good to be aware when copying will occur. All of the sequence operations we've gone over in this section do not involve changing the sequence contained in a sequence object. Even so, some of them do result in copying and new memory allocation.

Some of the operations we've covered, such as using ```len()``` or ```.index()```, don't return a sequence object. Obviously, these don't result in copying or creating a new sequence object.

For most built-in immutable types, operations like concatenation and slicing that do return a sequence object do result in copying and creating new objects. Note, in particular, that this is true for strings and tuples.

>Later, when we learn about byte sequence types, we'll introduce the ```memoryview``` type, which can be used for immutable data while also supporting getting slices without copying.

Lists, however, are mutable. Because of that, certain operations that result in copying for other types can be done on a list without copying. List concatenation is a particular operation for which this is true. We'll explore that further in a moment.

Slicing always results in a copy, even for a list, and even when specifying a range that includes the entire list. We can see this by doing an identity comparison of a list variable with such a slice on itself.

```foo
>>> x = [1,2,3]
>>> x is x[:]
False
```

The slice resulted in a copy. Let's check another way by assigning the slice to a new variable and then comparing IDs.

```foo
>>> x = [1,2,3]
>>> id(x)
2544697278784
>>>
>>> y = x
>>> id(y)  # will be the same
2544697278784
>>>
>>> y = x[:]  # new copy
>>> id(y)
2544697280576
```

We also saw earlier that ```list()``` will create a new copy.

```foo
>>> y = list(y)  # another new copy
>>> id(y)
2544697280704
```

In certain situations, you may need to change a copy of a list while also retaining the original list. You can use either method above to get a copy.

Concatenation of lists is an important operation that doesn't involve copying. When conconcatenating a list onto another list, the left-hand operand is updated without creating a new object.

Let's compare concatenation of strings versus concatenation of lists. We'll use the ```id()``` function to check if we end up with the same object or a new object. First, strings:

```foo
>>> x = 'a'
>>> id(x)
2544667222448
>>>
>>> x += 'b'
>>> x
'ab'
>>> id(x)
2544697280304
```

After concatenation, we end up with a new string object. Now, lists:

```foo
>>> x = [1,2]
>>> id(x)
2544696974528
>>>
>>> x += [3,4]
>>> x
[1, 2, 3, 4]
>>> id(x)
2544696974528
```

After concatenation, we still have the same list object.

As noted earlier, if you build up a string or tuple through many repeated concatenation, that can have noticeable performance impacts. For tuples, you can avoid any perf impact simply by using a list instead. If you really need to end up with a tuple, then you can wait until the final sequence is assembled and then convert the list to a tuple.

To build up a string from many string fragments in a memory-efficient way, you can assemble the pieces in order as a list, and then create the final string from that list. Now, earlier we saw that converting a list to a string using ```str()``` didn't provide the kind of result we'd want.

```foo
>>> str(['ugly', 'string'])
"['ugly', 'string']"
```

However, the ```str.join()``` method provides a way to do what we want: it joins the fragments together in the way we'd want. To use it, you use it on a delimiting string that will be used to separate all of the string elements in the sequence. In this example, ```" "``` is used.

```foo
>>> " ".join(['good', 'string'])
'good string'
```

The separator string could be any string, including an empty string.

```foo
>>> x = ""
>>> y = ["Eli", "za D", "ool", "ittle"]
>>> x.join(y)
'Eliza Doolittle'
```

### Other immutable sequence operations

For several immutable types, including tuples and ranges, nearly all of the avaialble sequence operations have been covered. The only thing we haven't covered is the ```hash()``` function, which you may need to know about when defining your own custom types; that will be in a later lesson.

```str``` in another immutable type, and has a number of additional, string-specific methods. We'll save those for another lesson that goes into more detail on working with strings.

## Mutating list operations

Because ```list``` is a mutable sequence type, there are several other operations to know about.

>These operations are also relevant for the mutable byte sequence type, ```bytearray```, which we'll cover in later lesson.

### Changing list elements

To change an element in a list, you can simply refer to it by index and assign a new value:

```python
>>> my_list = [2, 4, 7, 8, 10, 12]
>>>
>>> my_list[2] = 6  # change a single element in the list
>>>
>>> my_list
[2, 4, 6, 8, 10, 12]
```

You can change multiple elements by assigning to a slice.

```python
>>> my_list[1:3] = [5, 7]
>>>
>>> my_list
[2, 5, 7, 8, 10, 12]
```

The length of the slice and the length of the sequence being assigned can be different.

```python
>>> my_list[1:3] = [4]
>>>
>>> my_list
[2, 4, 8, 10, 12]
```

This will change the number of elements in the list.

Note that, when assigning to a slice in this way, you must assign a sequence object, not a single number; that will raise an error.

```python
>>> my_list[1:3] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only assign an iterable
```

The new items being assigned can come from any iterable object.

```python
>>> my_list = [2, 10, 12]
>>> my_list[0:1] = range(2, 10, 2)
>>>
>>> my_list
[2, 4, 6, 8, 10, 12]
```

Note that, if you assign a string to a slice, the string will be treated like a sequence of characters:

```python
>>> my_list = [2, 4, 6, 8, 10, 12]
>>> my_list[1:3] = "cat"
>>>
>>> my_list
[2, 'c', 'a', 't', 8, 10, 12]
```

If you want the string to be treated like an atomic object, you must create a list containing the string and assign that.

```python
>>> my_list = [2, 4, 6, 8, 10, 12]
>>> my_list[1:3] = ["cat"]
>>>
>>> my_list
[2, 'cat', 8, 10, 12]
```

If you want to replace a single element with a sequence of elements, you must specify the element as a slice:

```python
>>> my_list = [2, 6, 8, 10, 12]
>>> my_list[1:2] = [4, 6]
>>>
>>> my_list
[2, 4, 6, 8, 10, 12]
```

If you don't use a slice, then you'll replace the object at the specified index with the sequence object _as an atomic object_.

```python
>>> my_list = [2, 6, 8, 10, 12]
>>> my_list[1] = [4, 6]
>>>
>>> my_list
[2, [4, 6], 8, 10, 12]
```

When assigning to a slice, you aren't limited to consecutive elements. You can specify a slice with a step value other than 1:

```python
>>> my_list = [0,0,0,0,0,0]
>>> my_list[1:6:2] = [1,2,3]
>>>
>>> my_list
[0, 1, 0, 2, 0, 3]
```

Note, however, that the number of elements in the slice and the number of elements being assigned must be the same; otherwise, you'll get an error.

```python
>>> my_list = [0,0,0,0,0,0]
>>> my_list[1:6:2] = [1,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: attempt to assign sequence of size 2 to extended slice of size 3
```

### Adding to the end of a list

To add a single element at the end of a list, use the ```.append()``` method, passing the new object as the argument.

```python
>>> my_list.append(14)
>>>
>>> my_list
[2, 4, 6, 8, 10, 12, 14]
```

You can also create a new list with the additional object and concatenate that to the existing list.

```python
>>> my_list += [16]
>>>
>>> my_list
[2, 4, 6, 8, 10, 12, 14, 16]
```

This is less efficient, however, since it involves creating a new, temporary list object.

You can't add an item at the end by trying to assign a value at an index one past the last index: you'll get an out of range error.

```python
>>> my_list[len(my_list)] = 18
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
```

On the other hand, you can add to the end of the list by assign a new list to _a slice range_ starting at the end.

```python
>>> my_list[len(my_list):] = [18]
>>> my_list
[2, 4, 6, 8, 10, 12, 14, 16, 18]
```

This is equivalent to using the ```.extend()``` method, which is more readable:

```python
>>> my_list.extend([20, 22])
>>>
>>> my_list
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
```

The ```.extend()``` method can take any iterable object. For example:

```python
>>> my_list.extend(range(24, 28, 2))
>>>
>>> my_list
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
```

### Adding items at a specific position in the list

You can add a single item at any position in a list using the ```.insert()``` method. It requires two arguments: a position index, and the object to be inserted.

```python
>>> my_list = ["cat", "dog", "spam"]
>>> my_list.insert(2, "eggs")
>>>
>>> my_list
['cat', 'dog', 'eggs', 'spam']
```

Note that the item is inserted _before_ the item that was originally at that position.

The same operation can be achieved by assigning to a slice ```[i:i]``` for some index ```i```.

```python
>>> my_list = [2, 6, 8, 10]
>>> my_list[1:1] = [4]
>>>
>>> my_list
[2, 4, 6, 8, 10]
```

The ```.insert()``` method can only insert a single element. If you try passing in a sequence or iterable object, that will be inserted as an atomic element.

```python
>>> my_list = [2, 8, 10]
>>> my_list.insert(1, [4, 6])
>>>
>>> my_list
[2, [4, 6], 8, 10]
```

```python
>>> my_list = [2, 8, 10]
>>> my_list.insert(1, range(4,8,2))
>>> my_list
[2, range(4, 8, 2), 8, 10]
```

To insert multiple elements, assign a sequence to an ```[i:i]``` range.

```python
>>> my_list = [2, 8, 10]
>>> my_list[1:1] = [4, 6]
>>>
>>> my_list
[2, 4, 6, 8, 10]
```

Note that if the slice range has different start and stop values, you'll replace rather than insert.

```python
>>> my_list = [2, 8, 10]
>>> my_list[1:2] = [4, 6]
>>>
>>> my_list
[2, 4, 6, 10]
```

### Removing items

There are various ways to remove items from a list. First, you can use ```.pop()``` (without any argument) to remove the last item from the list.

```python
>>> my_list = ["bacon", "eggs", "toast"]
>>> my_list.pop()
'toast'
```

Note that the "popped" item is returned. (You can ignore the returned value, of course.)

To remove an item with a particular value, use the ```.remove()``` method.

```python
>>> my_list = [1, 42, 2, 3, 42, 4]
>>> my_list.remove(42)
>>>
>>> my_list
[1, 2, 3, 42, 4]
```

This removes the first object in the list with that value. Note that compares object _values_, not object _identity_. For example, let's assign objects with the same value to two different variables. We'll use ```id()``` to confirm they are distinct objects.

```python
>>> x = [1,2]
>>> y = [1,2]
>>> id(x)
52114344
>>> id(y)
52143048
```

Next, we'll create a list that includes these objects. And we'll use ```id()``` again to confirm that the objects in the list are the same as ```x``` and ```y```, but distinct from one another.

```python
>>> z = [1, x, 2, y, 3]
>>> z
[1, [1, 2], 2, [1, 2], 3]
>>>
>>> id(x)
52114344
>>> id(z[1])
52114344
>>>
>>> id(y)
52143048
>>> id(z[3])
52143048
```

Finally, we'll invoke the ```.remove()``` method, passing ```y``` as the argument. Note that object ```y``` comes later in the list than ```x```.

```python
>>> z.remove(y)
>>> z
[1, 2, [1, 2], 3]
```

Note that ```x``` was removed, not ```y```. We can use ```id()``` to confirm that the remaining object is, indeed, ```y```:

```python
>>> id(y)
52143048
>>> id(z[2])
52143048
```

So, ```.remove()``` removes the first item with the same value, not the identical object.

If the list doesn't contain any element with same value, an error will occur.

```python
>>> my_list = [1, 2, 3]
>>> my_list.remove(42)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

You can avoid an error by checking first whether the item is in the list.

```python
>>> my_list = [1, 2, 3]
>>> if 42 in my_list:
...     my_list.remove(42)
...
>>>
```

You can remove the item at a specific position by using ```.pop()``` with an index argument.

```python
>>> my_list = [1, 2, 3]
>>> my_list.pop(1)
2
```

As we saw earlier, the "popped" item is returned.

Note that assigning ```None``` at a position is not the same as removing the item at that position: ```None``` is an object, so assigning ```None``` is like assigning any other value.

```python
>>> my_list = [1, 2, 3]
>>> my_list[1] = None
>>>
>>> my_list
[1, None, 3]
>>> len(my_list)
3
```

You can also remove an item using the ```del``` statement with an index reference to the item to be removed.

```python
>>> my_list = [1, 2, 3]
>>> del my_list[1]
>>>
>>> my_list
[1, 3]
```

Whereas ```.pop()``` can only remove one item, you can remove multiple items with ```del``` by specifying a slice.

```python
>>> my_list = [1, 2, 3, 4, 5, 6, 7, 8]
>>> del my_list[1:5:2]
>>> my_list
[1, 3, 5, 6, 7, 8]
```

>Note: if you don't specify an index or range, ```del``` will delete the entire list.
>
>```python
>>>> my_list = [1, 2, 3]
>>>> del my_list
>>>> my_list
>Traceback (most recent call last):
>  File "<stdin>", line 1, in <module>
>NameError: name 'my_list' is not defined
>```

Finally, you can remove all items from a list using ```.clear()```.

```python
>>> my_list = [1, 2, 3]
>>> my_list.clear()
>>>
>>> my_list
[]
>>> len(my_list)
0
```

This is the same as using ```del``` for the range ```[:]``` (the entire list).

### Other list operations

Because a list is an ordered sequence, it can potentially be re-ordered. The ```.reverse()``` method will reverse the order of all items in the list.

```python
>>> my_list = [1, 2, 3, 4, 5]
>>> my_list.reverse()
>>>
>>> my_list
[5, 4, 3, 2, 1]
```

The ```.sort()``` method will sort items in the list.

```python
>>> my_list = [5, 42, 17, 6, 12]
>>> my_list.sort()
>>>
>>> my_list
[5, 6, 12, 17, 42]
```

>Note: The ```.sort()``` method is available for ```list```, but isn't available for all mutable sequence types.

You can sort in descending order by adding ```reverse=True``` as an argument.

```python
>>> my_list = [5, 42, 17, 6, 12]
>>> my_list.sort(reverse=True)
>>>
>>> my_list
[42, 17, 12, 6, 5]
```

>Note: the ```reverse``` argument must be specified using the ```reverse``` keyword.

The items in the ```.sort()``` examples have been numbers, but other types that support a ```<``` comparison can also be sorted.

```python
>>> my_list = ['juice', 'toast', 'spam', 'eggs']
>>> my_list.sort()
>>>
>>> my_list
['eggs', 'juice', 'spam', 'toast']
```

**Note:** As mentioned in [lesson 5](5_Bool_Comparisons.md#comparison-expressions), string comparison is complex. When using ```.sort()``` on a list of strings as in the previous example, sort will compare strings like comparing lists of the numeric values of Unicode code points. Thus, uppercase letters will sort differently than the corresponding lowercase letters.

```python
>>> my_list = ['juice', 'toast', 'Spam', 'eggs']
>>> my_list.sort()
>>> my_list
['Spam', 'eggs', 'juice', 'toast']
```

The ```.sort()``` method can take a ```key``` argument that is a single-parameter function that can provide a comparison key for each item. For example, the ```str``` type has a static method that does a lowercase mapping of the string; that can be used to fold case differences:

```python
>>> my_list.sort(key=str.lower)
>>> my_list
['eggs', 'juice', 'Spam', 'toast']
```

But, again, string comparison is complex, particularly when different languages are involved. Tread carefully!

Also note that ```.sort()``` can only work when ```<``` comparison works between all pairs of items in the list. If a list contains a mix of types, an error may be raised.

```python
>>> my_list = ['cat', 42, 17, 'abc']
>>> my_list.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
```

Even if all items in the list are of the same type, sort will not be supported if objects of that type can't be compared using ```<```. (For example, a list of dictionaries can't be sorted.)

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

In the previous lesson, we went over the traditional flow control statements ```if``` and ```while```. But we held off on discussing ```for``` because, in Python, the ```for``` statement and sequence types work closely together. There are still some other sequence types that we haven't yet covered, byte sequences; we'll get to those later. We've now got a solid start on sequences; the [next lesson](8_For.md) will introduce Python's ```for``` statements.
