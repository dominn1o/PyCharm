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

def aShapedList(n):
    arr = np.random.randint(1, 1000001, size=n)
    arr.sort()
    left_side = arr[::2] #co 2 element
    right_side = arr[1::2][::-1] #reszta elementow, odwrocona
    return np.concatenate([left_side, right_side]) #polaczone tworza gore na srodku


def vShapedList(n):
    arr = np.random.randint(1, 1000001, size=n)
    arr.sort()
    left_side = arr[1::2][::-1]
    right_side = arr[::2]
    return np.concatenate([left_side, right_side])