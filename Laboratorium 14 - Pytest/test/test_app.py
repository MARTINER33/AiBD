from app import polly_A
import numpy as np

def test_polly_A():
    wek = np.array([2,2,2,2])
    got = polly_A(wek)
    want = np.array([16.,-32.,24.,-8.,1.])
    assert True ==  (got == want).all()

