def recommend(mood):

    suggestions = {
        "happy": [
            "Work on creative projects",
            "Exercise"
        ],
        "sad": [
            "Listen to music",
            "Take a walk"
        ],
        "neutral": [
            "Focus on your goals",
            "Drink water"
        ]
    }

    return suggestions.get(mood, [])