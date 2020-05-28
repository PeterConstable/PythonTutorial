# Sets and Dictionaries

In earlier lessons we learned about various sequence types: ```str``` (in [lesson 3](3_Intro_Strings.md)), ```list``` and ```tuple``` (in [lesson 7](7_List_Tuple_Range.md). Sequence types are all ordered containers: they contain zero or more member elements, and the elements are in some particular order. Strings are specialized containers: they can only contain characters. But list and tuple are general containers: they can contain objects of any type.

In this lesson, we will learn about Python's other built-in, general-purpose container types: ```set```, ```frozenset``` and ```dict```.

* [Overview: sets and frozen sets, lists and tuples](#overview-sets-and-frozen-sets-lists-and-tuples)
* [Working with sets and frozen sets](#working-with-sets-and-frozen-sets)
* [](#)
* [](#)
* [](#)

## Overview: sets and frozen sets, lists and tuples

The ```set``` and ```frozenset``` types are similar to ```list``` and ```tuple```, the main difference being that the lists and tuples are ordered (sequences) while sets and frozen sets are not ordered. Taking order and mutability as binary attributes, these four types provide all four possibilities:

|           | ordered      | un-ordered      |
|----------:|:-------------|:----------------|
|   mutable |  ```list```  | ```set```       |
| immutable |  ```tuple``` | ```frozenset``` |

Because they are sequences, lists and tuples are able to contain multiple elements that have the same values. For example,

```python
>>> x = list([2,3,2,4])
>>> x
[2, 3, 2, 4]
>>>
>>> x = tuple((2,3,2,4))
>>> x
(2, 3, 2, 4)
```

In contrast, because sets and frozen sets are not ordered, they cannot contain duplicates: every contained element has a different value.

```python
>>> x = set([2,3,2,4])
>>> x
{2, 3, 4}
>>> len(x)
3
>>>
>>> x = frozenset([2,3,2,4])
>>> x
frozenset({2, 3, 4})
>>> len(x)
3
```

> Note: when defining a set, if you include two distinct objects that have the same value, only the first will be included. However, membership is evaluated by object value, not object identity.

The fact that sets and frozen sets cannot contain duplicates has an additional consequence: they can contain all objects of some types, but not others. For example, a set can contain tuple or frozen set objects, but not list or set objects.

>The reason for this limitation has to do with hashes and mutability. Sets require member objects to have a hash that is derived from the value in an idempotent manner (a given value always results in the same hash), and that is constant for the life of the object. Tuples and frozen sets have such hash values. But because lists and sets are mutable, they cannot have such hash values.

Sets and frozen sets support operations available for lists and tuples that do not involve order of elements:

* ```len()```
* membership; for example, ```x in my_set```
* use in arithmetic functions, ```sum()```, ```min()```, ```max()```

Also, while sets and frozen sets are not ordered, they are iterables: they can be used in contexts that require a sequence to be produced. For example, ```for x in my_set```. (Note that the order of elements in the sequence may not be predictable, however.)

But sets and frozen sets do not support sequence operations that pertain to having an order:

* element reference by index
* slices
* concatenation
* finding elements using ```.index()```
* ```.count()``` (this assumes there can duplicates)

While concatenation isn't supported, since that involves an order, there are ways to combine sets together, as will be described below.

## Working with sets and frozen sets

You can create a set by listing members enclosed in ```{...}```.

```python
>>> x = {2, 3, 4, 2}
>>> x
{2, 3, 4}
```

You can also create a set using the ```set()``` constructor function and passing any iterable object as an argument.

```python
>>> x = set([2, 3, 4, 2])
>>> x
{2, 3, 4}
```

```python
>>> x = set(range(4))
>>> x
{0, 1, 2, 3}
```

As mentioned earlier, the elements to be included in the set cannot be mutable objects, like lists or sets.

To create an empty set, you must use the ```set()``` constructor function with no argument.

```python
>>> x = set()
>>> x
set()
```

Note: the brace notation, ```{...}``` is also used for ```dict```. Empty braces, ```{}```, always indicate an empty dictionary. For this reason, an empty set is always represented as ```set()```.

A frozen set must be created using the ```frozenset()``` constructor function with an iterable argument.

```python
>>> x = frozenset([2, 3, 4, 2])
>>> x
frozenset({2, 3, 4})
```

```python
>>> x = frozenset(range(4))
>>> x
frozenset({0, 1, 2, 3})
```

To distinguish from ```set```, frozen sets are always represented using ```frozenset(...)```.

You can create an empty frozen set by calling the constructor function with no argument. Frozen sets being immutable, though, an empty frozen set is not very useful.

### Set-like ```set``` operations

Various set operations are taught in mathematics: union, intersection, etc. Python has these operations for the ```set``` type. 

Some of these operations use the same operator symbols used for bitwise operations on integers. There is analogy here. For example, _bitwise or_ ```|``` returns a bit value 1 if that bit is set in either operand. Similarly ```|``` as a _set union_ operator returns an element if it is contained in either operand set.

The following set operators are available. For each operator, there is an equivalent method that's also available.

| Operator | Meaning              | Example     | Equivalent method     |
|----------|----------------------|-------------|-----------------------|
| ```|```  | union of sets        | ```x | y``` | ```.union()```        |
| ```&```  | intersection of sets | ```x & y``` | ```.intersection()``` |
| ```-```  | difference           | ```x - y``` | ```.difference()```   |
| ```^```  | symmetric difference | ```x ^ y``` | ```.symmetric_difference()``` |

Each of these operators creates a new set. The operators accept only ```set``` operands, while the corresponding methods work with any iterables.

There are also set comparison operators that return ```True``` or ```False```.

| Operator | Meaning            | Example      | Equivalent method   |
|----------|--------------------|--------------|---------------------|
| ```<=``` | is subset          | ```x <= y``` | ```.issubset()```   |
| ```<```  | is proper subset   | ```x < y```  |                     |
| ```>=``` | is superset        | ```x >= y``` | ```.issuperset()``` |
| ```>```  | is proper superset | ```x > y```  |                     |
|          | is disjoint        |              | ```.isdisjoint()``` |

We'll explore each of these operations in detail.

#### Union, intersection, difference

The union operator ```|``` requires set operands. A union expression can have two operands, or can be chained with additional operands.

```python
>>> x = {1, 2, 3}
>>> y = {11, 12, 13}
>>>
>>> x | y
{1, 2, 3, 11, 12, 13}
>>>
>>> x | y | {22, 23, 24} | {42}
{1, 2, 3, 42, 11, 12, 13, 22, 23, 24}
```

(Note in the last result that sets are not ordered!)

The ```.union()``` method on a set object can take one or more arguments. The arguments can be a set or any iterable.

```python
>>> x.union(y, {22, 23}, [42, 43], range(51, 54), 'abc')
{1, 2, 3, 11, 12, 13, 'a', 22, 23, 'b', 42, 43, 51, 52, 53, 'c'}
```

Note in that result that a string as an iterable returns it member characters sequentially as separate items. If you want a string to be kept atomic, contain it within a list, tuple or set. The same applies to any iterable type: to be included as a unit, it must be wrapped in an iterable container.

```python
>>> y = (41, 42)
>>>
>>> x.union(y)
{1, 2, 3, 41, 42}
>>>
>>> x.union({y})
{1, 2, 3, (41, 42)}
```

The intersection operator ```&``` requires set operands. An intersection expression can have two operands, or can be chained with additional operands. The resulting set contains only elements that were contained in all of the operand sets.

```python
>>> set(range(1,10)) & {2, 4, 7, 3} & {5, 7, 6, 2}
{2, 7}
```

The ```.intersection()``` method on a set object can take one or more iterable arguments.

```python
>>> set(range(1,10)).intersection(range(3,8), {2, 6, 7}, [7, 8])
{7}
```

The set difference operator ```-``` requires set operands. A difference expression can have two operands, or can be chained with additional operands. The left-most operand is the reference set, and any items in the other sets are excluded from the result set.

```python
>>> set(range(1, 10)) - {2, 4, 5} - {2, 7, 3}
{8, 1, 6, 9}
```

The ```.difference()``` method on a set object can take one or more iterable arguments. The set object is the reference set; the result set contains items in that set that are not contained in any of the argument sets.

```python
>>> set(range(1,10)).difference({2, 4, 5}, (2, 3), range(4, 7))
{1, 7, 8, 9}
```

The symmetric difference operator ```^``` takes exactly two set operands. The result set includes items contained in one operand or the other, but not in both.

```python
>>> {1, 2, 8, 9} ^ {7, 8, 1, 3, 2}
{3, 7, 9}
```

The ```.symmetric_difference()``` operator takes one iterable argument. The result set includes items in the object set or in the operand but not in both.

```python
>>> x = {1, 2, 8, 9}
>>> x.symmetric_difference(range(2, 10))
{1, 3, 4, 5, 6, 7}
```

### Set comparison operations

### Mutating set operations

There are ```set``` operations for adding and removing items that are similar to some of the [```list``` operations](7_List_Tuple_Range.md#mutating-list-operations), though they are not the same.

| ```set``` operation | Similar ```list``` operations | Comment |
|--|--|--|
| ```.add()``` | ```.append()```, ```insert()``` | Because lists are ordered, items must be added at some particular position |
| ```.update()``` | ```.extend()``` ||
| ```.pop()``` | ```.pop()``` | ```list.pop()``` removes an item from the end of the list; ```set.pop()``` removes an arbitrary item |
| ```.remove()``` | ```.remove()``` | |
| ```.discard()``` || Similar to ```.remove()```, but no error if item is not contained. ```list``` has no similar method. |
| ```.clear()``` | ```.clear()``` ||
|```.copy()``` | ```.copy()``` ||


