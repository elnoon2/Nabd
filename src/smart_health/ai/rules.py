"""Rule-based reasoning: ABO/Rh compatibility and donor eligibility."""
from smart_health import config

# recipient ABO -> donor ABO groups that are compatible
_ABO = {"O": {"O"}, "A": {"A", "O"}, "B": {"B", "O"}, "AB": {"A", "B", "AB", "O"}}


def _split(bt: str):
    return bt[:-1], bt[-1]


def is_compatible(donor_type: str, recipient_type: str) -> bool:
    d_abo, d_rh = _split(donor_type)
    r_abo, r_rh = _split(recipient_type)
    if d_abo not in _ABO[r_abo]:
        return False
    return not (d_rh == "+" and r_rh == "-")


def is_eligible(age, weight_kg, days_since_donation, available=True) -> bool:
    lo, hi = config.DONOR_AGE_RANGE
    return bool(available and lo <= age <= hi
                and weight_kg >= config.DONOR_MIN_WEIGHT_KG
                and days_since_donation >= config.MIN_DAYS_BETWEEN_DONATIONS)


def filter_donors(donors, requested_type: str):
    """donors: DataFrame. Returns the eligible + compatible subset."""
    mask = donors.apply(lambda r: is_compatible(r.blood_type, requested_type) and
                        is_eligible(r.age, r.weight_kg, r.days_since_donation, bool(r.available)), axis=1)
    return donors[mask]
