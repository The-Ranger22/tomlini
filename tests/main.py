from context import tomlini, TEST_DIR
from tomlini import toml_init

@toml_init
class MyClass2:
    def __init__(self, v1, dictionary):
        self.v1 = v1
        self.dictionary = dictionary

@toml_init
class MyClass:
    v1: int
    v2: str
    def __init__(self, v1, v2, myobj: MyClass2):
        self.v1 = v1
        self.v2 = v2
        self.myobj = myobj

    def func(self):
        print("aaa")

if __name__ == "__main__":
    mc = MyClass.load_from_toml(
        "/".join([TEST_DIR,"test.toml"])
    )
    print(mc.v1, mc.v2, mc.myobj.v1, mc.myobj.dictionary)


    