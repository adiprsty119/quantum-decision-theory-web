import math
from dataclasses import dataclass


@dataclass
class QDTParams:
    p_buy_e1: float
    p_buy_e2: float
    alpha: float
    beta: float
    theta: float

    def validate(self):
        if not 0 <= self.p_buy_e1 <= 1:
            raise ValueError("p_buy_e1 must be between 0 and 1")

        if not 0 <= self.p_buy_e2 <= 1:
            raise ValueError("p_buy_e2 must be between 0 and 1")

        if not math.isclose(self.alpha**2 + self.beta**2, 1.0, rel_tol=1e-6):
            raise ValueError("alpha^2 + beta^2 must equal 1")


def qdt_probability(p: QDTParams) -> float:
    p.validate()

    classical = (
        p.alpha**2 * p.p_buy_e1 +
        p.beta**2 * p.p_buy_e2
    )

    interference = (
        2 * p.alpha * p.beta *
        math.sqrt(p.p_buy_e1 * p.p_buy_e2) *
        math.cos(p.theta)
    )

    probability = classical + interference

    # safety clamp
    return max(0.0, min(1.0, probability))
