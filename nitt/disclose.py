DISCLOSURE = (
    "This process constitutes termination of the original and creation of a successor. "
    "Identity continuity is partial (CI < 1). The outcome is a branch, not a survival."
)

def disclosure(ci_estimate=None) -> str:
    if ci_estimate is None:
        return DISCLOSURE
    try:
        return f"{DISCLOSURE} (Current proxy estimate: CI ≈ {float(ci_estimate):.3f})"
    except Exception:
        return DISCLOSURE
