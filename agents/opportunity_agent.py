class OpportunityAgent:
    def score(self, property_data, equity, legal):
        score = 70

        if equity["estimated_equity"] > 100000:
            score += 15
        if legal["foreclosure_risk"] == "LOW":
            score += 10

        return {
            "deal_score": score,
            "recommendation": "WHOLESALE / HOLD"
        }
