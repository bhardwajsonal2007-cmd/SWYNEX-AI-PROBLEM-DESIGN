# AI Review Analyzer

A beginner-friendly prototype that classifies short product reviews as **Positive**, **Negative**, or **Neutral**.

## Problem

A small online seller may receive many product reviews and want a quick summary of customer sentiment. This prototype gives each review one sentiment label.

## Method

The prototype uses the TextBlob Python library's built-in sentiment analyzer. It calculates a polarity score and applies these rules:

- Score above `0.05` → Positive
- Score below `-0.05` → Negative
- Otherwise → Neutral

No API key is needed. The sample reviews are illustrative examples, not private customer data.

## Project files

- `task2_sentiment.py` — basic review-analysis prototype with example inputs.
- `task3_evaluation.py` — evaluation examples, edge cases, empty-input handling, and an interactive review prompt.
- `requirements.txt` — the TextBlob dependency.

## Run the prototype

Install Python 3, then run these commands from the project folder:

```text
python -m pip install -r requirements.txt
python task2_sentiment.py
python task3_evaluation.py
