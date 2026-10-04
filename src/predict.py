
"""
Mission Request Classification - Prediction Script

Educational demonstration using synthetic data.
Not for operational or production use.
"""

from train_model import load_data, build_model
from sklearn.model_selection import train_test_split


def create_trained_model():
    """Train the classifier using the training portion of the dataset."""
    dataset = load_data()

    X_train, _, y_train, _ = train_test_split(
        dataset["description"],
        dataset["category"],
        test_size=0.20,
        random_state=42,
        stratify=dataset["category"]
    )

    model = build_model()
    model.fit(X_train, y_train)

    return model


def triage_request(model, request_text, threshold=0.70):
    """Classify a request and flag uncertain results for review."""
    probabilities = model.predict_proba([request_text])[0]
    best_index = probabilities.argmax()

    category = model.classes_[best_index]
    score = float(probabilities[best_index])

    decision = (
        "HUMAN REVIEW REQUIRED"
        if score < threshold
        else "PROVISIONAL ROUTING SUGGESTION"
    )

    return {
        "request": request_text,
        "predicted_category": category,
        "model_score": round(score, 3),
        "decision": decision
    }


if __name__ == "__main__":
    model = create_trained_model()

    requests = [
        "Review identity access permissions for a protected application",
        "Investigate API integration and database mapping issues",
        "Coordinate deployment rollback after a failed software release",
        "Review the budget, schedule, and staffing requirements",
        "The system is behaving strangely and needs attention"
    ]

    print("MISSION REQUEST CLASSIFICATION RESULTS")
    print("--------------------------------------")

    for request in requests:
        result = triage_request(model, request)

        print()
        print("REQUEST:", result["request"])
        print("PREDICTION:", result["predicted_category"])
        print("MODEL SCORE:", result["model_score"])
        print("DECISION:", result["decision"])
        print("-" * 60)
