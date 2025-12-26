def count_issues_by_date(all_issues):
    results = []

    for item in all_issues:
        found = False
        for r in results:
            if r["Issue"] == item["issue"] and r["Date"] == item["date"]:
                r["Count"] += 1
                found = True
                break

        if not found:
            results.append({
                "Issue": item["issue"],
                "Date": item["date"],
                "Count": 1
            })

    return results

