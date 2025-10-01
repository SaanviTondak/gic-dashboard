import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_outliers_iqr(df):
    q1 = df["amount"].quantile(0.25)
    q3 = df["amount"].quantile(0.75)
    iqr = q3 - q1
    mask = (df["amount"] < q1 - 1.5 * iqr) | (df["amount"] > q3 + 1.5 * iqr)
    return mask


def detect_outliers_isolation_forest(df):
    X = np.log1p(df[["amount"]])  # log transform
    iso = IsolationForest(contamination=0.02, random_state=42)
    preds = iso.fit_predict(X)
    return pd.Series(preds == -1, index=df.index)
