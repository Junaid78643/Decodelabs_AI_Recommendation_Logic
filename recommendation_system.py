"""Simple recommendation system based on user preferences."""

from __future__ import annotations


def _normalize_tags(tags):
    return {tag.strip().lower() for tag in tags if tag and str(tag).strip()}


class RecommendationEngine:
    """Recommend items by matching user interests against item tags."""

    def recommend(self, preferences, items):
        if not preferences:
            return items

        preference_set = _normalize_tags(preferences)
        scored = []

        for item in items:
            item_tags = _normalize_tags(item.get("tags", []))
            match_count = len(preference_set & item_tags)
            if match_count > 0:
                scored.append({**item, "match_count": match_count})

        scored.sort(key=lambda item: item["match_count"], reverse=True)
        return [
            {key: value for key, value in item.items() if key != "match_count"}
            for item in scored
        ]


def recommend_items(preferences, items):
    engine = RecommendationEngine()
    return engine.recommend(preferences, items)


if __name__ == "__main__":
    sample_items = [
        {"name": "AI Projects Handbook", "tags": ["technology", "AI", "learning"]},
        {"name": "Science Discovery Journal", "tags": ["science", "learning", "technology"]},
        {"name": "Outdoor Adventure Guide", "tags": ["travel", "outdoors", "fitness"]},
        {"name": "Beginner Yoga Plan", "tags": ["fitness", "health", "wellness"]},
    ]

    print("Choose your interests separated by commas:")
    user_input = input("Example: technology, science, learning\n> ")
    preferences = [tag.strip() for tag in user_input.split(",") if tag.strip()]

    recommendations = recommend_items(preferences, sample_items)

    if not recommendations:
        print("No strong matches found. Try different interests.")
    else:
        print("\nRecommended for you:")
        for item in recommendations:
            print(f"- {item['name']} ({', '.join(item['tags'])})")
