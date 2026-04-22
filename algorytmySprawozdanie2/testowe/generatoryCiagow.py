import numpy as np

def randomList(n):
    return np.random.randint(1, 1000001, size=n).tolist()

def growingList(n):
    arr = np.random.randint(1, 1000001, size=n)
    arr.sort()
    return arr.tolist()

def descendingList(n):
    arr = np.random.randint(1, 1000001, size=n)
    arr.sort()
    return arr[::-1]