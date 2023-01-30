import os
import sys

sys.path.insert(
    0, 
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            '..'
        )
    )
)



TEST_DIR: str = os.path.dirname(__file__)