
## 🚀 Quick Demo

1. Run the app:
```bash
python -m streamlit run app.py
2. Enter a ticker (e.g., AAPL), set threshold (0.60), click Run Backtest.
3. Compare Buy & Hold vs ML vs MA with risk metrics (Return, Sharpe, Max DD).

📸 See screenshots below.


---

## 📸 2) Pin your best screenshots

Make sure your README shows:
- Metrics table (Sharpe > 1 for ML)
- Strategy comparison chart

---

```md
## 💡 What I Learned
- Directional accuracy alone is insufficient; **risk-adjusted metrics** matter more.
- **Confidence filtering** improves Sharpe by trading only high-signal periods.
- Transaction costs and slippage materially impact naive strategies.



Key Insight

The ML strategy may not always produce the highest total return, but confidence filtering can improve risk-adjusted performance by lowering volatility and drawdowns.

Disclaimer

This project is for educational and research purposes only. It is not financial advice.
