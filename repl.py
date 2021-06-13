import re
import sys

import chapter_3 as san

print("\nAVAILABLE MODULES: \n")
for mod in dir(sys.modules[__name__]):
    if (
        re.search("__\w", mod) is None and
        re.search("^(help|sys|re)$", mod) is None
    ):
        print(mod)

