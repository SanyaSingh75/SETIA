from agents.extractor import extract_issues
from agents.counter import count_issues_by_date
from agents.review_fetcher import fetch_reviews

import pandas as pd
import os
from datetime import datetime

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# Ask user for app id
app_id = input("Enter Google Play App ID (example: in.swiggy.android): ")

# Fetch real reviews
reviews = fetch_reviews(app_id, count=50)

all_issues = []

for review in reviews:
    issues = extract_issues(review["text"])
    for issue in issues:
        all_issues.append({
            "issue": issue,
            "date": review["date"]
        })

print("Number of reviews fetched:", len(reviews))
print("Number of issues extracted:", len(all_issues))

# Count issues date-wise
counts = count_issues_by_date(all_issues)

# Convert to DataFrame (df is CREATED HERE)
df = pd.DataFrame(counts)

# Add generation timestamp AFTER df exists
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
df["generated_at"] = timestamp

# Save output (overwrite every run)
df.to_csv("output/trend.csv", index=False)

print("File updated at:", timestamp)
print("Done! Check output/trend.csv")
