
"""
Automated tests for the synthetic mission request ML demo.

Run using:
    python -m pytest tests/test_model.py -v
"""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from train_model import load_data, build_model
from predict import triage_request


@pytest.fixture(scope="module")
def trained_model():
    """Create a small fitted model for testing."""
    dataset = load_data()
    model = build_model()

    model.fit(
        dataset["description"],
        dataset["category"]
    )

    return model


def test_dataset_has_expected_columns():
    dataset = load_data()

    assert "description" in dataset.columns
    assert "category" in dataset.columns


def test_dataset_contains_320_records():
    dataset = load_data()

    assert len(dataset) == 320


def test_dataset_contains_four_categories():
    dataset = load_data()

    assert dataset["category"].nunique() == 4


def test_model_can_make_prediction(trained_model):
    prediction = trained_model.predict([
        "Review identity access permissions"
    ])

    assert len(prediction) == 1
    assert prediction[0] in trained_model.classes_


def test_triage_returns_required_fields(trained_model):
    result = triage_request(
        trained_model,
        "Review identity access permissions"
    )

    assert "request" in result
    assert "predicted_category" in result
    assert "model_score" in result
    assert "decision" in result


def test_model_score_is_valid(trained_model):
    result = triage_request(
        trained_model,
        "Investigate API integration problems"
    )

    assert 0.0 <= result["model_score"] <= 1.0


def test_high_threshold_requires_review(trained_model):
    result = triage_request(
        trained_model,
        "Review application access permissions",
        threshold=1.0
    )

    assert result["decision"] == "HUMAN REVIEW REQUIRED"


def test_zero_threshold_allows_provisional_routing(trained_model):
    result = triage_request(
        trained_model,
        "Coordinate software deployment",
        threshold=0.0
    )

    assert result["decision"] == "PROVISIONAL ROUTING SUGGESTION"
