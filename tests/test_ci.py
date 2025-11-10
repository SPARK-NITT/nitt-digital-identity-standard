from nitt.ci import CIInputs, ci_exponential

def test_ci_monotone():
    base = ci_exponential(CIInputs(0,0,0))
    worse = ci_exponential(CIInputs(1e9,0,0))
    assert worse < base
