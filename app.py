import streamlit as st
import pandas as pd
import plotly.express as px


from src.data import load_data
from src.plots import (
    plot_time_series, plot_category_bar, plot_transaction_type,
    plot_payment_heatmap, plot_top_merchants
)
from src.outliers import detect_outliers_iqr, detect_outliers_isolation_forest

st.set_page_config(page_title="GIC Transactions Dashboard", layout="wide")
st.title("GIC Financial Transactions Dashboard")

#data loadingb
uploaded = st.sidebar.file_uploader("Upload CSV", type=["csv"])
if uploaded:
    df = load_data(uploaded)
else:
    df = load_data("financial_transactions.csv")

#sidebar functions/filters 
min_date, max_date = df["date"].min().date(), df["date"].max().date()
date_range = st.sidebar.date_input("Date range", [min_date, max_date])
start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
df_filtered = df[(df["date"] >= start) & (df["date"] <= end)]

k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Amount", f"${df_filtered['amount'].sum():,.2f}")
k2.metric("Average Amount", f"${df_filtered['amount'].mean():,.2f}")
k3.metric("Transactions", f"{len(df_filtered):,}")

mask_iqr = detect_outliers_iqr(df_filtered)
k4.metric("IQR Outliers", f"{mask_iqr.sum():,}")

# create tabs for different sections
tab1, tab2, tab3 = st.tabs(["Overview", "Merchants & Payments", "Outliers"])


#overview tab
with tab1:
    st.subheader("Data Snapshot")
    st.dataframe(df_filtered.head(20))
    st.subheader("Transaction Amount Summary")
    st.table(df_filtered["amount"].describe().round(2))
    st.plotly_chart(plot_time_series(df_filtered), use_container_width=True)
    st.plotly_chart(plot_category_bar(df_filtered), use_container_width=True)
    st.plotly_chart(plot_transaction_type(df_filtered), use_container_width=True)


#merchants tab
with tab2:
    st.plotly_chart(plot_top_merchants(df_filtered), use_container_width=True)
    st.plotly_chart(plot_payment_heatmap(df_filtered), use_container_width=True)



#outliers tab 
with tab3:
    method = st.selectbox("Outlier Detection Method", ["IQR", "IsolationForest"])


    if method == "IQR":
        mask = detect_outliers_iqr(df_filtered)

        
    else:
        mask = detect_outliers_isolation_forest(df_filtered)
    outliers = df_filtered[mask]
    st.write(f"Detected {len(outliers)} outliers")
    fig = px.scatter(df_filtered, x="date", y="amount",
                     color=mask.map({True: "Outlier", False: "Normal"}),
                     hover_data=["merchant", "category", "payment_method"],
                     title="Outlier Transactions Over Time")
    fig.update_yaxes(tickprefix="$", separatethousands=True)
    st.plotly_chart(fig, use_container_width=True)
