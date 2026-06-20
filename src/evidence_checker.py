import pandas as pd

# Load evidence requirements
requirements_df = pd.read_csv(
    "dataset/evidence_requirements.csv"
)

def check_evidence(claim_object, image_count):

    # Default required images
    required = 1

    # Object-specific requirements
    if claim_object == "car":
        required = 2

    elif claim_object == "laptop":
        required = 1

    elif claim_object == "package":
        required = 2

    # Check evidence
    if image_count >= required:

        return (
            True,
            f"{image_count}/{required} images available"
        )

    return (
        False,
        f"{image_count}/{required} images available"
    )