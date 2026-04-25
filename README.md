# ML-Powered Algorithmic Trading Backtester
## Overview
This project is an interactive Streamlit app that compares Buy & Hold, Moving Average Crossover, and ML-based trading strategies using historical market data.

## Features
- Download market data using yfinance
- Create technical indicators and ML features
- Train Random Forest trading signal model
- Apply confidence-based ML trade filtering
- Include transaction costs
- Compare strategy performance
- Calculate return, volatility, Sharpe ratio, and max drawdown

## Strategies Compared
1. Buy & Hold
2. Moving Average Crossover
3. ML Confidence-Filtered Strategy

## Tech Stack
- Python
- pandas
- scikit-learn
- yfinance
- Streamlit
- matplotlib

## How to Run
```bash
pip install -r requirements.txt
python -m streamlit run app.py

Key Insight

The ML strategy may not always produce the highest total return, but confidence filtering can improve risk-adjusted performance by lowering volatility and drawdowns.

Disclaimer

This project is for educational and research purposes only. It is not financial advice.
