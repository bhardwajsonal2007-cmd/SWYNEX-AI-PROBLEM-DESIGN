from textblob import TextBlob


def analyze_review(review):
    score = TextBlob(review).sentiment.polarity

    if score > 0.05:
        label = "Positive"
    elif score < -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return label, round(score, 2)


example_reviews = [
    "I love this product. It works perfectly!",
    "This product is terrible and completely useless."
]

for review in example_reviews:
    sentiment, score = analyze_review(review)
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment} | Score: {score}")
    print()
