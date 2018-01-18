#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# for~
for i in range(5):
    print(i)

for i in range (1,10,2):
    print(i)

print(range(10))

print(list(range(5)))

### functions
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print("arguments:",arg)
    print("-" * 40)
    for kw in keywords:
        print("keywords:", kw, ":", keywords[kw])

print("-" * 20, "cheeseshop", "-" * 20)
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
# -------------------- cheeseshop --------------------
# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# arguments: It's very runny, sir.
# arguments: It's really very, VERY runny, sir.
# ----------------------------------------
# keywords: shopkeeper : Michael Palin
# keywords: client : John Cleese
# keywords: sketch : Cheese Shop Sketch

## lambda
print("-" * 20, "lambda", "-" * 20)
def lambda_test(n):
    return lambda x: x+n
lambda_test(42)
print(lambda_test(0))

### python 常用
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
filter(lambda x: x % 3 == 0, foo)
## == print([x for x in foo if x % 3 == 0])
## =>[18, 9, 24, 12, 27]
map(lambda x: x * 2 + 10, foo)
## == print [x * 2 + 10 for x in foo]
# =>[14, 46, 28, 54, 44, 58, 26, 34, 64]
functools.reduce(lambda x, y: x + y), foo)
# => 134

## lambda 常用于简化表达和需要函数对象，在语法上限定于单个表达式


## code style
#1. use CamelCase for classes and lower_case_with_underscores for functions and methods.
#Always use self as the name for the first method argument

#2.Use spaces around operators and after commas,
#but not directly inside bracketing constructs: a = f(1, 2) + g(3, 4).
