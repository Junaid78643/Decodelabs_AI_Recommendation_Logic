from recommendation_system import RecommendationEngine, recommend_items


def test_recommend_items_returns_highest_matching_results():
    items = [
        {"name": "AI Projects Handbook", "tags": ["technology", "ai", "learning"]},
        {"name": "Science Discovery Journal", "tags": ["science", "learning", "technology"]},
        {"name": "Outdoor Adventure Guide", "tags": ["travel", "outdoors", "fitness"]},
        {"name": "Beginner Yoga Plan", "tags": ["fitness", "health", "wellness"]},
    ]

    result = recommend_items(["technology", "science"], items)

    assert result[0]["name"] == "Science Discovery Journal"
    assert result[1]["name"] == "AI Projects Handbook"
    assert "Outdoor Adventure Guide" not in [item["name"] for item in result[:2]]


def test_recommendation_engine_handles_empty_preferences():
    items = [
        {"name": "AI Projects Handbook", "tags": ["technology", "ai"]},
        {"name": "Outdoor Adventure Guide", "tags": ["travel", "outdoors"]},
    ]

    engine = RecommendationEngine()
    result = engine.recommend([], items)

    assert result == items
