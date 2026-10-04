
# Model Card: Mission Request Classification Prototype

## 1. Model Overview

**Project:** AI/ML Mission Delivery Demonstration

**Model type:** TF-IDF text vectorization with logistic regression

**Framework:** Python and scikit-learn

**Development status:** Educational prototype

**Operational status:** Not deployed; not authorized for production use

### Purpose

Demonstrate how a machine-learning classifier could support
initial triage of fictional mission-support requests.

The model predicts one of four categories:

- Data Integration
- Deployment Support
- Model Evaluation
- Security Review

Predictions are advisory and do not replace human decisions.

## 2. Training Data

The project uses 320 synthetic request records generated
specifically for this demonstration.

Each record includes a request description and category label.

The dataset contains 80 records per category.

No operational government data, classified information,
or real personal information is required.

### Dataset limitations

- Synthetic descriptions use repetitive patterns.
- The dataset does not represent actual mission traffic.
- Training and testing records come from the same generator.
- Performance may be inflated by similar wording across records.
- The dataset does not establish real-world generalization.

## 3. Training Method

The classifier uses:

1. TF-IDF to represent text numerically.
2. Logistic regression for category classification.
3. A stratified 80/20 train/test split.
4. A fixed random seed for reproducibility.

Training records: 256

Testing records: 64

The standalone training script is located at:

`src/train_model.py`

## 4. Evaluation

Evaluation methods include:

- Accuracy
- Precision
- Recall
- F1 score
- Classification report

The original Colab experiment achieved 100% accuracy
on its 64-record synthetic holdout.

This result should not be interpreted as evidence
of operational performance.

The standalone training script independently executes
the training and evaluation workflow.

Automated testing has also been completed:

- 8 tests passed
- 0 tests failed

These tests validate selected software behaviors.
They do not establish model reliability or security.

## 5. Human Oversight

The prediction script returns:

- Original request
- Predicted category
- Model score
- Routing decision

An illustrative threshold of 0.70 is used.

Scores below the threshold produce:

`HUMAN REVIEW REQUIRED`

Other scores produce:

`PROVISIONAL ROUTING SUGGESTION`

The threshold is not validated or optimized.

The model scores have not been calibrated and
must not be treated as verified probabilities
of correctness.

Even high-scoring predictions may be wrong.

## 6. Intended Uses

- Educational ML lifecycle demonstration
- Technical program management discussions
- Synthetic-data experimentation
- Prototype evaluation and test planning
- Human-in-the-loop workflow illustration

## 7. Out-of-Scope Uses

The prototype must not be used for:

- Operational national security decisions
- Personnel screening or vetting
- Security adjudication
- Automated access-control decisions
- Production incident or mission routing
- Decisions involving classified information

## 8. Risks and Limitations

### Model risk

The classifier may produce incorrect or misleading
categories for unfamiliar requests.

### Data risk

Synthetic training data does not capture the full
complexity of operational language.

### Confidence risk

The model's reported score is not a calibrated
measure of correctness.

### Automation risk

Automated routing could create delays or errors
if used without appropriate review and controls.

### Security risk

The prototype has not undergone a formal
security assessment or authorization process.

## 9. Required Work Before Operational Consideration

Any future operational version would require:

- Representative and appropriately governed data
- Independent validation and evaluation
- Out-of-distribution testing
- Model calibration assessment
- Error analysis and risk-based thresholds
- Defined human review and escalation procedures
- Security architecture and access controls
- Logging, monitoring, and incident response
- Applicable privacy and legal reviews
- Formal security authorization where required
- Ongoing model performance monitoring

## 10. Governance Statement

This project is a non-operational educational
demonstration of AI/ML lifecycle concepts.

It does not represent an accredited, authorized,
or deployed federal information system.
