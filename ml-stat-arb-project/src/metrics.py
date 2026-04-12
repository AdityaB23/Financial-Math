
import numpy as np

def sharpe(r):
    return np.sqrt(252) * r.mean() / r.std()
