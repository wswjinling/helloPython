import numpy as np


def new_func():
    msg = "Roll a dice!"
    return msg


msg = new_func()
print(msg)

print(np.random.randint(1, 9))
