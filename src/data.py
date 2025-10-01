import pandas as pd

def load_data(path_or_buffer):
    df = pd.read_csv(path_or_buffer, parse_dates=["date"], infer_datetime_format=True)
    if "transaction_id" in df.columns:
        df = df.drop_duplicates(subset=["transaction_id"]) #remove duplicate transaction 
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce") #invalids become NaN
    df["date"] = pd.to_datetime(df["date"], errors="coerce") #invalids become NaT
    df = df.dropna(subset=["date", "amount"])
    return df.reset_index(drop=True)
