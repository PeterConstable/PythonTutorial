# Stuff not yet incorporated into refactored topics

There's also a built-in function that can be used for exponentiation, ```pow()```. When used with integer arguments, it returns an integer.

```foo
>>> pow(2, 8)
256
```

The ```abs()``` and ```pow()``` functions were introduced earlier. These can also be used with float arguments, in which case a float will be returned.

```foo
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
