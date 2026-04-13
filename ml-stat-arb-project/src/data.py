from pathlib import Path
import pandas as pd

def load_prices():
    
    base_path = Path(__file__).resolve().parent.parent

    file_path = base_path / "data" / "processed" / "prices.csv"

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    return pd.read_csv(file_path, index_col=0, parse_dates=True)


def compute_returns(prices):
    return prices.pct_change().dropna()