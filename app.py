import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier


st.set_page_config(page_title="ML Trading Backtester", layout="wide")

st.title("📈 ML-Powered Trading Strategy Backtester")
st.write("Compare Buy & Hold, Moving Average Crossover, and ML-based trading signals.")


# Sidebar controls
ticker = st.sidebar.text_input("Ticker", value="AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2018-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2024-12-31"))
threshold = st.sidebar.slider("ML Confidence Threshold", 0.50, 0.80, 0.60, 0.05)
transaction_cost = st.sidebar.slider("Transaction Cost", 0.0, 0.005, 0.001, 0.0005)


def load_data(ticker, start, end):
    df = yf.download(ticker, start=start, end=end)
    return df


def create_features(df):
    df = df.copy()
    df["daily_return"] = df["Close"].pct_change()
    df["ma_10"] = df["Close"].rolling(window=10).mean()
    df["ma_50"] = df["Close"].rolling(window=50).mean()
    df["volatility_10"] = df["daily_return"].rolling(window=10).std()
    df["momentum_10"] = df["Close"] / df["Close"].shift(10) - 1
    df["target"] = (df["Close"].shift(-1) > df["Close"]).astype(int)
    df = df.dropna()
    return df


def calculate_metrics(returns, cumulative):
    total_return = cumulative.iloc[-1] - 1
    volatility = returns.std() * np.sqrt(252)

    if returns.std() == 0:
        sharpe = 0
    else:
        sharpe = returns.mean() / returns.std() * np.sqrt(252)

    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_drawdown = drawdown.min()

    return total_return, volatility, sharpe, max_drawdown


if st.sidebar.button("Run Backtest"):
    df = load_data(ticker, start_date, end_date)

    if df.empty:
        st.error("No data found. Check ticker or date range.")
    else:
        df = create_features(df)

        features = [
            "daily_return",
            "ma_10",
            "ma_50",
            "volatility_10",
            "momentum_10"
        ]

        X = df[features]
        y = df["target"]

        split = int(len(df) * 0.8)

        X_train = X.iloc[:split]
        X_test = X.iloc[split:]

        y_train = y.iloc[:split]

        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        proba = model.predict_proba(X_test)[:, 1]

        df_test = df.iloc[split:].copy()
        df_test["prob"] = proba

        # Market return
        df_test["market_return"] = df_test["Close"].pct_change().shift(-1)

        # Buy & Hold
        df_test["buy_hold_return"] = df_test["market_return"]

        # ML strategy
        df_test["ml_position"] = (df_test["prob"] > threshold).astype(int)
        df_test["ml_trade"] = df_test["ml_position"].diff().abs().fillna(0)
        df_test["ml_return"] = (
            df_test["ml_position"] * df_test["market_return"]
            - df_test["ml_trade"] * transaction_cost
        )

        # MA crossover
        df_test["ma_position"] = (df_test["ma_10"] > df_test["ma_50"]).astype(int)
        df_test["ma_trade"] = df_test["ma_position"].diff().abs().fillna(0)
        df_test["ma_return"] = (
            df_test["ma_position"] * df_test["market_return"]
            - df_test["ma_trade"] * transaction_cost
        )

        df_test = df_test.dropna()

        df_test["cum_buy_hold"] = (1 + df_test["buy_hold_return"]).cumprod()
        df_test["cum_ml"] = (1 + df_test["ml_return"]).cumprod()
        df_test["cum_ma"] = (1 + df_test["ma_return"]).cumprod()

        st.subheader(f"Backtest Results for {ticker}")

        bh_metrics = calculate_metrics(df_test["buy_hold_return"], df_test["cum_buy_hold"])
        ml_metrics = calculate_metrics(df_test["ml_return"], df_test["cum_ml"])
        ma_metrics = calculate_metrics(df_test["ma_return"], df_test["cum_ma"])

        metrics_df = pd.DataFrame({
            "Strategy": ["Buy & Hold", "ML Strategy", "MA Crossover"],
            "Total Return": [bh_metrics[0], ml_metrics[0], ma_metrics[0]],
            "Volatility": [bh_metrics[1], ml_metrics[1], ma_metrics[1]],
            "Sharpe Ratio": [bh_metrics[2], ml_metrics[2], ma_metrics[2]],
            "Max Drawdown": [bh_metrics[3], ml_metrics[3], ma_metrics[3]]
        })

        st.dataframe(metrics_df.style.format({
            "Total Return": "{:.2%}",
            "Volatility": "{:.2%}",
            "Sharpe Ratio": "{:.2f}",
            "Max Drawdown": "{:.2%}"
        }))

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df_test.index, df_test["cum_buy_hold"], label="Buy & Hold")
        ax.plot(df_test.index, df_test["cum_ml"], label="ML Strategy")
        ax.plot(df_test.index, df_test["cum_ma"], label="MA Crossover")
        ax.set_title("Strategy Performance Comparison")
        ax.legend()
        st.pyplot(fig)

        st.subheader("Latest Signal Data")
        st.dataframe(df_test[["Close", "prob", "ml_position", "ma_position"]].tail(20))