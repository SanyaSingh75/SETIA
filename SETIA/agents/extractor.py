def extract_issues(review):
    review = review.lower()
    issues = []

    if "late" in review or "delay" in review:
        issues.append("Delivery late")

    if "cold" in review or "stale" in review:
        issues.append("Food cold")

    if "rude" in review or "bad" in review:
        issues.append("Delivery person rude")

    return issues

