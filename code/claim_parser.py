def extract_claim(text):

    text = text.lower()

    issue_type = "unknown"
    object_part = "unknown"
    severity = "low"

    # Issue Type
    if "dent" in text:
        issue_type = "dent"

    elif "scratch" in text:
        issue_type = "scratch"

    elif "crack" in text:
        issue_type = "crack"

    elif "shatter" in text:
        issue_type = "glass_shatter"

    # Object Part
    if "front bumper" in text:
        object_part = "front_bumper"

    elif "door" in text:
        object_part = "door"

    elif "windshield" in text:
        object_part = "windshield"

    elif "headlight" in text:
        object_part = "headlight"

    # Severity
    if "deep" in text:
        severity = "high"

    elif "shatter" in text:
        severity = "high"

    elif "crack" in text:
        severity = "medium"

    return {
        "issue_type": issue_type,
        "object_part": object_part,
        "severity": severity
    }