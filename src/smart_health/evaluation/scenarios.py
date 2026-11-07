"""Generate 1,000+ random scenarios, split dev/held-out, compare A* vs baselines."""
import numpy as np
from smart_health import config


def make_scenarios(n=1000, seed=config.SEED):
    rng = np.random.default_rng(seed)
    return [{"hour": int(rng.integers(0, 24)),
             "specialty": str(rng.choice(config.SPECIALTIES)),
             "start_idx": int(rng.integers(0, 10**6))} for _ in range(n)]


def split(scenarios, held_out=0.3, seed=config.SEED):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(scenarios))
    k = int(len(scenarios) * (1 - held_out))
    return [scenarios[i] for i in idx[:k]], [scenarios[i] for i in idx[k:]]


if __name__ == "__main__":
    dev, test = split(make_scenarios())
    print(len(dev), "dev /", len(test), "held-out scenarios")
    # TODO: run recommend_hospital + baselines, save results to data/cleaned/results.csv
