# TOMLini

A minimal, unintrusive library that allows you to add the ability to initialize an object from a TOML file without having to go through the dictionary dance.

## Install

Available on PyPI

```bash
pip install tomlini
```

## Example

>All you need to do is create your class with the `@toml_init` decorator:


```python
# myclass.py

@toml_init
class MyClass:
    def __init__(v1, v2):
        self.v1 = v1
        self.v2 = v2

@toml_init
class MyClass2:
    def __init__(v3, v4: MyClass):
        self.v3 = v3
        self.v4 = v4

```

>Define your TOML file (make sure the TOML key names match the `__init__` parameter names!):

```TOML
# file1.toml

v1 = "aaa"
v2 = 1

```

```TOML
# file2.toml

v3 = [1, 2, 3]

[v4]
v1 = "aaa"
v2 = 1

```

>And you're off to the races!

```python
from myclass import MyClass, MyClass2

my_class = MyClass.load_from_toml("/path/to/file1.toml")

my_class_2 = MyClass2.load_from_toml("/path/to/file2.toml")

print(my_class.v1, my_class.v2)
# Outputs: 'aaa', 1

print(my_class_2.v4.v1)
# Outputs: 'aaa'


```