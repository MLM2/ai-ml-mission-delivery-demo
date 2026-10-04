
"""
Mission Request ML Classifier - Training Script

Educational demonstration using synthetic mission requests.
Not intended for operational or production use.
"""

from pathlib import Path

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


# STEP 1: Locate the project and dataset.
ROOT = Path(__file__).resolve().parents[1]

DATA_FILE = ROOT / "data" / "synthetic_requests.csv"


# STEP 2: Load and validate the dataset.
def load_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATA_FILE}"
        )

    dataset = pd.read_csv(DATA_FILE)

    required_columns = {"description", "category"}

    if not required_columns.issubset(dataset.columns):
        raise ValueError(
            "Dataset must contain description and category columns."
        )

    dataset = dataset.dropna(
        subset=["description", "category"]
    )

    if dataset.empty:
        raise ValueError("Dataset contains no usable records.")

    return dataset


# STEP 3: Create the machine-learning pipeline.
def build_model():
    return Pipeline([
        (
            "tfidf",
            TfidfVectorizer()
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000,
                random_state=42
            )
        )
    ])


# STEP 4: Train and evaluate the model.
def train_and_evaluate():
    dataset = load_data()

    X = dataset["description"]
    y = dataset["category"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    model = build_model()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("MISSION REQUEST ML TRAINING RESULTS")
    print("-----------------------------------")

    print("Total records:", len(dataset))
    print("Training records:", len(X_train))
    print("Testing records:", len(X_test))

    print(f"Accuracy: {accuracy:.2%}")

    print()
    print("CLASSIFICATION REPORT")
    print(
        classification_report(
            y_test,
            predictions,
            zero_division=0
        )
    )

    return model


# STEP 5: Run the training program.
if __name__ == "__main__":
    train_and_evaluate()
