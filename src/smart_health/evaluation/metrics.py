import numpy as np


def mean_time_reduction(baseline, ours):
    baseline, ours = np.asarray(baseline), np.asarray(ours)
    return 1 - ours.mean() / baseline.mean()


def fulfilment_rate(minutes, limit=45):
    return float((np.asarray(minutes) <= limit).mean())
