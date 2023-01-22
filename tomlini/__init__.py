import tomllib
import os
import re
import inspect
"""
Author: Levi Schanding

"""


def _add_init_args_and_annotations_to_cls(cls: object) -> object:
    # Add 
    clsargspec = inspect.getfullargspec(cls)
    cls.__init_args = clsargspec.args[1:]
    cls.__init_annotations = clsargspec.annotations
    return cls



def read_toml(filename: str) -> dict[str]:
    with open(filename, "rb") as toml_handle:
        return tomllib.load(toml_handle)



def _load_arguments(params: list, annotations: dict[str], arguments: dict[str]) -> list:
    return [
        annotations[param](
            *_load_arguments(
                annotations[param].__init_args,
                annotations[param].__init_annotations,
                arguments[param]
            )
        )
        if param in annotations.keys() and hasattr(annotations[param], 'load_from_toml') 
        else arguments[param]
        for param in params
    ]



def toml_init(cls: object):
    toml_dict: dict[str]
    cls = _add_init_args_and_annotations_to_cls(cls)

    @classmethod
    def load_from_toml(cls: object, filename: str) -> object:
        assert hasattr(cls, "__init_args")
        assert hasattr(cls, "__init_annotations")

        if not os.path.exists(filename):
            raise FileNotFoundError(f"Could not locate TOML '{filename}'")

        if not re.search("\.toml$", filename):
            raise tomllib.TOMLDecodeError(f"Expecting file ending in '.toml', received '{filename}'")

        toml: dict[str] = read_toml(filename)

        return cls(*_load_arguments(
            cls.__init_args, 
            cls.__init_annotations,
            toml
        ))


    # Add functions to class
    cls.load_from_toml = load_from_toml
    return cls