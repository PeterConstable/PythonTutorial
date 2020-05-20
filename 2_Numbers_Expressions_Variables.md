# Working with Numbers, Expressions and Variables

In this lesson, we'll start out by quickly covering some basics of working with numbers.

You can enter a number literal as a statement, and the Python interpreter will evaluate it:

```foo
>>> 6
6
```

Negative value literals are written with a prefixed "-". Positive values can be written with a prefixed "+", but that's optional and is always left out when results are shown.

```foo
>>> -6
-6
>>> +18
18
```

You can also enter numeric expressions for Python to evaluate:

```foo
>>> 6 + 42
48
>>> 6 - 42
-36
```

Python has two basic numeric types that are frequently used: ```int```, for integers, and ```float```, for real numbers (in the math sense—integers, rationals or irrationals). (There's a third basic numeric type, ```complex```; we'll skip that for now.) A number literal without any decimal point is an ```int```; but a literal that has a decimal point is a ```float```. You can enter a ```float``` literal without any decimal digits, but the evaluated results shown in interactive mode will always have at least one decimal digit.

```foo
>>> 42.
42.0
```

Naturally, numbers can be assigned to variables, and variables can be used in expressions.

```foo
>>> x = 42
>>> y = 3.14159
>>> x
42
>>> y
3.14159
>>> x + y
45.14159
```

Python has a typical set of numeric operators:

* ```+```: addition
* ```-```: subtraction
* ```*```: multiplication
* ```/```: real division
* ```//```: integer division
* ```%```: modulo (remainder)
* ```**```: exponentiation

Complex expressions can be written using multiple numbers and operators. Of course, there is a precedence order for how things get evaluated.

```foo
>>> 3 + 4 * 2  # multiplication takes precedence over addition
11
```

If a different order of evaluation is needed, you can include parentheses to indicate the desired intent.

```foo
>>> (3 + 4) * 2  # expression in parens takes precedence over multiplication
14
```

When an addition, subtraction or multiplication expression has two ```int``` operands, the result is an ```int```.

```foo
>>> 6 + 2
8
>>> 19 - 11
8
>>> 7 * 42
294
```

But if either operand is a ```float```, the result will be a ```float```.

```foo
>>> 6. + 2
8.0
>>> 2 + 13.
15.0
```

With the division operator, ```/```, the result is always a ```float```, even if the result in an integral value.

```foo
>>> 4 / 2
2.0
```

To do integer division—that is, division of two integers that returns an ```int``` (and discards any fractional portion)—use the ```//``` operator:

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

To get an integer remainder from division of two ```int```s, the modulo operator is ```%```.

```foo
>>> 5 % 3
2
```

Exponentiation of two ```int```s also returns an ```int```.

```foo
>>> 2 ** 8
256
```

The ```//```, ```%``` and ```**``` operators can also be used with ```float```s. If either operand is a ```float```, the result will be a ```float```.

```foo
>>> 4. ** 2
16.0
```

Integer division always returns an integral value, though the result will be a ```float``` if either operand is a ```float```.

```foo
>>> 5.3 // 2
2.0
```

```float```s have a limited precision, and some operations will introduce rounding errors. You can do use the modulo operator with non-integral values, but the result may have some rounding error.

```foo
>>> 5.3 % 2  # expecting 1.3
1.2999999999999998
```

```foo
>>> 11 % 2.2  # 11 = 2.2 * 5, so remainder should be 0?
2.1999999999999993
```

Exponentiation can take a ```float``` as the base operand and will return a ```float```:

```foo
>>> 4. ** 2
16.0
>>> 2.2 ** 8
548.7587353600004
```

A ```float``` can also be used for the exponent operand. For example, this provides a way to get a square root:

```foo
>>> 4 ** .5
2.0
```

How about cube root?

```foo
>>> 27 ** 1/3  # cube root is 3?
9.0
```

Oops! We forgot about the order of operations: exponentiation takes precedence over division. Let's add some parenthesis; and just for the sake of it, add another sub-expression:

```foo
>>> 27 ** (1/(8-5))  # roundabout way to ask for cube root
3.0
```

Note that exponentiation with non-integral exponents can have rounding errors:

```foo
>>> 64 ** (1/3)  # cube root of 64 is 4
3.9999999999999996
```

Most of the above was shown with numeric literals so we can see the values. But any of it could have been done with variables.

```foo
>>> x = 27
>>> y = 8
>>> z = 5
>>> x ## (1/(y-z))
27
```

Two other common numeric operations are to get the additive or multiplicative inverse of something. To get the additive inverse of an expression, simply enclose it in parenthesis and add the "-" prefix:

```foo
>>> -(5 * 4 + 2 ** 3)
-28
```

Of course, if the expression is a single number or variable, the parentheses aren't needed.

```foo
>>> x = 6
>>> -x
-6
```

Similarly, to get the multiplicative inverse of something, enclose an expression in parentheses (if needed) and divide 1 by that expression.

```foo
>>> x = 5
>>> 1/x
0.2
>>> 1/(17 * (2 + 3))
0.011764705882352941
```

One other common numeric operation is to get an absolute value. Python has a built-in function for this, ```abs()```.

```foo
>>> abs(13 - 27)
14
>>> x = 42
>>> abs(13 - x)
29
```

## Next up

There's more to learn about numbers, and about variables. But we'll hold off to introduce some other useful things first. In the next lesson, we take a first look at strings.
