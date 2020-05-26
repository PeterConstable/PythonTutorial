# PythonTutorial

This is a Python 3 Tutorial (or, at least, the beginnings of one).

Some programming knowledge and experience is assumed—it's not an _intro to programming_ course. Familiarity with typical programming concepts is assumed; for instance, it's assumed you know what variables and ```for``` statements are, but not necessarily how to use them (or use them well) in Python. But deep background and experience with other programming languages isn't assumed. This is geared toward someone with novice or intermediate skill in some other languages.

Topics are presented in an order that attempts to build up knowledge in useful chunks. Some things in Python (or any language) have lots of details, but you don't need to learn them all at once to get started doing something useful.

You might come looking for a specific detail because you need that for whatever project you're using to learn on, and not be able to find it in earlier chapters. Sorry, this isn't a reference manual. Maybe eventually an index might get added that could help. In the meantime, check the official [Python documentation](https://docs.python.org/3.8/index.html), or try asking on [stack**overflow**](https://stackoverflow.com/).

**Contents:**

* [Some Basics](1_SomeBasics.md#sof)
* [Working with Numbers, Expressions and Variables](2_Numbers_Expressions_Variables.md#sof)
* [Introduction to Strings](3_Intro_Strings.md#sof)
* [More About Assignment, Numbers and Strings](4_More_Assignment_Numbers_Strings.md#sof)
* [Booleans, Comparisons and Logical Expressions](5_Bool_Comparisons.md#sof)
* [Intro to Functions and Flow Control Statements](6_Intro_Functions_Flow_Control.md#sof)
* [Sequence Types: Lists, Tuples and Ranges](7_List_Tuple_Range.md#sof)
* [Flow Control Using ```for```](8_For.md#sof)
* [Our First Program](9_Sample_Program.md#sof)
* ... (more to come)
* [List Comprehensions](11_List_Comprehensions.md#sof)
* ...

## Background: _Why another Python tutorial?_

Good question. It was started mainly as a personal learning tool. I find that writing about something helps me clarify my thoughts. And trying to teach something _well_ requires me to know it and be able to communicate it. In order to explain it to someone else, I have to explain it to myself first.

Also, I started learning Python using some other tutorials, but sometimes found certain things a little frustrating. The official [Python Tutorial](https://docs.python.org/3.8/tutorial/index.html) got me going on several things, but at points it goes into too much detail at once, and so a progressive learning flow is broken.

One example of that is the introduction to functions in [topic 4](https://docs.python.org/3.8/tutorial/controlflow.html): it immediately drills into the complex details of function parameter specifications. That's definitely stuff that you need to know to be proficient. But I think a better didactic approach is to build up learnings in chunks that can be quickly put to use. Someone that's just learning about defining a function in Python probably isn't immediately going to want to practice with ```my_func(pos1, pos2, /, pos_or_kwd, ...)```.

The opposite also happens in some tutorials: presenting a specific area in breadth while providing practical application. That's more like reference material. The [w3schools Python tutorial](https://www.w3schools.com/python/default.asp) has some of this tendency. For example, the 7th topic, [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp) introduces all of the built-in data types, then gives "Try it" examples that simply show a variable assigned with an object of some type having that type. The lesson doesn't teach how to work with any of them.

Because topics in the w3schools content tend toward breadth, they sometimes leave out important or useful details. The [Python Numbers](https://www.w3schools.com/python/python_numbers.asp) topic doesn't say anything about hex or other representations; it doesn't mention the ability to use ```_``` as a grouping delimiter; and it doesn't say anything about the range of supported values or rounding errors for some operations when using ```float```.

While still learning, I often go back to the w3schools Python material to check on something, but I use it more like reference material. (It's easier to navigate to a topic than on [docs.python.org](https://docs.python.org/3.8/index.html)).

So, I felt motivated to start writing about Python. Initially, it was to capture learnings about things that seemed unusual or quirky coming from a language like C or C#. (E.g., _How do I step through elements in a sequence? There isn't a switch statement? How do I implement out parameters or return multiple values?_). Or learnings about (sometimes esoteric) details that I got tripped up on or found it hard to discover. (E.g., _How does ```__new__``` work? Is Python strongly typed or not? Are sequence arguments copied or not?_) Even some things I expected to be pretty familar involved learnings for me. _(So write it down to reinforce the learning.)_

And once I started writing, I thought, _I should try to present this in a good didactic manner I would have found useful._ So, I've written to some extent with myself in mind as the audience. But I've also tried to shift the focus toward someone who doesn't yet know what I've come to know.

## Guiding didactic principles

Some guiding principles I try to follow:

* Build up knowledge in absorbable and _usable_ chunks.
* Build on existing knowledge.
  * Don't depend on knowing something non-obvious that hasn't been taught yet. Avoid using examples that do that.
  * Don't teach something that requires another thing to be truly useful if you haven't yet taught enough about that other thing for the student to be able to use it on its own.
* Don't introduce unrelated things at the same time or in the same lesson.
* Interactive mode captures that are long or that have long lines can be hard to read. Make sure its easy to distinguish the individual examples. If needed, break the capture into a sequence of separate code blocks.
