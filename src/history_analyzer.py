import pandas as pd

history_df = pd.read_csv("dataset/user_history.csv")

def get_user_history(user_id):

    user = history_df[
        history_df["user_id"] == user_id
    ]

    if len(user) == 0:

        return {
            "risk_flag": "none"
        }

    user = user.iloc[0]

    if user["rejected_claim"] >= 3:

        return {
            "risk_flag": "user_history_risk"
        }

    return {
        "risk_flag": "none"
    }