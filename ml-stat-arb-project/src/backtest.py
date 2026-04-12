
import numpy as np
import pandas as pd

def backtest(preds, returns):

    aligned = returns.loc[preds.index]

    signal = np.sign(preds)
    strat = signal.shift(1) * aligned

    equity = (1+strat).cumprod()

    sharpe = np.sqrt(252) * strat.mean() / strat.std()
    drawdown = (equity / equity.cummax() - 1).min()

    return strat, equity, sharpe, drawdown
