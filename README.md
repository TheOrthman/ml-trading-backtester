# 📈 ML-Powered Algorithmic Trading Backtester

## 🚀 Overview

This project is an interactive trading strategy backtester that compares **Buy & Hold**, **Moving Average Crossover**, and a **Machine Learning-based trading strategy** using historical market data.

The system evaluates not just returns, but **risk-adjusted performance**, incorporating real-world constraints such as transaction costs and signal confidence filtering.

---

## 🎯 Objective

To answer a key question in quantitative finance:

> Can machine learning improve trading decisions compared to traditional strategies when evaluated under realistic market conditions?

---

## 🧠 Key Features

- Download historical market data using `yfinance`
- Feature engineering with financial indicators (returns, volatility, momentum)
- Train a **Random Forest classifier** to predict price direction
- Apply **confidence-based filtering** to trading signals
- Simulate trading with **transaction costs**
- Compare strategies using:
  - Total Return
  - Volatility
  - Sharpe Ratio
  - Maximum Drawdown
- Interactive **Streamlit dashboard**

---

## ⚙️ Strategies Compared

### 1. Buy & Hold
- Baseline strategy
- Invest and hold throughout the period

### 2. Moving Average Crossover
- Buy when short-term MA > long-term MA
- Traditional technical strategy

### 3. ML Strategy (Confidence-Filtered)
- Predict next-day direction using ML
- Only trade when model confidence exceeds threshold
- Reduces noise and improves decision quality

---

## 📊 Example Results

| Strategy | Return | Sharpe | Max Drawdown |
|--------|--------|--------|-------------|
| Buy & Hold | Highest | Moderate | Higher |
| MA Strategy | Moderate | ~1.0 | Medium |
| ML Strategy | Lower | **Highest (~1.0+)** | **Lowest** |

👉 **Key Insight:**  
The ML strategy does not always maximize returns, but delivers **superior risk-adjusted performance**, making it effective for **risk management**.

---

## 🧪 Methodology

### Data
- Source: Yahoo Finance (`yfinance`)
- Features:
  - Daily returns
  - Moving averages (10, 50)
  - Volatility (rolling std)
  - Momentum

### Model
- Random Forest Classifier
- Target: Predict next-day price direction

### Backtesting
- Train/test split (time-series aware)
- No look-ahead bias
- Includes transaction costs
- Confidence threshold filtering

---

## 🖥️ Streamlit App

The project includes an interactive web app.

### Features
- Input ticker (e.g., AAPL, TSLA)
- Select date range
- Adjust ML confidence threshold
- Set transaction cost
- Run backtest instantly
- Visualize performance and metrics

### Run Locally

```bash
pip install -r requirements.txt
python -m streamlit run app.py


📸 Demo
App Interface

Strategy Comparison

💡 Key Learnings
Predicting market direction is difficult; accuracy alone is not enough
Risk-adjusted metrics (Sharpe, drawdown) are more meaningful than raw returns
Confidence filtering significantly improves ML strategy performance
Traditional strategies can outperform ML in trending markets, but ML can reduce risk
⚠️ Disclaimer

This project is for educational and research purposes only.
It does not constitute financial advice or a production trading system.

👤 Author

Data Scientist focused on building real-world, decision-driven ML systems in finance and operations.
