# Booleans, Comparisons and Logical Expressions

Almost any program you create will need to have logic for program flow control, such as _branching_ (do certain things given one condition, but different things in other conditions). To get to that, we need to learn about comparison and logical expressions, and about another basic type, `bool`.

In this lesson, we'll go over all of those things. We'll introduce several additional operators used in comparison and logical expressions. We'll also explore use of the built-in object, `None`, that was introduced in the previous lesson, as well as a special built-in function, `isinstance()`, both of which are relevant for logical expressions.

In the previous lesson, we learned about the built-in function, `id()`, which returns an object’s ID. In this lesson, we’ll consider how to determine whether two things are the very same object.

Discussions of comparison operators for other languages often cover a _ternary_ operator construct that evaluates a condition and returns a value in a single statement. This isn't limited to boolean results and is more like a compact `if`...`else`. We'll cover that in the next lesson.

* [Booleans—the `bool` type](#booleans—the-bool-type)
* [Comparison expressions](#comparison-expressions)
* [Membership](#membership)
* [Logical expressions](#logical-expressions)
* [Chained comparisons](#chained-comparisons)
* [Identity comparison](#identity-comparison)
* [Comparison with `None`](#comparison-with-none)
* [`isinstance()`](#isinstance)
* [What's next](#whats-next)

## Booleans—the `bool` type

You're probably familiar with boolean values: _true_, or _false_. In Python, the `bool` type supports two such values, and there are special constant symbols to represent them: `True` and `False`. Let's look at these using the `type()` function.

```foo
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
```

Note that these constants must be written exactly as above, with an initial capital followed by lowercase letters. Any other spelling won't be recognized (unless you used it as a variable, say—not recommended, by the way).

Something to be aware of is that `bool` is a sub-class of `int`. So, `True` and `False` actually have integer values, 1 and 0 respectively. Sometimes, you might see 1 or 0 displayed as a result in a place where you expected to see `True` or `False`. If so, this is why. A side effect is that `True` and `False` will work as operands in numeric expressions as synonyms for 1 and 0. For example:

```foo
>>> 6 + True
7
>>> True + True
2
>>> 4 * False
0
>>> True - True
0
```

Probably not that useful, but something to be aware of.

What is more useful is to know that pretty much any object can be implicitly converted to a boolean if it's used in a place where a `bool` is expected, such as in a conditional expression in a flow control statement. (We'll come back to that in the next lesson.) For now, the thing to learn is that any object can be converted to a `bool`. The built-in `bool()` function can be used to do that explicitly. Let's explore some examples.

```foo
>>> bool(42)
True
>>> bool(3.14)
True
>>> bool(float('inf'))
True
>>> bool(float('nan'))
True
>>> bool("spam")
True
>>> bool('a')
True
```

Almost any object that has a value or length will convert to the value `True`. There are very few things that convert to `False`. From all the types we've covered so far, these are the only values that evaluate as `False`:

```foo
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool("")
False
```

We've mentioned that `str` is a sequence type. , and that there are other sequence and collection types. And we see above that the empty string converts to `False`. When we learn about those other types, the same will be true for them: an empty sequence or collection converts to `False`.)

That gets us started on `bool` values and the `bool()` function. Now we can begin looking at comparison operators and expressions.

## Comparison expressions

Python supports the typical set of numeric comparison operators:

|Operator|Meaning|Example expression|
|--------|-------|-------|
|`==`|equal                |`x == y`|
|`!=`|not equal            |`x != y`|
|`>` |greater than         |`x > y` |
|`<` |less than            |`x < y` |
|`>=`|greater than or equal|`x >= y`|
|`<=`|less than or equal   |`x <= y`|

Note the difference between the equal comparison operator, `==`, and the assignment operator, `=`. A common typing mistake is to enter a comparison expression using the assignment operator rather than the equal operator. If the left-hand operator is a variable, that’s a valid expression, but it’s not a comparison expression, and it can mess up the intended logic of your code!

Also note that "<>", which is used in some other languages as a comparison operator for not equal, is not used in Python.

Numeric comparison expressions evaluate to a `bool` value, `True` or `False`. Let's look at a few examples.

```foo
>>> x = 17  # assign a value
>>> x == 17
True
>>> x == (5 ** 2)
False
>>> x != (4 * 5)
True
>>> 26 > x
True
>>> 29 < x
False
```

These comparison operators can also be used with strings. For example:

```foo
>>> her_name == "Sally"
False
>>> her_name[3:5] == 'za'
True
>>> x != "spam"
True
```

>**Note:** Be aware that string comparison can be a very complex topic, especially when dealing with Unicode and international text. If you have a program that handles a limited, pre-determined set of string values that use only ASCII characters, you'll be fine using any of the comparison operators above. Beyond that, though, you should probably avoid writing your own string comparison logic unless you have a good understanding of the topic.)

In the examples above, we compared two objects of the same type. You can also compare objects of different types. If you compare two numbers, an `int` and a `float`, then those comparisons work as you'd expect.

```foo
>>> 42 == 42.0
True
```

We mentioned above that `bool` is a sub-class of `int` and that the values `True` and `False` have the integer values 1 and 0. So, comparison between numbers and these boolean values also work as expected (given that awareness).

```foo
>>> True == 1
True
```

Beyond that, however, comparisons across different types are very limited: in general, objects of different types are considered to have unequal values. For example:

```foo
>>> 42 == 'a'
False
>>> 42 != 'a'
True
```

And, in general, comparison between objects of different types using `>`, `<`, `>=` or `<=` aren't supported at all.

>Note: when you start defining your own custom classes, there is a way to make comparisons across types work using any of these operators. That's for a much later topic, though.

```foo
>>> 42 > 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'int' and 'str'
```

## Membership

We learned earlier that strings are sequences of characters, and so can contain multiple characters. In that sense, you can think of them as _like_ a set. So, a question that can arise is whether a particular character is contained in—is a member of—the string?

Python provides an operator that can be used to determine whether a character is contained in a string.

|Operator|Meaning|Example expression|
|--------|-------|-------|
|`in`|is contained in|`x in y`|

Here's an example:

```foo
>>> 'a' in "cat"
True
```

More generally, the `in` operator can be used with any container-like types to determine whether an object is contained in a container-like object. We'll cover more in later lessons. For now, we'll mention just one more way it can be used with strings: it can be used to tell of a string is a *substring* of another string. For example:

```foo
>>> "cat" in "scatter"
True
```

## Logical expressions

Logical expressions are comparisons between boolean values. Because `True` and `False` also have numeric values 1 and 0, we could handle logical expressions as numeric comparisons. For example, if we want to express _x equals 42 and y equals 3.14_ we could do that using the operators introduced above, plus some grouping with parentheses for clarity, as follows:

```foo
>>> ((x == 42) == (y == 3.14) == 1)
True
```

But that's pretty tedious and, worse, makes it harder to read and understand the intent.

Like most programming languages, Python provides boolean operators:

|Operator|Meaning|Example|
|--|--|--|
|`and`|`True` if both operands are `True`; otherwise, `False`|`x and y`|
|`or` |`True` if either operand is `True`; otherwise, `False`|`x or y`|
|`not`|the complement of the operand|`not x`|

Note that `not` is a unary operator—it only takes one operand. Complement means the opposite value (if `True`, then evaluate as `False`, and vice versa).

The way that expressions evaluate using these operators is probably familiar, so we won't provide complete "truth tables". Here's an example:

```foo
>>> False or not True
False
```

Of course, comparing boolean literals isn't particularly interesting. Better examples for using boolean operators involving comparing the results of comparison expressions, like the example at the start of this section:

```foo
>>> x == 42 and y == 3.14
True
```

In precedence order, the boolean operators have lower precedence than other comparison operators. So, in that example, the equality comparisons are evaluated first, and then the `and` comparison is evaluated.

Let's look at one more example:

```foo
>>> x != 17 and not her_name == "Erin"
True
```

The `not` operator takes precedence over `and` and `or`. Let’s restate the above adding parentheses to make clearer the precedence of operators and their operands:

```foo
>>> (x != 17) and (not(her_name == "Erin"))
True
```

Python doesn't have a built-in exclusive-or boolean operator. It's not commonly needed in logical expressions, but you can easily workaround it if needed:

```foo
>>> (x and not y) or (y and not x)
```


Now that we have a basic understanding of object IDs, let's look at identify comparison.

## Chained comparisons

In Python, you can combine multiple comparisons into a single expression. For example:

```foo
>>> 1 < 5 <= 12
True
```

The chained comparison expression in this example is equivalent to simple comparisons combined with a logical `and` operator:

```foo
>>> (1 < 5) and (5 <= 12)
True
```

Multiple comparison expressions can be chained together, with the operands on either side of a comparison operator compared. Each comparison is evaluated, and if any fails, then the chained comparison expression is false.

```foo
>>> 1 < 5 <= 5 != 12 < 17
True
```

The above examples used ordering comparison of numbers, but chained comparison expressions aren't limited to that. Other types of comparison can be used so long as each *<operand> <operator> <operand>* portion is a valid comparison. For example:

```foo
>>> "bar" != "foosball"[:3] in "foot"
True
```

## Identity comparison

So far, we've looked at comparison between values of objects, and combining simple comparison expressions into richer logical expressions. Most of the time when we’re comparing two things, we’re interested in comparing the values.

But sometimes we'll want to know if we're dealing with two references to _the same, identical object_. When that's the case, it's important to understand that comparing _values_ is not, in general, the same.

We were introduced to that distinction in the previous lesson: all objects have IDs, and two objects with the same value can have different IDs. We saw that illustrated for floats and strings. 

However, we also can't determine that two objects are identical simply by comparing their IDs. That's because two different objects could have the same ID if they are of different types.

For certain types, comparing values or IDs may be the same as comparing identify if values are _singletons_ within that type. We saw that for `int`s: each `int` value is a singleton. `None` is also a singleton. But objects of most types are not singletons, and in the general case, object identity is not the same as value or ID.

For identify comparison, Python provides identity operators:

|Operator|Meaning |Example |
|--------|--------|--------|
|`is`    |both operands are the same object |`x is y`    |
|`is not`|the operands are different objects|`x is not y`|

Let's look at an example:

```foo
>>> x = 6
>>> y = 6
>>> x is y
True
```

We can try doing identity comparison with a literal, but that's probably never useful, and in interactive mode the interpreter will give us a warning:

```foo
>>> x is 6
<stdin>:1: SyntaxWarning: "is" with a literal. Did you mean "=="?
True
```

Most of the time when you want to do identity comparison, you'll be comparing the objects referred to by two variables. For instance, you might define a function that takes two string arguments and (for whatever reason) need to know if whether or not arguments are identical string objects. Here's what that might look like:

```python
def my_func(string1, string2):
    if string1 is not string2:
        # do appropriate stuff
```

Earlier we saw "not" as a boolean operator. Note that "not", the boolean operator, and "not" in the `is not` identity comparison operator are not the same "not"! In many cases, the difference might not matter, but sometimes it can. Consider these examples:

```foo
>>> x = False
>>> x is not False # identity comparison operator is not
False
>>> x is (not False) # boolean operator
False
```

Since `False` has an integer value of 0, you might expect the same results if we assign 0 to x. However...

```foo
>>> x = 0
>>> x is not False # identity comparison operator
True
>>> x is (not False) # boolean operator
False
```

Confused yet?

It probably won't be often that you need to compare identity with things that evaluate to boolean values. But if you do, be careful in how you use "not"!

## Comparison with `None`

In the previous lesson, we were introduced to the special object `None` used to represent the idea of _nothing_. We learned that `None` is not the same as 0, or any other value. 

But `None` can be converted to a `bool`: `None` is one of the few things that converts to `False`.

```foo
>>> bool(None)
False
```

Since there are situations in which `None` may get assigned to a variable or returned from a function, we want a way to evaluate if that's the case. 

Here’s an example: A dictionary is a data structure that stores key-value pairs, and that allows you to look up a value by its key. (We’ll look at dictionaries in a future lesson.) 

```foo
>>> my_dict = {'Tucson': 2, 'Seattle': 20}
>>> my_dict.get('Tucson')
```

But if you try to look up an entry that isn't in the dictionary, the `.get()` method will return `None`.

```foo
>>> x = my_dict.get('Waterloo')
>>> x is None
True
```

Before you start acting on the object retrieved from the dictionary, you might want to check whether it is `None`.

We can do an identity comparison or an equality comparison—either will work:

```foo
>>> x = None
>>> x is None # identity comparison
True
>>> x == None # equality comparison
True
```

Earlier, we learned that objects can be implicitly converted to a boolean if used in a place where a `bool` is expected, such as a conditional expression. We can also let Python do an implicit conversion of `None` to `False`, though that isn't the same as testing if something is `None` since there are other things (not many, but some) that could also convert implicitly to `False`. If you need to check if something is `None`, it's best to do an explicit identity comparison using `is None` or `is not None`.

## `isinstance()`

Sometimes you might want to determine if a variable has a particular type. The built-in `isinstance()` function is designed to do just that. It's similar to `type()` in that it can be used to tell us about the type of an object or variable. But it takes two arguments, an object and a type, and returns `True` or `False`. That makes it handy for using in logical expressions.

Let's look at a few examples:

```foo
>>> isinstance("hi", str)
True
>>> x = "hi"
>>> isinstance(x, str)
True
>>> isinstance(x, int)
False
```

Note that the names of types are symbols, not strings. So you don't enclose them in quotation marks.

We saw that the `type()` function returns the type of an object; so we can use expressions using `type()` as the second argument to `instance()`:

```foo
>>> isinstance(6, type(42))
True
```

Of course, you won't ever need to check if an `int` literal is of the some type as another `int` literal. A more interesting example could involve comparing the types of variables:

```foo
>>> x = 42
>>> y = 3.14
>>> isinstance(x, type(y))
False
```

The second argument passed into `isinstance()` can be a single type or it can be a sequence of types (specifically, a _`tuple`_—we'll learn about that type a bit later). So, for example, we can check if a variable is an instance of any of the numeric types:

```foo
>>> x = 42
>>> isinstance(x, (int, float, complex))
True
>>> x = 3.14
>>> isinstance(x, (int, float, complex))
True
>>> x = 4-5j
>>> isinstance(x, (int, float, complex))
True
>>> x = "spam"
>>> isinstance(x, (int, float, complex))
False
```

A typical situation in which `isinstance()` can be useful is if you define a function that can take arguments of different types and you need to do different things depending on the type of the argument that was passed in. For example:

```python
def my_func(val):
    if isinstance(val, str):
        # do appropriate stuff
```

Finally, it was mentioned earler that `bool` is a sub-class of `int`. This means that a boolean value is both an instance of `bool` and also an instance of `int`.

```python
>>> isinstance(False,int)
True
>>> isinstance(False,bool)
True
```

This will apply to any other situations in which a type is defined as a sub-class of another type.


## What's next

In this lesson, we've started to introduce some examples that look ahead to new topics, such as custom functions and flow control logic. There's more to learn about the things we've introduced so far—numbers, variables and what not. But let's go for a bit more breadth before more depth. So, the [next lesson](6_Intro_Functions_Flow_Control.md) will get us started on defining functions and will introduce statements for flow control.
