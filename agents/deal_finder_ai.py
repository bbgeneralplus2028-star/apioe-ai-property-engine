def deal_score(equity, risk):
    score = 50

    if equity["potential_profit"] > 75000:
        score += 30
    if not risk:
        score += 20

    return {
        "deal_score": score,
        "classification": "STRONG BUY"
    }
