
import pandas as pd
import numpy as np

def create_features(returns):

    df = returns.copy()

    for lag in [1,2,5]:
        df[f"lag_{lag}"] = returns.shift(lag)

    vol = returns.rolling(20).std()
    df["vol"] = vol

    momentum = (1+returns).rolling(20).apply(lambda x: x.prod())
    df["momentum"] = momentum

    df["bond_spread"] = returns["TLT"] - returns["SHY"]

    return df.dropna()
