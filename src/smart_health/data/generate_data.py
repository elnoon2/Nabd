"""Seeded synthetic data generator. Justify every parameter in docs/simulation_parameters.md."""
import numpy as np
import pandas as pd
from smart_health import config

# Approximate ABO/Rh frequencies: REPLACE with a cited source.
BLOOD_FREQ = {"O+": .37, "A+": .34, "B+": .17, "AB+": .05,
              "O-": .02, "A-": .03, "B-": .01, "AB-": .01}


def gen_wait_logs(n_hospitals: int, n=15000, rng=None):
    rng = rng or np.random.default_rng(config.SEED)
    hour = rng.integers(0, 24, n)
    specialty = rng.choice(config.SPECIALTIES, n)
    severity = rng.integers(1, 6, n)
    peak = ((hour >= 9) & (hour <= 20)).astype(int)
    patients = rng.poisson(8 + 6 * peak, n)
    base = rng.gamma(shape=2.0, scale=10.0, size=n)
    wait = base * (1 + 0.04 * patients) * (1 + 0.1 * ((hour >= 17) & (hour <= 21))) / (1 + 0.1 * (severity - 1))
    return pd.DataFrame({
        "hospital_id": rng.integers(0, n_hospitals, n), "day": rng.integers(0, 7, n),
        "hour": hour, "specialty": specialty, "severity": severity,
        "patients_present": patients, "wait_minutes": wait.round(1),
        "is_peak": peak, "blood_stock_level": rng.integers(0, 4, n),
    })


def gen_donors(n=2000, n_nodes=1000, rng=None):
    rng = rng or np.random.default_rng(config.SEED + 1)
    types, p = zip(*BLOOD_FREQ.items())
    return pd.DataFrame({
        "donor_id": range(n),
        "blood_type": rng.choice(types, n, p=np.array(p) / sum(p)),
        "age": rng.integers(16, 70, n),
        "weight_kg": rng.normal(75, 15, n).clip(40, 130).round(1),
        "area_node": rng.integers(0, n_nodes, n),
        "days_since_donation": rng.integers(0, 400, n),
        "available": rng.random(n) < 0.7,
        "response_prob": rng.beta(4, 3, n).round(2),
    })


def gen_requests(n_hospitals: int, n=1500, rng=None):
    rng = rng or np.random.default_rng(config.SEED + 2)
    types, p = zip(*BLOOD_FREQ.items())
    return pd.DataFrame({
        "request_id": range(n), "hospital_id": rng.integers(0, n_hospitals, n),
        "blood_type": rng.choice(types, n, p=np.array(p) / sum(p)),
        "hour": rng.integers(0, 24, n), "units": rng.integers(1, 5, n),
        "urgency": rng.integers(1, 4, n),
    })


if __name__ == "__main__":
    config.DATA_RAW.mkdir(parents=True, exist_ok=True)
    nh = 100
    gen_wait_logs(nh).to_csv(config.DATA_RAW / "wait_logs.csv", index=False)
    gen_donors().to_csv(config.DATA_RAW / "donors.csv", index=False)
    gen_requests(nh).to_csv(config.DATA_RAW / "blood_requests.csv", index=False)
    print("Synthetic data written to", config.DATA_RAW)
