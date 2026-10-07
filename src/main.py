import argparse
from src.parser import load_logs
from src.features import add_features
from src.detection import rule_score, add_ml_score

def main():
    p = argparse.ArgumentParser(description="Analyze synthetic authentication logs.")
    p.add_argument("--input", default="data/sample_logs.csv")
    args = p.parse_args()

    df = load_logs(args.input)
    df = add_features(df)
    df = rule_score(df)
    df = add_ml_score(df)
    df["priority"] = df["rule_score"] + 2 * df["ml_anomaly"]

    cols = ["timestamp", "user", "source_ip", "event_id", "status",
            "rule_score", "ml_anomaly", "priority"]
    print(df.sort_values("priority", ascending=False)[cols].to_string(index=False))

if __name__ == "__main__":
    main()
