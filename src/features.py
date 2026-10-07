def add_features(df):
    out = df.copy()
    out["hour"] = out["timestamp"].dt.hour
    out["is_failed"] = (out["event_id"].astype(str) == "4625").astype(int)
    out["is_success"] = (out["event_id"].astype(str) == "4624").astype(int)
    out["unusual_hour"] = out["hour"].between(0, 5).astype(int)
    out["ip_event_count"] = out.groupby("source_ip")["source_ip"].transform("size")
    out["user_event_count"] = out.groupby("user")["user"].transform("size")
    return out
