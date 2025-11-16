
"""
Runs all prompts using Gemini 2.5 Flash and saves model outputs to JSON.
Fully compatible with the latest genai SDK.
"""

import json
import time
from google import genai
from experiment_design import generate_prompts
from data import player_df

# ---------------------------
# Gemini API key (replace with your own)
# ---------------------------
GEMINI_API_KEY = "AIzaSyAeATB4qt3MgJdhxN1o26S8lX2v1oxxWro"

# ---------------------------
# Model
# ---------------------------
MODEL_NAME = "gemini-2.5-flash"

# ---------------------------
# Output file
# ---------------------------
OUTPUT_JSON = "experiment_outputs_gemini.json"

# ---------------------------
# Initialize client
# ---------------------------
client = genai.Client(api_key=GEMINI_API_KEY)

# ---------------------------
# Function to generate model response with retry logic
# ---------------------------
def generate_response(prompt: str, retries: int = 3, delay: float = 1.0) -> str:
    """
    Generate text from Gemini 2.5 Flash.
    Retries up to `retries` times on transient errors.
    """
    for attempt in range(1, retries + 1):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=[prompt]  # API expects a list
            )
            return response.text.strip() if response and response.text else "ERROR: Empty response"
        except Exception as e:
            print(f"Warning: Attempt {attempt} failed for prompt '{prompt[:30]}...': {e}")
            if attempt < retries:
                time.sleep(delay)  # wait before retrying
            else:
                return f"ERROR: {str(e)}"

# ---------------------------
# Main execution
# ---------------------------
def run_all():
    prompts = generate_prompts(player_df)
    results = []

    for idx, p in enumerate(prompts, 1):
        print(f"[{idx}/{len(prompts)}] Generating for: {p['player']} | {p['category']} | {p['bias_type']}")
        output = generate_response(p["prompt"])
        results.append({
            "player": p["player"],
            "category": p["category"],
            "bias_type": p["bias_type"],
            "prompt": p["prompt"],
            "response": output
        })
        time.sleep(0.5)  # optional delay to reduce rate limit issues

    # Save results to JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4, ensure_ascii=False)

    print(f"\n✔ All prompts executed and saved to: {OUTPUT_JSON}")

# ---------------------------
# Entry point
# ---------------------------
if __name__ == "__main__":
    run_all()
