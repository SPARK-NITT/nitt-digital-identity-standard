from dataclasses import dataclass
import math

@dataclass
class CIInputs:
    info_loss_bits: float = 0.0       # ΔI (illustrative proxy, in bits)
    energy_jump_joules: float = 0.0   # ΔE (illustrative proxy, in J)
    downtime_ms: float = 0.0          # process interruption (ms)
    weights: tuple = (1.0, 1.0, 1.0)  # (wI, wE, wT)
    alpha: float = 1e-6               # sensitivity scalar

def ci_exponential(inputs: CIInputs) -> float:
    """Illustrative aggregator: CI = exp(-alpha * (wI*ΔI + wE*ΔE + wT*Δt))"""
    wI, wE, wT = inputs.weights
    penalty = (wI * inputs.info_loss_bits) + (wE * inputs.energy_jump_joules) + (wT * inputs.downtime_ms)
    return math.exp(-inputs.alpha * penalty)

def ci_from_overlap(overlap_fraction: float) -> float:
    """If someone estimates state overlap (0..1), map to CI (demo proxy)."""
    overlap_fraction = max(0.0, min(1.0, overlap_fraction))
    return overlap_fraction
