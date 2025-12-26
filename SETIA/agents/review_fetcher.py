from google_play_scraper import reviews, Sort

def fetch_reviews(app_id, count=50):
    result, _ = reviews(
        app_id,
        lang="en",
        country="in",
        sort=Sort.NEWEST,
        count=count
    )

    review_list = []

    for r in result:
        review_list.append({
            "text": r["content"],
            "date": r["at"].strftime("%Y-%m-%d")
        })

    return review_list
