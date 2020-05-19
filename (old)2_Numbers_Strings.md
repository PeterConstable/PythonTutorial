# Intro to Basic Types: Numbers and Strings

Python has several built-in types. We'll start by looking at numeric types and strings, and basic operations on those types. We'll also

Python also has several built-in functions. We'll introduce a few of these that are especially relevant for numbers and strings, as well as the ```type()``` function that will help us understand types in Python.

We'll end with a brief look at one of the deeper aspects of Python related to objects and types.

## A quick intro to ```type()```

Everything in Python is an object with a class type. (Really, _everything!_) The built-in ```type()``` function returns the type of whatever it is that gets passed to it.

```foo
>>> type(6)
<class 'int'>
```

We'll use the ```type()``` function to understand the basic types and results from different operators as well as some aspects of how variables are handled.

## Numeric types

Python has built-in types for three basic kinds of numbers: ```int``` (integers), ```float```, and ```complex```. Let's start with integers.

### The integer type—```Int```

Integer literals are written without any decimal. The "-" prefix indicates negative values; a "+" prefix is optional.

```foo
>>> -6
-6
>>> +6
6
```

We can use the built-in ```type()``` function to see the type of our integer literal:

```foo
>>> type(6)
<class 'int'>
```

Numeric values can be in the form of literals or numeric expressions that get evaluated to a numeric type. For example:

```foo
>>> 4 + 2
6
```

Functions that can take numbers as values can also take numeric expressions. The expression will first be evaluated and then passed as the argument to the function.

```foo
>>> print(4 + 2)
6
```

Integer literals can be written in hexadecimal as well as in decimal. For hexadecimal, use the "0x" prefix; digits A through F can be entered in upper or lower case.

```foo
>>> 0x30
48
>>> 0xaF
175
```

Integer literals can also be written in binary, using the "0b" prefix, or as octal using the "0o" prefix.

```foo
>>> 0b110010
50
>>> 0o234
156
```

To get integers presented as hex or binary strings, use the built-in ```hex()```, ```bin()``` or ```oct()``` functions.

```foo
>>> hex(142)
'0x8e'
```

```foo
>>> bin(142)
'0b10001110'
```

```foo
>>> oct(142)
'0o216'
```

Note that these functions return strings, not integers!

```foo
>>> type(hex(42))
<class 'str'>
```

The usual basic arithmetic operators for addition, subtraction and multiplication are supported and return another integer:

```foo
>>> 4 + 2
6
>>> 4 - 2
2
>>> 4 * 2
8
>>> type(4*2)
<class 'int'>
```

The division operator, however, always returns a float:

```foo
>>> 4 / 2 # normal division, returns a float
2.0
```

```foo
>>> type(4/2)
<class 'float'>
```

To do integer division—that is, division that returns an integer (and discards any fractional portion)—use the ```//``` operator:

```foo
>>> 5/3  # normal division returns a float
1.6666666666666667
>>>
>>> 5//3  # integer division returns an int
1
```

Note that this is _floor_ division: the result is always rounded down toward negative infinity.

```foo
>>> -5//3
-2
```

To get an integer remainder from division, the modulo operator is ```%```.

```foo
>>> 5 % 3
2
```

Python also supports an exponentiation operator, ```**```.

```foo
>>> 2 ** 8
256
```

There's also a built-in function that can be used for exponentiation, ```pow()```. When used with integer arguments, it returns an integer.

```foo
>>> pow(2, 8)
256
```

One other built-in function for numeric operations is ```abs()```, which returns the absolute value of a number.

```foo
>>> abs(-4 * 3)
12
```

In Python, integers are not limited to a particular range or machine representation. For example:

```foo
>>> 1000000000000000000000000000000000000000000000000000000000000000 - 1
999999999999999999999999999999999999999999999999999999999999999
>>>
>>> -888888888888888888888888888888888888888888888888888888888888888 + 2
-888888888888888888888888888888888888888888888888888888888888886
```

For really long numbers, an infix "\_" can be used as a grouping delimiter.

```foo
>>> 0xFFFF_FFFF
4294967295
>>>
>>> 1_848_947_235_632
1848947235632
```

Note that "\_" must be an infix and can't occur at the start or end of an integer literal; that would result in an error. The Python interpreter will ignore any infixed "\_", so any size grouping can be used. Be sure to stick to conventional groupings so that you don't get confused later.

```foo
>>> 0xffff_fff # not 4G!
268435455
```

### The real type—```float```

Floats are used for fractional values. (In math, real numbers: integer, rational or irrational.) When a numeric literal includes a decimal point, ".", it is interpreted as a float, even if no fractional portion is entered.

```foo
>>> type(6.)
<class 'float'>
```

When a float result is returned in interactive mode, at least one decimal place will be shown.

```foo
>>> 6.
6.0
```

The presence of the decimal point and at least one decimal digit makes clear that the result is a float, not an integer.

Unlike integers, the float type has limited precision. The actual limitation will depend on the specific Python interpreter you're using and the architecture of the machine you're running on. You can enter a float literal with any number of decimal places, but the value will be limited by the precision limitation.

```foo
>>> 1.2222222222222222222222222222222
1.2222222222222223
```

An issue to be aware of whenever float types are involved is that rounding errors can get introduced by operations. We'll see that very shortly.

As mentioned above, the division operator always returns a float. If a numeric expression using ```+```, ```-```, ```*``` or ```**``` has a float as one of the operands, the result will be a float.

```foo
>>> 4. + 2
6.0
>>> 4. - 2
2.0
>>> 4. * 2
8.0
>>> 4. ** 2
16.0
```

Note that the exponentiation operator accepts a float as the exponent operand.

```foo
>>> 4 ** .5
2.0
```

The integer division operator also accepts float operands and return a whole-integer result, but as a float.

```foo
>>> 5.3 // 2
2.0
```

Similarly, the modulo operator accepts float operands and will return a float. When non-integral values are used, though, some rounding errors may be introduced.

```foo
>>> 5.3 % 2  # expecting 1.3
1.2999999999999998
```

```foo
>>> 11 % 2.2  # 11 = 2.2 * 5, so remainder should be 0?
2.1999999999999993
```

The ```abs()``` and ```pow()``` functions were introduced earlier. These can also be used with float arguments, in which case a float will be returned.

```foo
>>> abs(-2.)
2.0
>>> pow(2., 8)
256.0
>>> pow(2, 3.)
8.0
>>> pow(9, .5)
3.0
```

Note in that last example that a fractional exponent argument can be used to get the square or nth root of a number. But also note that rounding precision errors can occur.

```foo
>>> pow(27, 1/3)
3.0
>>> pow(64, 1/3)  # expected: 4
3.9999999999999996
```

The exponentiation operator ```**``` can also be used to calculate square roots, as seen earlier; let's repeat that example:

```foo
>>> 4 ** .5
2.0
```

You can use try using a composite expressions to get an nth root. Let's give it a shot:

```foo
>>> 27 ** 1/3  # cube root is 3?
9.0
```

What happened? If you guessed that there's an issue with order of operations, you're right: exponentiation has higher precedence than division. So, ```27 ** 1``` was evaluated first, and then that result was divided by 3. Parentheses can be used in complex numeric expressions to ensure a desired order of operations.

```foo
>>> 27 ** (1/(8-5))
3.0
```

Up to now, we've seen examples of floats represented using a decimal point. There is another representation that's also used for float literals, the exponent form:

```foo
>>> 2.34e5
234000.0
```

The number after "e" is an exponent applied to a base of 10, and that is multiplied times the number before "e". For very large float values, results in interactive mode will use the exponent representation with a single-digit mantissa.

```foo
>>> 1234567890123456789.
1.2345678901234568e+18
```

### The ```complex``` type

Complex values have real and imaginary components. In complex literals, the imaginary component is represented using a suffix "j" or "J"; for example, "4+2j".

```foo
>>> 4+2j
(4+2j)
>>> type(4+2j)
<class 'complex'>
```

Note that the imaginary component must always have a decimal digit before the "j" suffix, even for imaginary unit of 1. The real component is optional.

```foo
>>> 4+2j * 3J
(-2+0j)
```

Numeric expressions that include a complex operand as well as numeric functions with complex arguments will generally return a complex value. For example:

```foo
>>> pow(1j, 2)
(-1+0j)
```

One notable exception is the ```abs()``` function: when a complex number is passed as an argument, it returns the _magnitude_ as a float.

```foo
>>> abs(1j)
1.0
```

### Using constructors ```int()```, ```float()```, ```complex()```

You can convert numeric values between ```int``` and ```float``` by using the built-in ```int()``` and ```float()``` constructor functions.

```foo
>>> float(2)
2.0
>>> int(2.0)
2
```

> Note: when coverting from ```float``` to ```int```, the float is truncated, not rounded.
>
> ```foo
> >>> int(2.6)
> 2
> >>> int(-2.3)
> -2
> >>> int(-2.6)
> -2
> ```

Integer and float values can be converted to complex using the ```complex()``` constructor function.

```foo
>>> complex(2)
(2+0j)
>>> complex(4.3)
(4.3+0j)
```

However, complex values cannot be converted to integer or float.

```foo
>>> float(4+2j)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't convert complex to float
```

### More details on numeric types

For more details on numeric types, see the relevant Python documentation, [Numeric Types — int, float, complex](https://docs.python.org/3.8/library/stdtypes.html#typesnumeric). For precedence order of operators, see [6.17 Operator precedence](https://docs.python.org/3.8/reference/expressions.html#operator-summary).

## Strings—the ```str``` type

String literals are enclosed in double or single quotation marks ("..." or '...').

```foo
>>> "spam and eggs"
'spam and eggs'
>>> type(_)
<class 'str'>
```

When a string result is returned in the console, it will be enclosed in quotation marks. But results from the ```print()``` function, which are strings, are not enclosed in quotes.

```foo
>>> print("eggs and spam")
eggs and spam
```

When a string is enclosed in double quotes, single quote marks are interpreted as characters within the string. Similarly, if the string is enclosed in single quotes, a double quote mark is interpreted as part of the string.

```foo
>>> "spam and 'eggs'"
"spam and 'eggs'"
```

```foo
>>> 'eggs and "spam"'
'eggs and "spam"'
```

To include a double or single quote within a string that's enclosed in the same kind of quote mark, the characters can be represented using an escape sequence, with a "\" prefix.

```foo
>>> "spam and "spam""
  File "<stdin>", line 1
    "spam and "spam""
               ^
SyntaxError: invalid syntax
```

```foo
>>> "spam and \"spam\""
'spam and "spam"'
```

Multi-line string literals are also supported. These are entered by enclosing inside three double quote marks before and after, """...""".

```foo
>>> """eggs
... and
... spam"""
'eggs\nand\nspam'
```

>Note the multi-line prompt, "...", indicating that the interpreter is awaiting additional lines to complete the statement.

The evaluated result is presented on a single line, with the new-line shown as an escape sequence, "\n". But if a multi-line string is passed to the ```print()``` function, the output will be displayed on multiple lines, without escape sequences.

```foo
>>> print("""spam
... and
... eggs""")
spam
and
eggs
```

A multi-line string can also be entered in a single line using double or single quotes with the new-line escape sequence. When

```foo
>>> print("cats\nand dogs")
cats
and dogs
```

### String concatenation

Strings can easily be concatenated. For string literals, then can simply be listed in a line with nothing or only whitespace in between.

```foo
>>> "a" "b"
'ab'
```

```foo
>>> "c""de"
'cde'
```

```foo
>>> "a" "b"
'ab'
```

```foo
>>> "c"'d'
'cd'
```

```foo
>>> 'efg'    'hij'
'efghij'
```

As expected, the strings are concatenated without any whitespace added. This is different from what happens in the ```print()``` function if multiple string arguments are passed: ```print()``` always separates the items with a space.

```foo
>>> "spam" "and" "eggs"
'spamandeggs'
>>> print("spam", "and", "eggs")
spam and eggs
```

String can also be concatenated by using the ```+``` operator. (For string variables, this will be required to concatenate.)

```foo
>>> "humming" + "bird"
'hummingbird'
```

The ```\*``` operator can also be used with strings to concatenate multiple instances of a string. The way to do this is to write an expression of the form _n_ * _str_, where _n_ is an integer. For example:

```foo
>>> 4 * "really " + "long"
'really really really really long'
```

>Note that the number must be the first operand, with the string as the second operand. The other way around will produce an error.

### Strings as Unicode character sequences

Strings in Python 3.x are sequences of Unicode characters. String literals can include any Unicode character, if supported by the console or editor you're using. But even if they're not supported by the console or editor, any Unicode character can be written in a string literal as an escape sequence with the prefix "\u" or "\U".

```foo
>>> "convert to \u20ac"
'convert to €'
```

Note that the "\\u" prefix is used for Unicode characters from U+0000 to U+FFFF, and exactly four hex digits must be provided: \\uxxxx. The "\\U" prefix can be used for any Unicode characters from U+0000 to U+10FFFF, and exactly eight hex digits must be provided: \\Uxxxxxxxx.

```foo
>>> '\U0001f603'
'😃'
```

The built-in ```ord()``` function can take any single Unicode character and return its numeric code point (as an ```int```).

```foo
>>> ord('€')
8364
```

>Note that the returned number is presented in decimal, even though Unicode code points are normally cited in hex. You can use the built-in ```hex()``` function to get a hex representation (returned as a ```str```):
>
>```foo
>>>> hex(ord('€'))
>'0x20ac'
>```

The built-in ```chr()``` function is the inverse of ```ord()```: it takes a number and returns a string with the Unicode character for that code point.

```foo
>>> chr(8364)
'€'
```

>Note: The ```ord()``` function only takes a single character, not a sequence of multiple characters. Similarly, the ```chr()``` function only takes a single numeric value.

Now, we mentioned that strings are _sequences_ of characters. Sequence-type objects support a number of operations, such as ability to index elements within the sequence or to get slices (sub-ranges) from the sequence. These operations are supported for strings as well. We won't go into a lot of detail on sequence operations just yet; the following examples introduce the general idea:

```foo
>>> "cats and dogs"[2]  # get the character at index 2
't'
>>> "cats and dogs"[5:8]  # get the slice from index 5 to index 8
'and'
```

### Converting numeric types to string using the ```str()``` constructor

Python does not support implicit conversion of numbers to strings. For example, the following attempt to concatenate produces an error.

```foo
>>> "How many eggs? " + 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

It's easy to work around this: you just need to remember to convert numbers to strings using the built-in ```str()``` constructor function.

```foo
>>> "How many eggs? " + str(4)
'How many eggs? 4'
```

When using the ```print()``` function, there are other ways to integrate numbers into a string using string-formatting operations. We'll save that for a later topic.

## A little more insight on objects and types from ```type()```

We'll end this introduction to basic types to peek a bit "under the hood" into objects and types in Python. As mentioned earlier, _everything_ in Python is an object with some class type. (It's objects all the way down!) We can use the ```type()``` function to expose a bit more of this.

On screen, we see the result of the ```type()``` function as a string but, in fact, the ```type()``` function returns an object of another type. We can use the interactive mode "\_" variable to help see that:

```foo
>>> type(6)
<class 'int'>
>>> type(_)
<class 'type'>
```

Even built-in functions are objects that have their own type:

```foo
>>> type(print)
<class 'builtin_function_or_method'>
```

## Review

In this topic, we introduced the following basic types and their corresponding constructor functions:

* ```int```, ```int()```
* ```float```, ```float()```
* ```complex```, ```complex()```
* ```str```, ```str()```

We also went over the basic numeric operators:

* ```+```: addition
* ```-```: subtraction
* ```*```: multiplication
* ```/```: real division
* ```//```: integer division
* ```%```: modulo (remainder)
* ```**```: exponentiation

String concatenation operators were introduced:

* ```+```: concatenate two strings
* ```*```: concatenate _n_ instances of a string

We touched on multi-line strings and certain escape sequences, and on certain differences between how results from evaluating string expressions are shown versus results from the ```print()``` function.

And we also introduced the these other built-in functions:

* ```abs()```: returns the absolute value of a number
* ```pow()```: returns the exponentiation result from two numbers
* ```bin()```: returns the binary string representation of a number
* ```hex()```: returns the hexadecimal string representation of a number
* ```oct()```: returns the octal string representation of a number
* ```ord()```: return the Unicode code point for a single character
* ```chr()```: return the Unicode character for a code point number
* ```type()```: return the type of any object
