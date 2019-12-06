import math
import os
from os import rename

import requests



r = requests.get("https://www.baidu.com")
print(r.status_code)
print(r.ok)
