import pandas as pd
from src.features import add_features

def test_unusual_hour():
    df = pd.DataFrame([{
        "timestamp": pd.Timestamp("2026-01-01T02:00:00"),
        "user": "student",
        "source_ip": "10.0.0.1",
        "event_id": 4624,
        "status": "success",
    }])
    assert add_features(df).iloc[0]["unusual_hour"] == 1
