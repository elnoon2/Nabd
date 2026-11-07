"""Baselines: nearest hospital by distance; nearest compatible donor (straight line); random donor."""
import numpy as np
from smart_health.ai.hospital_search import haversine_km


def nearest_hospital(user_latlon, hospitals):
    return min(hospitals, key=lambda hid: haversine_km(user_latlon, hospitals[hid]["latlon"]))


def nearest_donor(hospital_latlon, eligible_donors):
    """eligible_donors needs lat/lon columns."""
    d = eligible_donors.apply(lambda r: haversine_km(hospital_latlon, (r.lat, r.lon)), axis=1)
    return eligible_donors.loc[[d.idxmin()]]


def random_donor(eligible_donors, seed=0):
    return eligible_donors.sample(1, random_state=seed)
