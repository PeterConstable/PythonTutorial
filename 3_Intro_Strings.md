# Introduction to Strings

In the previous lesson, we explored working with numeric literals and variables. In this lesson, we'll do the same for strings.

Some types in Python are _sequence types_, which means that they contain a sequence of elements. Strings are one of the sequence types. We'll learn about some useful ways you can interact with the elements within a sequence, as well as the built-in ```len()``` function that can be used with sequences.

* [String basics](#string-basics)
* [String concatenation](#string-concatenation)
* [Strings as character sequences](#strings-as-character-sequences)
* [Strings are immutable](#strings-are-immutable)
* [What's next](#whats-next)

## String basics

Strings in Python have the type ```str```. You can enter a string literal as a statement, and the Python interpreter will evaluate it. String literals must be enclosed in double or single quotation marks ("..." or '...').

```foo
>>> "spam and eggs"
'spam and eggs'
```

When a string result is returned in the interactive mode console, it will be enclosed in quotation marks. (Usually, it will be single quotes, but in some cases double quotes will be used.)

Results from the ```print()``` function are strings, but these are not enclosed in quotes when displayed in the console.

```foo
>>> print("eggs and spam")
eggs and spam
```

Of course, a string can be assigned to a variable.

```foo
>>> her_name = "Eliza Doolittle"
>>> her_name
'Eliza Doolittle'
```

When a string is enclosed in double quotes, single quote marks are interpreted as characters within the string.

```foo
>>> his_name = "'Enry 'Iggins"
>>> his_name
"'Enry 'Iggins"
```

Similarly, if the string is enclosed in single quotes, a double quote mark is interpreted as part of the string.

```foo
>>> 'He said, "More spam, please."'
'He said, "More spam, please."'
```

If you try to include a double or single quote mark within a string that enclosed in the same kind of quote mark, you'll end up getting an error:

```foo
>>> "spam and "spam""
  File "<stdin>", line 1
    "spam and "spam""
               ^
SyntaxError: invalid syntax
```

To get around this, the quote marks within the string can be represented using an escape sequence, with a "\\" prefix.

```foo
>>> "spam and \"spam\""
'spam and "spam"'
```

Multi-line string literals are also supported. These are entered by enclosing the string inside three double quote marks before and after, """...""".

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

A multi-line string can also be entered in a single line using double or single quotes with the new-line escape sequence.

```foo
>>> print("cats\nand dogs")
cats
and dogs
```

## String concatenation

A common operation for strings is concatenation. For string literals, you can concatenate simply by listing the literal elements in a line with nothing or only whitespace in between.

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

As expected, the strings are concatenated without any whitespace added. This is different from what happens in the ```print()``` function if multiple string arguments are passed: ```print()``` always separates the items passed to it with a space.

```foo
>>> "spam" "and" "eggs"
'spamandeggs'
>>> print("spam", "and", "eggs")
spam and eggs
```

Strings literals can also be concatenated by using the string concatenation operator, ```+```.

```foo
>>> "humming" + "bird"
'hummingbird'
```

In a concatenation expression with string variables, the ```+``` operator must be used between the variables and any literals:

```foo
>>> "The main characters are " + her_name + " and " + his_name
"The main characters are Eliza Doolittle and 'Enry 'Iggins"
```

Python also supports a second kind of string concatenation operator: the ```*``` operator can be used to concatenate multiple instances of a string. The way to do this is to write an expression of the form _n_ * _str_, where _n_ is an integer. For example:

```foo
>>> 4 * "really " + "long"
'really really really really long'
```

You can write the integer and string operands in either order: both work the same way.

```foo
>>> "It was l" + 'o' * 8 + "ng"
'It was loooooooong'
```

## Strings as character sequences

As mentioned above, ```str``` is a sequence type: strings contain a sequence of zero or more character elements. There are various ways you can interact with the character elements of a string. (These mechanisms can also be used with other sequence types we'll learn about later.)

One common thing you'll need to do is to find out about the length of a string. To do that, we use the ```len()``` function.

```foo
>>> len("spam")
4
>>> len(her_name)
15
>>> len("")
0
```

Another common operation is to inspect a single character within the string. You indicate the desired character using a zero-based index (0 for the first character, 1 for the next character, etc.). The indexed character will be returned as a single-character string. This is done as in the following example:

```foo
>>> her_name[3]
'z'
```

You can also extract a sub-string, or _slice_, by specifying a range using the starting and ending indices:

```foo
>>> her_name[0:5]
'Eliza'
```

It's important to understand how the range specification works: think of each number as a position _before_ the indexed character. In this example, "0:5" indicates a range that _begins before_ the character at index 0 and _ends before_ the character at index 5. In particular, note that the result does not include the character at index 5.

This may take a little getting used to. One thing that's handy, though, is that the difference between the ending and starting indices is the desired length. So, suppose you have a variable for the starting position and another variable for the length. It's easy to use those to extract the desired slice, as in this example:

```foo
>>> start_posn = 0
>>> length = 5
>>> her_name[start_posn : start_posn + length]
'Eliza'
```

Usually you'll want the ending position to be after the starting position. If it's the same as or before the starting position, that implies a length of zero, and you'll get the empty string.

```foo
>>> her_name[5:3]
''
```

So, if you unexpectedly get an empty string returned, check your indices!

Another thing you can do with the sequence range specification is to indicate a range indexed from the end of the string. You do this by using negative index values: -1 means the position before the last character, -2 means the position before the second-last character, and so on. Here's an example:

```foo
>>> her_name[-6 : -2]
'litt'
```

You can combine positive and negative indices in the range specification.

```foo
>>> her_name[-5: 13]
'itt'
```

Doing that with integer literals in your code is probably not a good idea as it's less obvious what is intended or what the result will be. But it may be useful if you have code logic that calculates start and end positions for the range.

Keep in mind that an ending position before the starting position will result in an empty string. That also applies when indexing from the end with negative indices.

```foo
>>> her_name[-5 : -7]
''
```

If both indices are positive or both indices are negative, the a generalization that holds is that you'll get an empty string _if the ending index is less than or equal to the starting index_. If you mix positive and negative indices, however, that doesn't work.

If you want to get a sub-string that starts at the beginning of a string, you can indicate 0 as the starting position. But an even easier way is just to leave out the first index: that means to start at the beginning:

```foo
>>> her_name[ : 8]
'Eliza Do'
```

Similarly, if you leave out the second index, that indicates that the ending position is the end of the string.

```foo
>>> her_name[-5 : ]
'ittle'
```

Leaving out the ending index is the same as specifying ```len(her_name)``` as the ending index.

```foo
>>> her_name[-5: len(her_name)]
'ittle'
```

There's one more thing you can do with these sequence range specification, though you'll probably use this less often: add a third number indicating a _step_ amount—how many characters in the string to advance after each extracted character. For example, the following requests _every other_ character from the first 8 characters in the string:

```foo
>>> her_name[0:8:2]
'EiaD'
```

This will get every third character from the entire string:

```foo
>>> her_name[::3]
'EzDlt'
```

## Strings are immutable

Since we have a way to access individual characters and slices within the string, you might wonder if its possible to change individual characters or sub-strings within the string. In Python, strings are immutable—meaning that the elements within the string cannot be changed. If you try to assign new values to any of the elements, you'll get an error:

```foo
>>> his_name[0:1] = "He"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

If you need to change a portion of a string, you have to do that by constructing a new string.

For examply, consider the ```his_name``` string variable we created in an earlier example:

```foo
>>> his_name
"'Enry 'Iggins"
```

Suppose we want to change the spelling to the way Professor Higgins would insist it be spelled, "Henry Higgins". We can use range specifications as above to get the parts that are correct, and concatenate those together with replacements where needed.

```foo
>>> his_corrected_name = "He" + his_name[2:6] + "Hi" + his_name[8:]
>>> his_corrected_name
'Henry Higgins'
```

## What's next

Here's a closing thought for this lesson:

```foo
closing_thought = "There's l" + 8 * 'o' + 'ts more still to learn about working with strings."
```

So far, we've introduced numbers, strings and assigning those values to variables. There are a few more things to know about each of those that you're going to find useful. We'll cover those in the [next lesson](4_More_Assignment_Numbers_Strings.md) before moving on to other topics.
