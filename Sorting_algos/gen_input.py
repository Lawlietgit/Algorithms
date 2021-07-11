import numpy as np

def gen_random_array(size, dtype='int'):
    if dtype=='int':
        return np.random.randint(0, 100, size=size)
    elif dtype=='float':
        return np.random.random(size)

