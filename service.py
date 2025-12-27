from models import QDTParams, qdt_probability


def evaluate_decision(data: dict):
    params = QDTParams(
        p_buy_e1=float(data["p_buy_e1"]),
        p_buy_e2=float(data["p_buy_e2"]),
        alpha=float(data["alpha"]),
        beta=float(data["beta"]),
        theta=float(data["theta"]),
    )

    prob = qdt_probability(params)

    return {
        "probability": round(prob, 4),
        "decision": "BUY" if prob >= 0.5 else "NOT BUY"
    }
