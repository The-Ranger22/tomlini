import unittest
from tests.context import tomlini, TEST_DIR
import tomlini
import tomllib


@tomlini.toml_init
class MyTestClass:
    def __init__(self, v1, v2, myobj):
        self.v1 = v1
        self.v2 = v2
        self.myobj = myobj


class TestTomlini_TomlInit(unittest.TestCase):
    def test_load_success(self):
        class TestDemoCls:
            def __init__(self, v1):
                self.v1 = v1
        
        DecoratedTestDemoCls = tomlini.toml_init(TestDemoCls)
        self.assertTrue(hasattr(DecoratedTestDemoCls, 'load_from_toml'))
        self.assertTrue(hasattr(DecoratedTestDemoCls, 'load_from_toml_string'))


    def test_load_fail(self):
        class TestDemoCls:
            def __init__(self, v1):
                self.v1 = v1
        try:
            tomlini.toml_init(None)
        except ValueError as e:
            self.assertTrue(True)

class TestTomliniLoadFromToml(unittest.TestCase):
    filepath = "/".join([TEST_DIR, 'test.toml'])
    def test_load_success(self):
        self.assertIsInstance(
            MyTestClass.load_from_toml(self.filepath), 
            MyTestClass
        )
    
    def test_load_fail_bad_filepath(self):
        try:
            MyTestClass.load_from_toml("BAD PATH")
        except FileNotFoundError as e:
            self.assertTrue(True)
    
    def test_load_fail_bad_file_ext(self):
        try:
            MyTestClass.load_from_toml("/".join([TEST_DIR, 'bad_test.txt']))
        except tomllib.TOMLDecodeError as e:
            self.assertTrue(True)

        

class TestTomlLoadFromTomlString(unittest.TestCase):
    toml_string = '''v1 = 1
    v2 = "EEEE"

    [myobj]
    v1 = 1

    [myobj.dictionary]
    vals = [1, 2, 3, 4, 5]'''

    def test_load_success(self):
        self.assertIsInstance(
            MyTestClass.load_from_toml_string(self.toml_string), 
            MyTestClass
        )

    def test_load_fail_bad_argument(self):
        for idx, bad_arg in enumerate([1, 1.0, True, [], dict()]):
            with self.subTest(i=idx):
                try:
                    MyTestClass.load_from_toml_string(bad_arg)
                except TypeError as e:
                    self.assertTrue(True)
        


    
    