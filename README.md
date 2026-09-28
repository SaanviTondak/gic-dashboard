# Financial Transactions Anomaly Dashboard

An interactive Streamlit dashboard for exploring a financial transactions dataset and flagging unusual transactions. Built as a take-home assignment for GIC's Internal Audit Data Analytics internship application.

## What it does

- **Cleans the data** (`src/data.py`): date parsing, numeric conversion, duplicate removal
- **KPI cards:** total and average spend, transaction count, outlier count
- **Exploration:** daily transaction totals, spend by category, transaction-type mix, payment method x category heatmap, top merchants
- **Anomaly detection** (`src/outliers.py`): IQR rule and Isolation Forest, with flagged transactions plotted over time
- **Interactive:** upload your own CSV, filter by date range, tabbed workflow

## Structure

```
app.py                      Streamlit app
src/data.py                 loading and cleaning
src/plots.py                Plotly chart functions
src/outliers.py             IQR + Isolation Forest
financial_transactions.csv  sample dataset
```

## Run it

```bash
git clone https://github.com/SaanviTondak/gic-dashboard.git
cd gic-dashboard
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Stack: Python 3.9+, Streamlit, pandas, NumPy, Plotly, scikit-learn.
