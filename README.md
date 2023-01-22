# TOMLini

A minimal, unintrusive library that allows you to add the ability to initialize an object from a TOML file without having to go through the dictionary dance.

## Example

>All you need to do is create your class with the `@toml_init` decorator:


```python
# myclass.py

@toml_init
class MyClass:
    def __init__(v1, v2):
        self.v1 = v1
        self.v2 = v2

```

>Define your TOML file (make sure the TOML key names match the `__init__` parameter names!):

```TOML
# file.toml

v1 = "aaa"
v2 = 1

```

>And you're off to the races!

```python
from myclass import MyClass

my_class = MyClass.load_from_toml("/path/to/file.toml")

print(my_class.v1, my_class.v2)


```