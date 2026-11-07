from smart_health.ai.rules import is_compatible, is_eligible


def test_universal_donor():
    assert is_compatible("O-", "AB+")
    assert is_compatible("O-", "O-")


def test_rh_negative_cannot_receive_positive():
    assert not is_compatible("A+", "A-")
    assert not is_compatible("A+", "O+")


def test_eligibility():
    assert is_eligible(30, 70, 100)
    assert not is_eligible(17, 70, 100)
    assert not is_eligible(30, 49, 100)
    assert not is_eligible(30, 70, 55)
    assert not is_eligible(61, 70, 100)
