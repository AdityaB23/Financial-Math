# 🚀 Machine Learning Statistical Arbitrage (Production-Grade)

## Overview
This project implements a production-style quantitative research pipeline for building and evaluating statistical arbitrage strategies using machine learning on financial time-series data.

The focus is on:
- predictive modelling  
- robust backtesting  
- handling non-stationary data  
- reproducible research workflows  

---

## 🎯 Objective
To develop data-driven trading signals that predict short-term returns across liquid ETFs and evaluate them using realistic backtesting.

---

## 🧠 Key Features

### ✔ End-to-End ML Pipeline
- Data ingestion → Feature engineering → Model training → Backtesting → Evaluation

### ✔ Walk-Forward Validation
- Rolling training window  
- Strict out-of-sample evaluation  
- Avoids lookahead bias  

### ✔ Multi-Asset Feature Engineering
- Lagged returns  
- Rolling volatility  
- Momentum signals  
- Cross-asset spreads (e.g. bond term structure: TLT − SHY)

### ✔ Machine Learning Models
- Ridge regression (baseline)
- Random Forest (non-linear benchmark)

### ✔ Backtesting Framework
- Signal generation from predictions  
- Strategy returns calculation  
- Performance metrics:
  - Sharpe ratio  
  - Maximum drawdown  
  - Equity curve  

---

## 📊 Example Output

Typical outputs include:
- Equity curve  
- Sharpe ratio  
- Drawdown statistics  

This allows for rapid iteration and model comparison.

---

## 📁 Project Structure

ml_stat_arb/
│
├── src/
│   data.py          # data ingestion
│   features.py      # feature engineering
│   models.py        # ML models
│   walkforward.py   # rolling training
│   backtest.py      # strategy evaluation
│
├── notebooks/
│   full_pipeline.ipynb   # end-to-end workflow
│
├── configs/
│   config.yaml
│
└── results/

---

## ⚙️ Methodology

### 1. Data
- Daily ETF data (SPY, QQQ, TLT, IEF, SHY, etc.)
- Returns computed from adjusted close prices  

### 2. Feature Engineering
Features include:
- Lagged returns (t−1, t−2, t−5)
- Rolling volatility (20-day)
- Momentum (20-day cumulative return)
- Cross-asset spreads (fixed income signals)

---

### 3. Model Training

We model:
r_(t+1) = f(X_t)

Using:
- Linear models (Ridge)
- Tree-based models (Random Forest)

---

### 4. Walk-Forward Validation

For each time step:
- Train on past data  
- Predict next observation  
- Move forward  

This simulates live trading conditions.

---

### 5. Backtesting

Trading signal:
w_t = sign(r̂_(t+1))

Strategy returns:
r_strategy_t = w_(t-1) * r_t

Metrics:
- Sharpe ratio  
- Drawdown  
- Cumulative returns  

---

## 📈 Results Interpretation

The goal is not just high returns, but:
- stability  
- robustness  
- consistency out-of-sample  

Particular attention is paid to:
- overfitting  
- signal decay  
- non-stationarity  

---

## ⚠️ Key Considerations

- Financial time-series are non-stationary
- Overfitting is a major risk → mitigated via walk-forward validation
- Transaction costs are not yet included (can be added)
- Signals are simple and meant as a research baseline

---

## 🚀 Future Improvements

- Add transaction cost modelling  
- Include intraday / higher-frequency data  
- Extend to classification (direction prediction)  
- Incorporate advanced models (XGBoost, LSTM)  
- Apply to electricity / energy markets  

---

## 💡 Motivation

This project reflects how quantitative trading models are developed in practice:
- iterative experimentation  
- disciplined validation  
- strong focus on robustness  

---

## 🧾 Author

Aditya Bawane  
PhD, Mathematical Physics  
Quantitative Research | Machine Learning | Time Series  
