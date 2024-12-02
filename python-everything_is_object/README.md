# Python3: Mutable, Immutable... everything is object!

## Introduction
In this blog post, we will explore the fascinating world of Python objects. We will delve into the concepts of mutable and immutable objects, understand their significance, and see how Python treats them differently. This journey will help you grasp the nuances of Python's object model and how it impacts your code.

## Id and Type
Every object in Python has a unique identifier and a type. The `id()` function returns the identity of an object, which is its memory address in CPython. The `type()` function returns the type of an object. Understanding these concepts is crucial as they form the foundation of how Python handles objects.

```
a = 42
print(id(a))  # Unique identifier
print(type(a))  # <class 'int'>
```

## Mutable Objects
Mutable objects are those that can be changed after their creation. Lists, dictionaries, and sets are examples of mutable objects. When you modify a mutable object, its identity remains the same, but its content changes.

```
my_list = [1, 2, 3]
print(id(my_list))  # Unique identifier
my_list.append(4)
print(id(my_list))  # Same identifier, content changed
```

## Immutable Objects
Immutable objects, on the other hand, cannot be changed after their creation. Examples include integers, floats, strings, and tuples. Any operation that modifies an immutable object will create a new object with a different identity.

```
my_str = "Hello"
print(id(my_str))  # Unique identifier
my_str += " World"
print(id(my_str))  # Different identifier, new object created
```

## Why Does It Matter?
Understanding the difference between mutable and immutable objects is essential because it affects how Python handles variables and memory. Mutable objects can lead to unexpected behavior if not handled carefully, especially when passed as arguments to functions.

## How Arguments Are Passed to Functions
In Python, arguments are passed to functions by assignment. This means that the function receives a reference to the object, not a copy of it. For mutable objects, this can lead to changes in the original object, while for immutable objects, the original object remains unchanged.

```
def modify_list(lst):
    lst.append(4)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 4]

def modify_string(s):
    s += " World"

my_str = "Hello"
modify_string(my_str)
print(my_str)  # "Hello"
```

## Conclusion
Understanding the concepts of mutable and immutable objects in Python is crucial for writing efficient and bug-free code. By mastering these concepts, you can better manage memory, avoid unexpected behavior, and write more predictable and maintainable code.
