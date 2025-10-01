
import plotly.express as px


#tab1 plots
def plot_time_series(df):
    df_time = df.set_index("date").resample("D")["amount"].sum().reset_index()
    fig = px.line(df_time, x="date", y="amount", title="Daily Transaction Totals")
    fig.update_yaxes(tickprefix="$", separatethousands=True)
    return fig

def plot_category_bar(df, top_n=20):
    cat_sum = df.groupby("category", dropna=False)["amount"].sum().sort_values(ascending=False).reset_index()
    if len(cat_sum) > top_n:
        cat_sum = cat_sum.head(top_n)
    fig = px.bar(cat_sum, x="category", y="amount", title="Total Amount by Category")
    fig.update_yaxes(tickprefix="$", separatethousands=True)
    return fig

def plot_transaction_type(df):
    return px.pie(df, names="transaction_type", values="amount", title="Amount by Transaction Type")


#tab 2 plots 
def plot_payment_heatmap(df):
    pivot = df.pivot_table(index="category", columns="payment_method", values="amount", aggfunc="sum", fill_value=0)
    fig = px.imshow(pivot, labels=dict(x="Payment Method", y="Category", color="Total Amount"), aspect="auto", title="Payment Method vs Category")
    return fig

def plot_top_merchants(df, top_n=10):
    merchants = df.groupby("merchant")["amount"].sum().nlargest(top_n).reset_index()
    fig = px.bar(merchants, x="merchant", y="amount", title=f"Top {top_n} Merchants by Amount")
    fig.update_yaxes(tickprefix="$", separatethousands=True)
    return fig
