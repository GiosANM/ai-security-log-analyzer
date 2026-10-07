from sklearn.ensemble import IsolationForest

FEATURES = ["hour", "is_failed", "unusual_hour", "ip_event_count", "user_event_count"]

def rule_score(df):
    out = df.copy()
    out["rule_score"] = (
        out["is_failed"]
        + 2 * out["unusual_hour"]
        + (out["ip_event_count"] >= 3).astype(int)
    )
    return out

def add_ml_score(df):
    out = df.copy()
    if len(out) < 5:
        out["ml_anomaly"] = 0
        return out
    model = IsolationForest(random_state=42, contamination="auto")
    prediction = model.fit_predict(out[FEATURES])
    out["ml_anomaly"] = (prediction == -1).astype(int)
    return out
