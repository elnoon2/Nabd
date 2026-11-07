"""Clean raw CSVs into data/cleaned."""
import pandas as pd
from smart_health import config


def main():
    config.DATA_CLEAN.mkdir(parents=True, exist_ok=True)
    for name in ["wait_logs", "donors", "blood_requests"]:
        df = pd.read_csv(config.DATA_RAW / f"{name}.csv").drop_duplicates().dropna()
        df.to_csv(config.DATA_CLEAN / f"{name}.csv", index=False)
        print(name, df.shape)


if __name__ == "__main__":
    main()
