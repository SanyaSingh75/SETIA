from flask import Flask, request, jsonify
from agents.extractor import extract_issues
from agents.counter import count_issues_by_date
from agents.review_fetcher import fetch_reviews

import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/run-agent", methods=["POST"])
def run_agent():
    data = request.get_json()
    app_id = data.get("app_id")

    if not app_id:
        return jsonify({"error": "App ID missing"}), 400

    os.makedirs("output", exist_ok=True)

    reviews = fetch_reviews(app_id, count=50)
    all_issues = []

    for review in reviews:
        issues = extract_issues(review["text"])
        for issue in issues:
            all_issues.append({
                "issue": issue,
                "date": review["date"]
            })

    counts = count_issues_by_date(all_issues)
    df = pd.DataFrame(counts)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df["generated_at"] = timestamp

    df.to_csv("output/trend.csv", index=False)

    return jsonify({
        "message": "Agent executed successfully",
        "reviews_fetched": len(reviews),
        "issues_found": len(all_issues)
    })

if __name__ == "__main__":
    app.run(debug=True)
