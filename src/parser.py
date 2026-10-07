import pandas as pd

REQUIRED = {"timestamp", "user", "source_ip", "event_id", "status"}

def load_logs(path):
    df = pd.read_csv(path)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="raise")
    return df
