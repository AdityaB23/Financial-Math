
import numpy as np
import pandas as pd

def backtest(predictions, returns):

    signal = np.sign(predictions)
    strategy = signal.shift(1) * returns

    equity = (1+strategy).cumprod()

    sharpe = np.sqrt(252) * strategy.mean()/strategy.std()

    drawdown = equity / equity.cummax() - 1

    return {
        "equity": equity,
        "sharpe": sharpe,
        "drawdown": drawdown.min()
    }
