import numpy as np

class Reader(object):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename) as f:
            lines = f.readlines()
            x, y = [], []
            for line in lines:
                a, b = list(map(float, line.strip().split()))
                x.append(a)
                y.append(b)
            return np.array(x), np.array(y)

