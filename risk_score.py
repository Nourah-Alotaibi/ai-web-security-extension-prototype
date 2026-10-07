def calculate_risk_score(vulns):
    scores = []
    for v in vulns:
        name = v.get("alert", "Unnamed Issue")
        gain = 5  # placeholder for threat impact
        effort = 1  # placeholder for exploit difficulty
        score = gain / effort
        scores.append((name, score))
    return sorted(scores, key=lambda x: x[1], reverse=True)
