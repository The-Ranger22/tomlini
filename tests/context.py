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

import tomlini


TEST_DIR: str = os.path.dirname(__file__)