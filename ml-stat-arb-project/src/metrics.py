
import numpy as np

def sharpe(r):
    return np.sqrt(252)*r.mean()/r.std()

def max_drawdown(equity):
    return (equity/equity.cummax()-1).min()
