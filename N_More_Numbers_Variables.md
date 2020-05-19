# More about Numbers and Variable Assignment

In lesson 2, we introduced the basics of working with numbers, expressions and variables: how to express numbers as literals, assign them to variables, and create numeric expressions using various operators. And in lesson 3 we got introduced to strings. In this lesson, we'll go into more detail into each of these areas:

* [Variable assignment and compound assignment operators](#variable-assignment-and-compound-assignment-operators)
* [Range and precision of ```int``` and ```float```](#range-and-precision-of-```int```-and-```float```)
* [Different formats for numeric literals](#different-formats-for-numeric-literals)
* [Strings as Unicode character sequences](#strings-as-unicode-character-sequences)
* [Converting between number and string types](#converting-between-number-and-string-types)

## Variable assignment and compound assigment operators

We've already seen the familiar assignment operator, ```=```, for assigning values to variables.

```foo
>>> x = 42
>>> y = "hey, there!"
```

Like several other languages, Python supports compound (or _in-place_) assigment operators that evaluate an expression and assign the result. For example:

```foo
>>> x = 6
>>> x += 5
>>> print(x)
11
```

In the second statement, ```+=``` is used to combine two steps into one. First, the expression ```x + 5``` is evaluated; then, the result is assigned back to ```x```. It's convenient shorthand for ```x = x + 5```.

The other numeric operators also have corresponding compount assignment operators. Follow along this sequence of statements:

```foo
>>> x = 4
>>> x -= 1
>>> x
3
>>> x *= 2
>>> x
6
>>> x **= 2
>>> x
36
>>> x //= 4
>>> x
9
>>> x %= 5
>>> x
4
>>> x /= 2
>>> x
2.0
```

>Note: some languages support ```=+``` and ```=-``` as well as ```+=``` and ```-=```, with slightly different effects in loop conditions. In Python, ```=+``` and ```=-``` are meaningul, but they're not compound assignment operators! They're simply the assignment operator ```=``` with the following ```+``` and ```-``` interpreted as prefixes to the following number. For example,
>
>```foo
>>>> x =- 5
>```
>
>means exactly the same thing as
>
>```foo
>>>> x = -5

With strings, ```+=``` can be used as a compound concatenation-assignment operator.

```foo
>>> x = "boo"
>>> x += "hoo"
>>> x
'boohoo'
```

## Range and precision of ```int``` and ```float```

In Python, ```int```s are not limited to a particular range or machine representation. For example:

```foo
>>> 1000000000000000000000000000000000000000000000000000000000000000 - 1
999999999999999999999999999999999999999999999999999999999999999
>>>
>>> -888888888888888888888888888888888888888888888888888888888888888 + 2
-888888888888888888888888888888888888888888888888888888888888886
```

The ```float``` type, however, however, has limited precision. The actual limitation will depend on the specific Python interpreter you're using and the architecture of the machine you're running on. You can enter a float literal with any number of decimal places, but the value will be constrained by the precision limitation of your setup.

```foo
>>> 1.2222222222222222222222222222222
1.2222222222222223
```

Because of the precision limitation, rounding errors will occur, especially with certain numeric operations. We already saw some examples of this in lesson2.

```foo
>>> 11 % 2.2  # 11 = 2.2 * 5, so remainder should be 0?
2.1999999999999993
```

```foo
>>> 64 ** (1/3)  # cube root of 64 is 4
3.9999999999999996
```

>To learn more about precision of ```float``` and how to find out details for your system, see the Python documentation for [sys.float_info](https://docs.python.org/3.8/library/sys.html#sys.float_info).

The ```float``` type in Python supports values for positive and negative infinity. These are obtained passing certain strings to the ```float()``` function:

```foo
>>> x = float('inf')
>>> x
inf
>>> y = float('-infinity')
>>> y
-inf
```

Either the short or long strings, 'inf' or 'infinity' can be used. Also, case doesn't matter.

```foo
>>> y = float('-inFiNitY')
>>> y
-inf
```

Or course, most numeric calculations involving infinity result in infinity.

```foo
>>> y / 2
-inf
```

There are a few exceptions, but they involve another special ```float``` value, ```nan```, meaning _not a (well-defined) number_. So, for example:

```foo
>>> x + y
nan
>>> x * 0
nan
>>> x / y
nan
```

Because ```int```s aren't bounded, these concepts don't apply. (Happy counting, Buzz Lightyear; let us know when you're done.)

## Different formats for numeric literals

So far, we've only dealt with numeric literals using decimal representations. But integer literals can also be expressed in hexadecimal, binary or octal. (Results in interactive mode will be shown in decimal, however.)

For hex, use the "0x" prefix followed by any number of digits; digits A through F can be entered in upper or lower case:

```foo
>>> 0x30
48
>>> 0xaF
175
```

To write literals in binary, use the "0b" prefix. For octal, use the "0o" prefix.

```foo
>>> 0b110010
50
>>> 0o234
156
```

Expressions using numeric operators can take literal operands expressed in any of these forms:

```foo
>>> 0xc1 * 0b11010010
40530
```

If you want to see integer values exprssed as hex, binary or octal strings, you can use the built-in ```hex()```, ```bin()``` or ```oct()``` functions.

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

In the previous section, we saw that ```int`` values are unbounded, so it's possible to work with some really long number literals. (And if you need to write numbers as binary, those can quickly get long as well.) In daily life, we use grouping delimiters to make it clearer what the value is. For instance

4,294,967,296

is much easier to read than

4294967296

When writing long number literals in Python, an infix "\_" can be used as a grouping delimiter.

```foo
>>> 0xFFFF_FFFF
4294967295
>>>
>>> 1_848_947_235_632
1848947235632
```

Note that "\_" must be an infix and can't occur at the start or end of an integer literal; that would result in an error. The Python interpreter will ignore any infixed "\_", so any size grouping can be used. Be sure to stick to conventional groupings so that you don't get confused later:

```foo
>>> 0xffff_fff # not 4G!
268435455
```

For decimal digits, stick to groupings of three. (Some cultures use other sized groupings, but three is universally familiar.), For hex, use groupings of four or eight; and use eight for binary.

We've been talking about ```int``` literals. What about ```floats```? Hex, binary or octal representations are not supported for ```float```s. You can use the "\_" grouping delimiter, however.

```foo
>>> x = 87_234_786.29
>>> x
87234786.29
```

## Strings as Unicode character sequences

## Converting between number and string types

In lesson 2, we learned about two basic numeric types, ```int``` and ```float```. We also saw that numeric expressions that have a ```float``` as one of the operands always result in a ```float```. But sometimes, you may need to get an ```int``` variable for a subsequent step. Each of the basic built-in types has a corresponding constructor function that can be used to convert between types.

The following examples show an ```int``` literal being converted to a ```float``` value using the ```float()``` constructor fuction; and ```float``` being converted to ```int``` using the ```int()``` constructor function:

```foo
>>> float(2)  # converts int to float
2.0
>>> int(2.0)  # converts float to int
2
```

Note that ```int()``` truncates the ```float``` value:

```foo
>>> int(4.2)
4
>>> int(4.8)
4
>>> int(-4.2)
-4
>>> int(-4.8)
-4
```

When working with strings, we may want to concatenate a number into a string. But Python doesn't allow an ```int``` or ```float``` to be concatenated onto a string.

```foo
>>> x = 42
>>> "final count: " + x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

But we can use the built-in ```str()``` constructor function to convert numbers into strings:

```foo
>>> x = 42
>>> "final count: " + str(x)
'final count: 42'
```

Any of the built-in numeric types can be converted to a string in this way.

We can use ```int()``` and ```float()``` to convert strings to numbers, so long as the strings are string expressions of decimal numbers:

```foo
>>> int("42")
42
>>> float("42")
42.0
>>> float("3.14159")
3.14159
```

Whitespace within the string before or after the number is tolerated, but there must be only one number and no non-numeric characters:

```foo
>>> int("4 2")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '4 2'
```

```foo
>>> int("22 birds")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '22 birds'
```

Earlier, we saw that integer literals can be expressed in hex, binary or octal as well as in decimal. When using ```int()```, the number string can only be in decimal form. The "\_" grouping delimiter can be used, however:

```foo
>>> int("12_345_678")
12345678
```

We've already seen that strings in Python 3.x use Unicode. Unicode supports many scripts that have their own decimal digit characters. In Python, conversion from number strings is supported for any characters that Unicode defines as decimal digits. In the following example, a number string using Arabic-script digits is converted to an ```int```:

```foo
>>> int("٤٢")
42
```

You can even mix and match digits from different scripts—though this isn't recommended:

```foo
>>> int("4٢")
42
```
