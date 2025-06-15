# 🧠 Crypto Trend Predictor with AI




---

## 🌍 Live Demo

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live-%23FF4B4B?logo=streamlit&logoColor=white)](https://crypto-trend-predictor-4bgnnmgyyhwf4otqrhc6vf.streamlit.app/)

👉 Try it out: [crypto-trend-predictor.streamlit.app](https://crypto-trend-predictor-4bgnnmgyyhwf4otqrhc6vf.streamlit.app/)

---



This project uses RSI (Relative Strength Index) and Fibonacci retracement zones to predict short-term Bitcoin price movements using machine learning — including XGBoost and a Streamlit dashboard.

---

## 🔍 Features

- 📉 Technical indicators: RSI & Fibonacci Golden Zone logic
- 🤖 ML Models: Logistic Regression & XGBoost
- 📊 Visualization: RSI/Fib charts with Matplotlib
- 🌐 Streamlit Dashboard: Interactive web app for live predictions

---

## 🚀 Try the Dashboard (Locally)

```bash
streamlit run app.py
```

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `CryptoTrendClassifier_Complete.ipynb` | Full notebook: RSI, Fib, XGBoost, visuals |
| `app.py` | Streamlit dashboard for predictions |
| `xgb_crypto_model.pkl` | Saved ML model |
| `.gitignore` | Excludes large files like raw CSVs |
| `btc_sample.csv` | Small BTC dataset (if added) |

---

## 📈 Sample Dashboard

*(Add a screenshot named `screenshot.png`)*  
![Streamlit Screenshot](screenshot.png)

---

## 💡 Usage Example

Once the app is running:

- Select RSI value using slider
- Choose if price is in Fibonacci golden zone
- Enter daily return %
- Click **Predict** → Instant trend prediction

---

## 🧠 Author

**Haris Papadopoulos**  
Stuttgart, Germany  
AI & Blockchain Engineer in progress  
[GitHub](https://github.com/sysops-cpu)

---

## 📎 Optional Enhancements

- Add `btc_sample.csv` for demo/testing
- Deploy to [Streamlit Cloud](https://streamlit.io/cloud)
- Add CI badge with GitHub Actions
