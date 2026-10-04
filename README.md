
# AI/ML Mission Delivery Demonstration

### Synthetic Mission Request Classification | Technical Program Management | Responsible AI

An educational AI/ML project demonstrating how a mission-oriented
technical program manager can coordinate data preparation,
model development, evaluation, automated testing, Agile delivery,
risk management, and security authorization planning.

**Repository owner:** Mike McKeever

**Project status:** Working educational prototype

**Operational status:** Not deployed; no Authority to Operate (ATO)

---

## Project Overview

This project demonstrates a basic machine-learning workflow
that classifies fictional mission-support requests into
four categories:

1. Data Integration
2. Deployment Support
3. Model Evaluation
4. Security Review

The classifier uses TF-IDF text vectorization and
logistic regression implemented with scikit-learn.

Predictions are advisory. An illustrative decision threshold
flags lower-scoring predictions for human review.

The project uses synthetic data only and does not connect
to government systems.

## Why I Built This Project

My professional background includes federal mission
IT program management, Agile/SAFe delivery,
requirements analysis, systems integration,
and government-side technical oversight.

I developed this educational prototype to strengthen
my hands-on understanding of AI/ML workflows and
demonstrate how technical delivery activities can
be coordinated with program management,
testing, risk management, and governance.

The project is not intended to represent production
ML engineering experience or an operational federal system.

## Technical Stack

- Python
- pandas
- scikit-learn
- TF-IDF
- Logistic Regression
- pytest
- Google Colab
- GitHub
- Markdown and Mermaid architecture diagrams

## Implemented Capabilities

### 1. Synthetic Data Generation

A Python script generates 320 fictional
mission-support requests across four categories.

Each category contains 80 labeled examples.

**Artifact:** `src/generate_data.py`

### 2. Model Training and Evaluation

A baseline classifier is trained using:

- TF-IDF text features
- Logistic regression
- Stratified 80/20 train/test split
- Fixed random seed for reproducibility

The split produces:

- 256 training records
- 64 testing records

Evaluation includes accuracy, precision,
recall, and F1.

**Artifact:** `src/train_model.py`

### 3. Exploratory Notebook

A Google Colab notebook documents
the experimental workflow and results.

The initial experiment achieved 100% accuracy
on a synthetic 64-record holdout.

This result is not evidence of real-world
model performance. The generated dataset
contains repetitive patterns and may
overstate generalization.

**Artifact:** `notebooks/Mission_Request_ML_Experiment.ipynb`

### 4. Prediction and Human Review

The prediction script classifies fictional
requests and returns:

- Predicted category
- Model score
- Human-review decision

The illustrative threshold is 0.70.

Below-threshold results are flagged:

`HUMAN REVIEW REQUIRED`

Other results receive:

`PROVISIONAL ROUTING SUGGESTION`

Scores are not calibrated probabilities
of correctness. No operational routing occurs.

**Artifact:** `src/predict.py`

### 5. Automated Testing

Eight automated pytest checks cover:

- Dataset structure
- Record count
- Category count
- Basic prediction behavior
- Required output fields
- Model score range
- Human-review threshold behavior

**Verified result:** 8 tests passed.

**Artifact:** `tests/test_model.py`

## Repository Structure

```text
ai-ml-mission-delivery-demo/
|
|-- data/
|   |-- synthetic_requests.csv
|   `-- README.md
|
|-- notebooks/
|   |-- Mission_Request_ML_Experiment.ipynb
|   `-- README.md
|
|-- src/
|   |-- generate_data.py
|   |-- train_model.py
|   `-- predict.py
|
|-- tests/
|   `-- test_model.py
|
|-- docs/
|   |-- model_card.md
|   |-- risk_register.md
|   |-- agile_backlog.md
|   |-- architecture.md
|   `-- rmf_ato_readiness.md
|
|-- .gitignore
|-- LICENSE
`-- README.md
```

## Run the Project

### Prerequisites

Python 3.10 or newer and these packages:

```bash
python -m pip install pandas scikit-learn pytest
```

### 1. Clone the Repository

```bash
git clone https://github.com/MLM2/ai-ml-mission-delivery-demo.git
cd ai-ml-mission-delivery-demo
```

### 2. Generate Synthetic Data

```bash
python src/generate_data.py
```

Alternatively, use the committed synthetic CSV
in the `data/` directory.

### 3. Train and Evaluate the Classifier

```bash
python src/train_model.py
```

### 4. Run Example Predictions

```bash
python src/predict.py
```

### 5. Run Automated Tests

```bash
python -m pytest tests/test_model.py -v
```

The scripts were exercised in Google Colab.
The test suite completed with eight passing tests.

## Reference Architecture

See [Architecture Documentation](docs/architecture.md)
for implemented and proposed future-state diagrams.

The implemented workflow includes:

1. Synthetic data generation
2. Data loading and validation
3. Train/test splitting
4. TF-IDF and logistic regression
5. Model evaluation
6. Advisory inference
7. Human-review decision logic
8. Automated software tests

The future-state architecture is conceptual
and has not been implemented.

## AI/ML Delivery and Governance Artifacts

| Artifact | Purpose |
|---|---|
| [Model Card](docs/model_card.md) | Intended use, evaluation, limitations, and oversight |
| [Risk Register](docs/risk_register.md) | Risk scoring, proposed owners, mitigations, and escalation |
| [Agile Product Backlog](docs/agile_backlog.md) | User stories, acceptance criteria, and delivery planning |
| [Reference Architecture](docs/architecture.md) | Implemented workflow and proposed future-state components |
| [RMF/ATO Readiness](docs/rmf_ato_readiness.md) | Illustrative federal security authorization planning |

## Technical Program Management Perspective

This demonstration connects technical implementation
to delivery-management practices:

**Requirements management**

- Define capabilities and acceptance criteria.
- Maintain traceability between requirements and tests.

**Agile delivery**

- Prioritize backlog items.
- Identify dependencies and plan incremental demonstrations.

**Quality management**

- Establish reproducible test execution.
- Document evaluation evidence and known limitations.

**Risk management**

- Assess data suitability, model generalization,
  confidence limitations, and integration risks.
- Assign proposed owners and mitigation actions.

**Security and governance**

- Identify potential security requirements early.
- Integrate RMF-related dependencies into planning.
- Distinguish prototype functionality from
  formally authorized operational capabilities.

## Key Limitations

- The dataset is entirely synthetic.
- Test descriptions may resemble training descriptions.
- Model performance has not been validated
  using independent operational data.
- Model scores are not calibrated.
- The human-review threshold is illustrative.
- There is no deployed API or user interface.
- No formal security assessment has been performed.
- No ATO has been granted.
- The project is not suitable for production use.

## Future Enhancements

- Independent evaluation datasets
- Out-of-distribution testing
- Model calibration assessment
- Expanded automated test coverage
- Continuous integration
- Model versioning and reproducibility
- Monitoring and drift detection
- Formalized human-review workflow
- Security architecture and control implementation planning

## Project Disclaimer

This repository is an independent educational AI/ML demonstration developed using synthetic data.

It is not affiliated with, sponsored by, or endorsed by any government agency or private organization.

The project does not contain classified information, sensitive operational data, or proprietary materials.

It is not an operational system and has not undergone formal security accreditation or authorization.

All architectures, governance artifacts, and operational scenarios are illustrative and intended solely for professional development and technical demonstration.


## License

See [LICENSE](LICENSE).
