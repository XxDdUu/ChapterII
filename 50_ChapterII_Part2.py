import os
import base64
from random import *

length = randrange(7, 10)
random_bytes = os.urandom(length)
random_string = base64.b64encode(random_bytes).decode('utf-8')[:length]
print(random_string)


