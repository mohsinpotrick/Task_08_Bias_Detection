import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("bias_analysis.csv")
avg_sentiment = df.groupby(["bias_type"])["sentiment"].mean()
avg_sentiment.plot(kind="bar", color=["skyblue", "salmon", "lightgreen"])
plt.ylabel("Average Sentiment")
plt.title("Average Sentiment by Bias Type")
plt.xticks(rotation=0)
plt.savefig("bias_sentiment_chart.png")
plt.show()

