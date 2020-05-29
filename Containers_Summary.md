# Appendix: Summary of Container Types and Operations

This is a summary of container-like types, their characteristics and available operations.

## Characteristics

|                 | Sequence | Mutable | Limitation on elements |
|-----------------|:--------:|:-------:|:--:|
| ```str```       | ✔       |         | Unicode characters |
| ```tuple```     | ✔       |         |
| ```bytes```     | ✔       |         | bytes
| ```list```      | ✔       | ✔      |
| ```bytearray``` | ✔       | ✔      | bytes
| ```frozenset``` |         |         |
| ```set```       |         | ✔       | immutable, hashable |
| ```dict```      |         | ✔       | key must be hashable |

## Available operations

In the following table, "obj" is an object of the given type, "x" is some object, "i", "j", "k" and "n" are non-negative integers, and "t" is an iterable object. "*t" indicates one or more iterables.

||```tuple```|```bytes```|```list```|```bytearray```|```frozenset```|```set```|```dict```|
|-:|-|-|-|-|-|-|-|
| _Constructor:_       |
| ```class(```_iterable_```)```              | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| _Accessing elements:_
| ```obj[```_i_```]```                       | ✔ | ✔ | ✔ | ✔ |
| ```obj[```_i_```:```_j_```]```             | ✔ | ✔ | ✔ | ✔ |
| ```obj[```_i_```:```_j_```:```_k_```]```   | ✔ | ✔ | ✔ | ✔ |
| ```obj[```_key_```]```                     |  |  |  |  |  |  | ✔ |
| _Membership:_
| _x_ ```in obj```                           | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| _x_ ```not in obj```                       | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| _key_ ```in obj```                         |  |  |  |  |  |  | ✔ |
| ```obj.index(```_x_```)```                 | ✔ | ✔ | ✔ | ✔ |
| ```obj.index(```_x_```,``` _i_```)```      | ✔ | ✔ | ✔ | ✔ |
| ```obj.index(```_x_```,``` _i_```,``` _j_```)```| ✔ | ✔ | ✔ | ✔ |
| ```obj.count(```_x_```)```                 | ✔ | ✔ | ✔ | ✔ |
| _Assigning to elements:_
| ```obj[```_i_```] =``` _x_                 |  |  | ✔ | ✔ |
| ```obj[```_i_```:```_j_```] =``` _t_       |  |  | ✔ | ✔ |
| ```obj[```_i_```:```_j_```:```_k_```] =``` _t_ ||| ✔ | ✔ |
| ```obj[```_key_```] =``` _x_               |  |  |  |  |  |  | ✔ |
| _Adding elements:_
| ```obj.append(```_x_```)```                ||| ✔ | ✔ |
| ```obj.extend(```_t_```)```                ||| ✔ | ✔ |
| ```obj.insert(```_i_```,```_x_```)```      ||| ✔ | ✔ |
| ```obj +=``` _t_                           ||| ✔ | ✔ |
| ```obj *=``` _n_                           ||| ✔ | ✔ |
| ```obj.add(```_x_```)```                   |||  |  | | ✔ |
| ```obj.update(```*_t_```)```               |||  |  | | ✔ |
| _Removing elements:_
| ```del obj[```_i_```]```                   ||| ✔ | ✔ |
| ```del obj[```_i_```:```_j_```]```         ||| ✔ | ✔ |
| ```del obj[```_i_```:```_j_```:```_k_```]```||| ✔ | ✔ |
| ```obj.pop()```                            ||| ✔ | ✔ |  | ✔ |
| ```obj.pop(```_i_```)```                   ||| ✔ | ✔ |
| ```obj.remove(```_x_```)```                ||| ✔ | ✔ |  | ✔ |
| ```obj.discard(```_x_```)```               |||  |  | | ✔ |
| ```obj.clear()```                          ||| ✔ | ✔ |  | ✔ |
| _Other operations:_
| ```obj.copy()```                           ||| ✔ | ✔ |  | ✔ |
| ```obj1 + obj2```                          | ✔ | ✔ | ✔ | ✔ |
| ```obj *``` _n_ <br> _n_ ```* obj```           | ✔ | ✔ | ✔ | ✔ |
| ```len(obj)```                             | ✔ | ✔ | ✔ | ✔ |
| ```max(obj)```                             | ✔ | ✔ | ✔ | ✔ |
| ```min(obj)```                             | ✔ | ✔ | ✔ | ✔ |
| ```obj.reverse()```                        ||| ✔ | ✔ |
| ```obj.sort(```*, _key=None_, _reverse=False_```)```|||✔|

Sets have several additional set-specific methods...

Strings have many additional string-specific methods...
