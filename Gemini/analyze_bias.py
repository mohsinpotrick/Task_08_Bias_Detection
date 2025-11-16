"""
Basic text analysis to detect sentiment and framing differences.
"""

import json
from textblob import TextBlob
import pandas as pd

def analyze():
    with open("experiment_outputs_gemini.json") as f:
        data = json.load(f)

    rows = []

    for entry in data:
        text = entry["response"]
        sentiment = TextBlob(text).sentiment.polarity

        rows.append({
            "player": entry["player"],
            "category": entry["category"],
            "bias_type": entry["bias_type"],
            "sentiment": sentiment
        })

    df = pd.DataFrame(rows)
    df.to_csv("bias_analysis_gemini.csv", index=False)

    print("✔ Bias results saved to bias_analysis_gemini.csv")

if __name__ == "__main__":
    analyze()

