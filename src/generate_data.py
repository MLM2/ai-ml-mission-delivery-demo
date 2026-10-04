
from pathlib import Path
import random
import pandas as pd

# Identify the main project folder.
ROOT = Path(__file__).resolve().parents[1]

# Create a folder for generated data.
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Use a fixed random seed for reproducibility.
random.seed(42)

# Fictional technical requests grouped by category.
categories = {
    "Data Integration": [
        "Build an API interface for exchanging database records",
        "Investigate data mapping issues between source systems",
        "Connect an application to a relational database",
        "Validate JSON payloads sent through an integration endpoint",
        "Resolve a data ingestion failure in the pipeline",
        "Document schema changes for an external data feed",
        "Reconcile duplicate records in a data warehouse",
        "Configure a connector to transfer application data"
    ],
    "Security Review": [
        "Review access control requirements for an application",
        "Assess identity permissions for a protected data service",
        "Document security controls for authorization review",
        "Investigate an audit logging configuration gap",
        "Evaluate encryption requirements for stored records",
        "Review least privilege settings for service accounts",
        "Prepare security evidence for an accreditation review",
        "Assess authentication requirements for a new interface"
    ],
    "Model Evaluation": [
        "Evaluate classifier precision and recall on test data",
        "Investigate machine learning model prediction errors",
        "Review confusion matrix results from the latest experiment",
        "Compare candidate models using F1 scores",
        "Assess training data quality and possible model bias",
        "Investigate model drift in recent predictions",
        "Validate an experiment against acceptance criteria",
        "Review false positive and false negative predictions"
    ],
    "Deployment Support": [
        "Coordinate a software release into the test environment",
        "Prepare a deployment rollback plan",
        "Investigate an application failure after release",
        "Review production monitoring alerts after deployment",
        "Validate container deployment readiness",
        "Coordinate release scheduling across technical teams",
        "Prepare an operational handoff checklist",
        "Resolve an environment configuration issue before rollout"
    ]
}

programs = [
    "Program Alpha",
    "Program Bravo",
    "Program Charlie"
]

contexts = [
    "during a planned update",
    "before the next milestone",
    "for a new customer request",
    "after a technical review",
    "as part of an integration effort"
]

records = []

# Create 80 fictional requests for each category.
for category, examples in categories.items():
    for i in range(80):
        description = (
            random.choice(examples)
            + " "
            + random.choice(contexts)
        )

        records.append({
            "request_id": f"REQ-{len(records)+1:04d}",
            "program": random.choice(programs),
            "description": description,
            "category": category
        })

# Convert records into a table.
df = pd.DataFrame(records)

# Shuffle the rows in a repeatable way.
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Save the synthetic dataset.
output_file = DATA_DIR / "synthetic_requests.csv"
df.to_csv(output_file, index=False)

# Show confirmation when the program runs.
print("Dataset created successfully!")
print("Total requests:", len(df))
print()
print("Requests by category:")
print(df["category"].value_counts())
print()
print("First five records:")
print(df.head())
print()
print("Saved to:", output_file)
