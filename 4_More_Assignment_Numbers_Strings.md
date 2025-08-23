# More About Assignment, Numbers and Strings

In lesson 2, we introduced the basics of working with numbers, expressions and variables: how to express numbers as literals, assign them to variables, and create numeric expressions using various operators. And in lesson 3 we got introduced to strings. In this lesson, we'll go into more detail on each of those topics.

* [Multiple assignment](#multiple-assignment)
* [Using compound assignment operators](#using-compound-assignment-operators)
* [Range and precision of `int` and `float`](#range-and-precision-of-int-and-float)
* [Different formats for numeric literals](#different-formats-for-numeric-literals)
* [Bitwise operations on integers](#bitwise-operations-on-integers)
* [Strings as Unicode character sequences](#strings-as-unicode-character-sequences)
* [Converting between number and string types](#converting-between-number-and-string-types)
* [What's next](#whats-next)

## Multiple assignment

We've already seen the familiar assignment operator, `=`, for assigning values to variables.

```foo
>>> x = 42
>>> y = "hey, there!"
```

Something that's very handy in Python is that you can assign values to multiple variables in a single statement.

```foo
>>> x, y = 42, "hey, there!"
>>> x
42
>>> y
'hey, there!'
```

You simply list two or more variables on the left, separated by commas, and then the same number of values on the right, also separated by commas. There must be the same number of variables on the left as there are values on the right, otherwise you'll get an error.

```foo
>>> x, y = 2, 3, 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

The examples above have literals as values, but you can also use expressions or functions.

```foo
>>> x, y = 3 * 19, len("spam")
>>> x
57
>>> y
4
```

## Using compound assigment operators

Like several other languages, Python supports compound (or _augmented_ or _in-place_) assigment operators that evaluate an expression and assign the result. For example:

```foo
>>> x = 6
>>> x += 5
>>> print(x)
11
```

In the second statement, `+=` is used to combine two steps into one. First, the expression `x + 5` is evaluated; then, the result is assigned back to `x`. It's convenient shorthand for `x = x + 5`.

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

>Note: some languages support `=+` and `=-` as well as `+=` and `-=`, with slightly different effects in looping conditions. In Python, `=+` and `=-` are meaningul, but they're not compound assignment operators! They're simply the assignment operator `=` with the following `+` and `-` interpreted as prefixes to the following number. For example,
>
>```foo
>>>> x =- 5
>```
>
>means exactly the same thing as
>
>```foo
>>>> x = -5

With strings, `+=` can be used as a compound concatenation/assignment operator.

```foo
>>> x = "boo"
>>> x += "hoo"
>>> x
'boohoo'
```

Similarly, `*=` can be used as a compound repeat-concatenation/assignment operator; the following operand is an integer.

```foo
>>> x = "boo"
>>> x *= 5
>>> x
'boobooboobooboo'
```

## Range and precision of `int` and `float`

In Python, `int`s are not limited to a particular range or machine representation. For example:

```foo
>>> 1000000000000000000000000000000000000000000000000000000000000000 - 1
999999999999999999999999999999999999999999999999999999999999999
>>>
>>> -888888888888888888888888888888888888888888888888888888888888888 + 2
-888888888888888888888888888888888888888888888888888888888888886
```

The `float` type, however, however, has limited precision. The actual limitation will depend on the specific Python interpreter you're using and the architecture of the machine you're running on. You can enter a float literal with any number of decimal places, but the value will be constrained by the precision limitation of your setup.

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

There's a way you can get details about the supported precision of `float` on your system, but it involves using certain features we haven't explored yet (importing a module, `sys`, that's included with your Python installation but not loaded by default). If you want to find out more, see the Python documentation for [sys.float_info](https://docs.python.org/3.8/library/sys.html#sys.float_info). Here's an example of what the detailed info looks like:

```foo
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
```

To get an idea of how this compares to floating value types in other languages, this is comparable to the [range for `double` in the Microsoft C++ compiler](https://docs.microsoft.com/en-us/cpp/cpp/data-type-ranges?view=vs-2019).

The `float` type in Python supports values for positive and negative infinity. These are obtained by passing certain strings to the `float()` function:

```foo
>>> x = float('inf')
>>> x
inf
>>> y = float('-infinity')
>>> y
-inf
```

Either the short or long strings, 'inf' or 'infinity', can be used. Also, case doesn't matter.

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

There are a few exceptions, but they involve another special `float` value, `nan`, meaning _not a (well-defined) number_. So, for example:

```foo
>>> x + y
nan
>>> x * 0
nan
>>> x / y
nan
```

You can obtain the `nan` value directly as follows:

```foo
>>> x = float('nan')
>>> x
nan
```

>Note: `nan` is not the same as 0, null or `None`.

Because `int`s aren't bounded, these concepts don't apply. (Happy counting galaxies, Buzz Lightyear! When you're done, come join us at Milliways.)

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

If you want to see integer values exprssed as hex, binary or octal strings, you can use the built-in `hex()`, `bin()` or `oct()` functions.

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

In the previous section, we saw that `int` values are unbounded, so it's possible to work with some really long number literals. (And if you need to write numbers as binary, those can quickly get long as well.) In daily life, we use grouping delimiters to make it clearer what the value is. For instance

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
>>> 0xffff_fff # not 4 gig!
268435455
```

For decimal digits, stick to groupings of three. (Some cultures use other sized groupings, but three is universally familiar.), For hex, use groupings of four or eight; and use eight for binary.

We've been talking about `int` literals. What about `floats`? Hex, binary or octal representations are not supported for `float`s. You can use the "\_" grouping delimiter, however.

```foo
>>> x = 87_234_786.29
>>> x
87234786.29
```

Up to now, we've seen examples of floats represented using common, decimal representation. There is another representation that's also used for float literals, the exponent form:

```foo
>>> 2.34e5
234000.0
```

The number after "e" is an exponent applied to a base of 10, and that is multiplied times the number before "e". For very large float values, results in interactive mode will use the exponent representation with a single-digit mantissa.

```foo
>>> 1234567890123456789.
1.2345678901234568e+18
```

## Bitwise operations on integers

In addition to arithmetic operators seen earlier, Python has a typical set of bitwise operators.

|Operator|Meaning|Example expression|
|--------|-------|-------|
|`\|` |bitwise or           |`x \| y` |
|`&` |bitwise and          |`x & y` |
|`^` |bitwise exclusive or |`x ^ y` |
|`<<`|left shift           |`x << 3`|
|`>>`|right shift          |`x >> 3`|
|`~` |complement / invert  |`~x`    |

There are also corresponding compound assignment operators for all but the bitwise complement.

|Operator |Example expression|Equivalent expression|
|---------|------------------|---------------------|
|`\|=` |`x \|= y`      |`x = x \| y`      |
|`&=` |`x &= y`      |`x = x & y`      |
|`^=` |`x ^= y`      |`x = x ^ y`      |
|`<<=`|`x <<= y`     |`x = x << y`     |
|`>>=`|`x >>= y`     |`x = x >> y`     |

Note that bitwise operations are only meaningful and supported for integers (`int`). Also, for shift operations, the second operand cannot be negative.

As in other languages, _bitwise or_, _and_ or _exclusive or_ set individual bits in a result value by comparing the corresponding bits in two operands:

* or: 1 if either operand bit is 1, else 0
* and: 1 if both operand bits are 1, else 0
* exclusive or: 1 if operand bits are different, else 0

_Right shift_ causes binary digits to be shifted right by a specified number of digits. For example:

```python
>>> bin(0b0010_1101 >> 2)
'0b1011'
```

_Right shift_ is equivalent to floor division by powers of 2. As existing digits shift right, 0 digits are inserted on the left; least-significant digits are simply dropped.

_Left shift_ causes binary digits to be shifted left by a specified number of digits. For example:

```python
>>> bin(0b0010_1101 << 6)
'0b101101000000'
```

_Left shift_ is equivalent to multiplication by powers of 2. As existing digits shift left, 0 digits are inserted on the right. Because integers in Python are unbounded, there are an infinite number of binary digits available, so digits on the left are never truncated or wrapped. This is a difference in behaviour compared to many other languages; we'll return to this below.

Conceptually, the _bitwise complement_ operator `~` performs a _bitwise NOT_:

* bitwise complement (_conceptually_): 1 if bit is 0, else 0

In practice, `~` works this way in Python _so long as you don't inspect actual bit patterns or try to compare with binary or hex literals_. (That is a difference in behaviour compared to many other languages; we'll return to this difference below.) In most situations, that is not an issue.

A typical usage for bitwise operations is to manipulate bits in a flags bitfield. For example, consider the following flag definitions:

```python
flag_INSTALLABLE = 0b0010
flag_RESTRICTED  = 0b0100
flag_EDITABLE    = 0b1000
mask_PERMISSIONS = 0b1111
```

To filter a value to just these flags, you'd use _bitwise and_ with the mask:

```python
    permissions_flags = my_flags & mask_PERMISSIONS
```

To check whether a given flag is set, you'd use _bitwise and_ with the flag constant:

```python
    if my_flags & flag_RESTRICTED == flag_RESTRICTED:
        # restricted flag is set; take appropriate actions
        ...
```

>Note: equality comparison will be covered in [lesson 5](5_Bool_Comparisons.md#comparison-expressions); `if` statements will be covered in [lesson 6](6_Intro_Functions_Flow_Control.md#the-if-statement).

To set a particular flag, you'd use _bitwise or_ with the flag constant:

```python
    # set the restricted flag
    my_flags |= flag_RESTRICTED
```

To clear the _restricted flag_, you'd use bitwise and together with bitwise complement:

```python
    # clear the restricted flag
    my_flags &= ~flag_RESTRICTED
```

### Matching fixed bit-width assumptions of other languages

In most languages, integer data types have specific, limited bit widths, which affects how binary operations will work. But in Python, integers are not bounded in bit width. This can lead to some differences in behaviour in certain situations, particularly when _left shift_ or _bitwise complement_ operations are involved.

For instance, in C, you could compare the result of a _left shift_ with a literal, as in the following:

```c
UInt16 x = 0b1011_1100;
UInt16 y = (UInt16)(x << 12);
if (y == 0xc000) // true
```

But you can't do the same directly in Python:

```python
>>> x = 0b1011_1100
>>> y = x << 12
>>> y == 0xc000
False
```

In C, the comparison assumes a limited bit width, with the _left shift_ causing high-order bits to be dropped. But in Python, those bits are not dropped.

Similarly, in C, you could compare the result of a _bitwise complement_ operation with a literal, as in the following:

```c
byte x = 4;
byte y = (byte)~x;
if (y == 0xfb) // true
```

But you can't do that directly in Python:

```python
>>> x = 4
>>> y = ~x
>>> y == 0xfb
False
```

In Python, if you need to closely match bit-width assumptions in other languages, you may need to add logic that provides fixed-bit-width assumptions.

When doing a _left shift_ operation, you can match the fixed-width assumptions of another language by applying `2**N - 1` as a mask to the result of the shift operation (where `N` is the assumed bit width).

```python
>>> x = 0b1011_1100
>>> y = (x << 12) & 0xffff
>>> y == 0xc000
True
```

When using a _bitwise complement_ operation, you can match the fixed-width assumptions of another language by applying the result of the _bitwise complement_ as a mask to `2**N - 1` (where `N` is the assumed bit width).

```python
>>> x = 4
>>> y = ~x & 0xff
>>> y == 0xfb
True
```

### Representation of negative integers in Python versus other languages

When integer data types in other languages have specific, limited bit widths, negative integer values are typically represented using [two's complement](https://en.wikipedia.org/wiki/Two%27s_complement) representation. In this representation, the value -1 has all bits set, -2 has all but the last bit set, and so on.

Signed 8-bit integers:

|Decimal value|Binary two's complement representation|
|:-:|:-:|
| -1  | 1111 1111 |
| -2  | 1111 1110 |
| -3  | 1111 1101 |
| -4  | 1111 1100 |
| ... | ...       |
|-125 | 1000 0011 |
|-126 | 1000 0010 |
|-127 | 1000 0001 |
|-128 | 1000 0000 |

Because of this, the _bitwise complement_ operation is equivalent to computing `-(n + 1)`, for an integer data type of a particular bit width.

For unbounded negative integers, the two's complement representation can't be assumed in practice, as it would require an infinite number of bits.

This is another form of the issue described above. We saw that results of _left shift_ or _bitwise complement_ operations could not be compared with literal values that involved fixed-bit-width assumptions unless accommodation to those assumptions were made. The same is true for comparing negative integers with literals that assume some fixed-width representation.

For example, the following comparison can be made in C#:

```cs
int x = -2;
if unchecked(x == (int)0xffff_fffe)  // true
```

In Python, to make a similar comparison of a negative value `x` to a literal, add `x` to `2**N`, where `N` is the assumed bit width.

```python
>>> x = -2
>>> (x + 2**32) == 0xffff_fffe
True
```

Also, when the `bin()` function is used to convert a negative number to a binary string representation, do not expect to see the two's complement representation as you would get for similar operations in other languages. For example, compare results from C# versus Python:

C#:

```cs
> Int16 x = -5;
> Convert.ToString(x, 2)
"1111111111111011"
```

Python:

```python
>>> x = -5
>>> bin(x)
'-0b101'
```

The Python string has the same binary representation as +5, but with "-" prefixed.

## Strings as Unicode character sequences

In lesson 3, we learned that Python strings are sequences of characters. Going into more detail, strings in Python 3.x are sequences of _Unicode_ characters. A string variable can include any Unicode character. Likewise, string literals can include any Unicode character, if supported by the console or editor you're using.

But even if they're not supported by the console or editor, any Unicode character can be written in a string literal as an escape sequence with the prefix "\u" or "\U".

```foo
>>> "convert $ to \u20ac"
'convert $ to €'
```

The "\\u" prefix is used for Unicode characters from U+0000 to U+FFFF, and exactly four hex digits must be provided: \\uxxxx. The "\\U" prefix can be used for any Unicode characters from U+0000 to U+10FFFF, and exactly eight hex digits must be provided: \\Uxxxxxxxx.

```foo
>>> '\U0001f603'
'😃'
```

>If you learned about Unicode in the past, you might have heard about _surrogate pairs_: two code units in the range 0xDC00 to 0xDFFF that are combined to represent Unicode characters U+10000 and above. Forget about surrogate pairs! To specify a character from U+10000 or above in an escape sequece, you must specify the Unicode code point directly with an eight-digit \\U sequence.

Python has useful built-in functions to go between a Unicode character and the integer value for its code point. The `ord()` function takes any single Unicode character and returns its code point as an `int`.

```foo
>>> ord('€')
8364
```

>As always, numeric results in interactive mode are presented in decimal. But Unicode code points are normally cited in hex. You can use the `hex()` function to get a hex string representation:
>
>```foo
>>>> hex(ord('€'))
>'0x20ac'
>```

The `chr()` function is the inverse of `ord()`: it takes a number and returns a string with the Unicode character for that code point.

```foo
>>> chr(8364)
'€'
```

>Note: The `ord()` function only takes a single character, not a sequence of multiple characters. Similarly, the `chr()` function only takes a single numeric value.

## Converting between number and string types

In lesson 2, we learned about the basic numeric types, `int`, `float` and `complex`. We also saw that numeric expressions that have a `float` as one of the operands always result in a `float`. But sometimes, you may need to get an `int` variable for a subsequent step. Each of the basic built-in types has a corresponding constructor function that can be used to convert between types.

The following examples show an `int` literal being converted to a `float` value using the `float()` constructor fuction; and `float` being converted to `int` using the `int()` constructor function:

```foo
>>> float(2)  # converts int to float
2.0
>>> int(2.0)  # converts float to int
2
```

Note that `int()` truncates the `float` value:

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

Integer and float values can be converted to complex using the `complex()` constructor function.

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

> It is possible to get the real or imaginary parts of a complex number using the `.real` and `.imag` attributes of a `complex` object. (This is getting ahead—we haven’t yet covered that all values in Python are objects.) For example:
> ```
> >>> (4+1j).real
> 4.0
> >>> (4+1j).imag
> 1.0
> ```

When working with strings, we may want to concatenate a number into a string. But Python doesn't allow an `int`, `float` or `complex` to be concatenated onto a string.

```foo
>>> x = 42
>>> "final count: " + x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

But we can use the built-in `str()` constructor function to convert numbers into strings. This works for any of the numeric types:

```foo
>>> x = 42
>>> "final count: " + str(x)
'final count: 42'
```

```foo
>>> "Patient temp: " + str(37.9)
'Patient temp: 37.9'
```

```foo
>>> "This is complex: " + str(2+3j)
'This is complex: (2+3j)'
```

>Note: Integrating numbers into strings, or _string formatting_, is a bigger topic, and there are other ways to do that with more and better options. We'll save that for a later lesson.

We can use `int()` and `float()` to convert strings to numbers, so long as the strings are string expressions of decimal numbers:

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

Earlier, we saw that integer literals can be expressed in hex, binary or octal as well as in decimal. When using `int()` to convert from a string, however, the number string can only be in decimal form.

```foo
>>> int("0x42")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '0x42'
```

The "\_" grouping delimiter can be included in the string:

```foo
>>> int("12_345_678")
12345678
```

We've already seen that strings in Python 3.x use Unicode. Unicode supports many scripts that have their own decimal digit characters. In Python, conversion from number strings is supported for any characters that Unicode defines as decimal digits. In the following example, a number string using Arabic-script digits is converted to an `int`:

```foo
>>> int("٤٢")
42
```

You can even mix and match digits from different scripts—though this isn't recommended:

```foo
>>> int("4٢")
42
```

## What's next

There's more we could cover on numbers and strings, but it's time for something else. In the [next lesson](5_Bool_Comparisons.md), we'll learn about another booleans and logical expressions.
