"""
Generate a bar chart of average sentiment by bias type
from bias_analysis_gemini.csv.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------
# Load data
# ---------------------------
INPUT_CSV = "bias_analysis_gemini.csv"
OUTPUT_PNG = "bias_sentiment_barplot.png"

df = pd.read_csv(INPUT_CSV)

# ---------------------------
# Compute average sentiment per bias_type
# ---------------------------
avg_sentiment = df.groupby("bias_type")["sentiment"].mean().reset_index()

# ---------------------------
# Create bar chart
# ---------------------------
plt.figure(figsize=(12, 6))
sns.barplot(x="bias_type", y="sentiment", data=avg_sentiment, palette="viridis")
plt.xticks(rotation=45, ha="right")
plt.title("Average Sentiment by Bias Type")
plt.ylabel("Average Sentiment Polarity")
plt.xlabel("Bias Type")
plt.tight_layout()

# ---------------------------
# Save PNG
# ---------------------------
plt.savefig(OUTPUT_PNG)
plt.show()

print(f"✔ Bar chart saved as {OUTPUT_PNG}")
