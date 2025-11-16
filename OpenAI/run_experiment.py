"""
Runs all prompts and saves model outputs.
"""

import json
from openai import OpenAI
from data import player_df
from experiment_design import generate_prompts

client = OpenAI(api_key="myapikey")
def run_all():

    prompts = generate_prompts(player_df)
    results = []

    for p in prompts:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": p["prompt"]}]
        )

        results.append({
            "player": p["player"],
            "category": p["category"],
            "bias_type": p["bias_type"],
            "prompt": p["prompt"],
            "response": response.choices[0].message.content
        })

    with open("experiment_outputs.json", "w") as f:
        json.dump(results, f, indent=4)

    print("✔ All prompts executed and saved to experiment_outputs.json")

if __name__ == "__main__":
    run_all()

