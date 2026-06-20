import pandas as pd

from claim_parser import extract_claim
from decision_engine import decide
from image_analyzer import analyze_image
from history_analyzer import get_user_history
from evidence_checker import check_evidence

# Read claims
claims = pd.read_csv("dataset/claims.csv")

results = []

for index, row in claims.iterrows():

    # -----------------------
    # Claim Analysis
    # -----------------------
    claim_data = extract_claim(
        row["user_claim"]
    )

    # -----------------------
    # User History
    # -----------------------
    history = get_user_history(
        row["user_id"]
    )

    # -----------------------
    # Image Analysis
    # -----------------------
    images = row["image_paths"].split(";")

    image_results = []

    for image_path in images:

        full_path = "dataset/" + image_path

        image_result = analyze_image(
            full_path
        )

        image_results.append(
            image_result
        )

    # -----------------------
    # Evidence Check
    # -----------------------
    evidence_met, evidence_reason = (
        check_evidence(
            row["claim_object"],
            len(images)
        )
    )

    # -----------------------
    # Risk Flags
    # -----------------------
    risk_flag = history["risk_flag"]

    for img in image_results:

        if img["valid_image"] == False:

            risk_flag = "blurry_image"

    # -----------------------
    # Decision
    # -----------------------
    decision = decide(
        claim_data["issue_type"]
    )

    # -----------------------
    # Output Row
    # -----------------------
    result = {

        "user_id":
        row["user_id"],

        "image_paths":
        row["image_paths"],

        "user_claim":
        row["user_claim"],

        "claim_object":
        row["claim_object"],

        "evidence_standard_met":
        evidence_met,

        "evidence_standard_met_reason":
        evidence_reason,

        "risk_flags":
        risk_flag,

        "issue_type":
        claim_data["issue_type"],

        "object_part":
        claim_data["object_part"],

        "claim_status":
        decision["claim_status"],

        "claim_status_justification":
        decision["justification"],

        "supporting_image_ids":
        "none",

        "valid_image":
        True,

        "severity":
        claim_data["severity"]
    }

    results.append(result)

# -----------------------
# Create DataFrame
# -----------------------
output_df = pd.DataFrame(results)

# -----------------------
# Save Output CSV
# -----------------------
output_df.to_csv(
    "dataset/output.csv",
    index=False
)

# -----------------------
# Display Results
# -----------------------
print(output_df.head())

print("\n✅ output.csv generated successfully")
print("✅ Total Claims:", len(output_df))

risk_count = (
    output_df["risk_flags"]
    == "user_history_risk"
).sum()

print(
    "✅ Users with history risk:",
    risk_count
)