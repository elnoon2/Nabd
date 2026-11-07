from smart_health.data.generate_data import gen_donors, gen_wait_logs


def test_reproducible():
    assert gen_donors(50).equals(gen_donors(50))


def test_wait_logs_shape():
    df = gen_wait_logs(10, n=100)
    assert df.shape == (100, 9) and (df.wait_minutes > 0).all()
