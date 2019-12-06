import math
import os
from os import rename

import requests


def greet():
    pass


r = requests.get("https://www.baidu.com")
print(r.status_code)
