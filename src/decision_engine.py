def decide(issue_type):

    if issue_type == "unknown":

        return {
            "claim_status": "not_enough_information",
            "justification":
            "Issue could not be identified from claim"
        }

    return {
        "claim_status": "supported",
        "justification":
        "Issue mentioned clearly in claim"
    }