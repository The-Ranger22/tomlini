import tomllib
import os
import re
import inspect
"""
Author: Levi Schanding

"""

class TomlKeyAttributeMismatch(Exception):
    pass

def _matching_cls_toml_keys(cls: object, toml: dict[str]) -> bool:
    return (
        frozenset(cls.__annotations__.keys()) == frozenset(toml.keys())
    )

def toml_init(cls: object):
    toml_dict: dict[str]

    # Check that the class annotations match the toml


    # with open(filename, "rb") as f:
    #     toml_dict = tomllib.load(f)

    

    # if not _matching_cls_toml_keys(cls, toml_dict): 
    #     raise TomlKeyAttributeMismatch("")

    @classmethod
    def load_from_toml(cls: object, filename: str) -> object:
        if not hasattr(cls, '__annotations__'):
            raise AttributeError("""
                '__annotations__' class attribute undefined! '@toml_init' requires your class to have annotations for each datafield. Example:
                    @toml_init
                    class ExampleCls:
                        dfield_1: <dtype>
                        dfield_2: <dtype>
                        ...
                        dfield_n: <dtype>
            """)

        if not os.path.exists(filename):
            raise FileNotFoundError(f"Could not locate TOML '{filename}'")

        if not re.search("\.toml$", filename):
            raise tomllib.TOMLDecodeError(f"Expecting file ending in '.toml', received '{filename}'")

        toml: dict[str]
        
        # load TOML config file
        with open(filename, "rb") as toml_handle:
            toml = tomllib.load(toml_handle)
        
        # Compare TOML keys against class annotations
        if not _matching_cls_toml_keys(cls, toml):
            raise TomlKeyAttributeMismatch("TOML keys and class annotations do not match!")

        return cls(
            *[toml[key] for key in inspect.getfullargspec(cls).args[1:]]
        )

    
    def save_to_toml(self, filename: str = f"{type(cls)}.toml"):
        print(filename)


    # Add functions to class
    cls.load_from_toml = load_from_toml
    cls.save_to_toml = save_to_toml
    return cls