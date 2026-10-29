from textblob import TextBlob


def analyze_review(review):
    if not isinstance(review, str) or not review.strip():
        return {
            "sentiment": "Error",
            "score": None,
            "message": "Please enter a non-empty review."
        }

    try:
        score = TextBlob(review.strip()).sentiment.polarity
    except Exception:
        return {
            "sentiment": "Error",
            "score": None,
            "message": "The review could not be analyzed."
        }

    if score > 0.05:
        label = "Positive"
    elif score < -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return {
        "sentiment": label,
        "score": round(score, 2),
        "message": None
    }


def run_evaluation():
    examples = [
        ("I love this product. It works perfectly!", "Positive"),
        ("This product is terrible and completely useless.", "Negative"),
        ("The quality is excellent and delivery was fast.", "Positive"),
        ("The product is poor and very disappointing.", "Negative")
    ]

    correct = 0
    print("MODEL EVALUATION")

    for review, expected in examples:
        result = analyze_review(review)
        predicted = result["sentiment"]

        if predicted == expected:
            correct += 1

        print(f"Review: {review}")
        print(f"Expected: {expected} | Predicted: {predicted}")
        print()

    accuracy = correct / len(examples) * 100
    print(f"Accuracy on these examples: {accuracy:.0f}%")
    print()


def inspect_edge_cases():
    cases = [
        ("Great, it broke after one day.", "Possible sarcasm"),
        ("The design is nice but the battery is awful.", "Mixed opinion")
    ]

    print("EDGE CASES TO INSPECT")

    for review, reason in cases:
        result = analyze_review(review)
        print(f"Review: {review}")
        print(f"Why it is difficult: {reason}")
        print(f"Model prediction: {result['sentiment']} | Score: {result['score']}")
        print()


def run_demo():
    review = input("Type a product review (or press Enter to test empty-input handling): ")
    result = analyze_review(review)

    if result["message"]:
        print(result["message"])
    else:
        print(f"Prediction: {result['sentiment']} | Score: {result['score']}")


if __name__ == "__main__":
    run_evaluation()
    inspect_edge_cases()
    run_demo()
