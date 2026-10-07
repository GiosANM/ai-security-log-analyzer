# AI Security Log Analyzer

A student project combining data analysis, machine learning concepts, and SOC log investigation.

## What It Does
The starter pipeline loads sanitized authentication events, creates behavioral features, applies explainable rules, and optionally uses Isolation Forest for anomaly scoring.

## Pipeline
```text
CSV Logs -> Validation -> Feature Engineering -> Rule Score
                                      |
                                      +-> Isolation Forest
                                               |
                                               v
                                        Ranked Alerts
```

## Quick Start
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m src.main --input data/sample_logs.csv
```

## Why This Project
SOC analysts work with large volumes of telemetry. This project demonstrates how Python and ML concepts can assist prioritization while keeping analyst validation in the loop.

## Future Improvements
- Windows EVTX ingestion
- Time-window aggregation
- User behavioral baselines
- Model evaluation metrics
- Streamlit dashboard
- LLM-generated summaries using sanitized alerts

This project is for defensive learning and uses synthetic data.
