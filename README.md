# AI Review Analyzer – Problem Design

## 1. Problem
Customers may need to read many product reviews to understand overall feedback. This project proposes a simple AI tool that classifies a short review as **Positive** or **Negative**.

## 2. Intended user
A small online seller who wants to quickly understand customer feedback.

## 3. Data source
A small sample of product reviews created for this project, with positive and negative examples. No personal or private customer information will be used.

## 4. Proposed AI approach
Use a text classification model to predict whether each review is Positive or Negative.

## 5. Constraints and risks
The model may misunderstand jokes, mixed opinions, spelling mistakes, or very short reviews. Predictions may be wrong, so a person should check important decisions.

## 6. Evaluation approach
Test the model on sample reviews with known labels. Compare the predictions with the known labels and count how many are correct. Also record examples where the model makes a mistake.

## 7. Expected result
A simple demonstration of review sentiment classification. The output is an AI prediction, not a guaranteed judgment.
