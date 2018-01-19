## list
## 当使用 sorted 排序是并不会改变原有的 list 而是会
# 生成一个新的 list
## attaction
## 使用 list 作为 stack 时是合理的，但作为 queue 使用

# While appends and pops from the end of list are fast,
# doing inserts or pops from the beginning of a list is slow ，
# because all of the other elements have to be shifted by one.
# 可以使用 from collections import deque

 # call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# => ['banana', 'loganberry', 'passion fruit']

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# => [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
# => [1, 2, 3, 4, 5, 6, 7, 8, 9]
# you can also use this way with 'reduce'
## functools.reduce(lambda x,y: x+y, vec)

# transpose rows and columns:
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]

 [[row[i] for row in matrix] for i range(4)]
 [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# method 2
test = []
 for i in range(4):
     test.append([row[i] for row in matrix])

# method 3
list(zip(*matrix))

# Tuples and sequences
# 1. A tuple consists of a number of values separated by commas
t = 123, 456, 'hello'
(123, 456, 'hello')
# 2. tuples are immutable, but they can contain mutable objects
# 3. tuples may be nested
t[0] = 44 # error
v = ([1, 2, 3], [3, 2, 1])
v[0] = [7,8] # error
v[0][0] = 8
# => ([8, 2, 3], [3, 2, 1])

t = 123, 456, 'hello!'
x, y, z = t
# => x = 123, y = 456, z = 'hello!'
# multiple assignment is really just a combination of tuple packing and sequence unpacking

# Sets
## Curly braces or the set() function can be used to create sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# => {'orange', 'pear', 'banana', 'apple'}
a = set('abracadabra')
# => {'a', 'r', 'b', 'c', 'd'}
# 1. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
# 2. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary

# Dictionaries
# 1. Dict key must be immutable
## tuple can also be used as keys if they contain  only strings,numbers, or tuples, if tuple contains any mutable
## object either directly or indirectly, it cannot be used as keys
d = {'d': 1, 'c': 3, 'a': 7, 'f': 8}
list(d.keys())
# => ['d', 'c', 'a', 'f']
# The dict() constructor builds dictionaries directly from sequences of key-value pairs
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# => {'sape': 4139, 'jack': 4098, 'guido': 4127}
{x: x**2 for x in (2, 4, 6)}
# => {2: 4, 4: 16, 6: 36}

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
dict(sape=4139, guido=4127, jack=4098)
# => {'sape': 4139, 'jack': 4098, 'guido': 4127}

# Looping Techniques
## dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)
## loop sequence
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
## loop over two or more sequences at the same time the entries can be paired with the zip() function
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(q,a)
## To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list
## while leaving the source unaltered.
bb = ['c', 'a', 'd', 'b', 'b']
for i in sorted(set(bb)):
    print(i)
# => a b c d
## donot  change a list while you are looping over it; however, it is often simpler and safer to create a new list instead
