
import pandas as pd
import numpy as np

def create_features(returns):
    df = pd.DataFrame(index=returns.index)

    for col in returns.columns:
        df[f"{col}_ret"] = returns[col]
        for lag in [1,2,5]:
            df[f"{col}_lag{lag}"] = returns[col].shift(lag)

        df[f"{col}_vol20"] = returns[col].rolling(20).std()
        df[f"{col}_mom20"] = (1+returns[col]).rolling(20).apply(lambda x: x.prod())

    df["bond_spread"] = returns["TLT"] - returns["SHY"]

    return df.dropna()
