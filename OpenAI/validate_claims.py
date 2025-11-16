"""
Validate numeric claims in model responses against true player stats.
Works with experiment_outputs_gemini.json from run_experiments.
"""

import re
import json
import os
import pandas as pd
from data import player_df  # team stats if needed

# ---------------------------
# File paths
# ---------------------------
IN_FILE = "experiment_outputs.json"  # from run_all()
OUT_FILE = "fabrications_openai.csv"

# ---------------------------
# Load experiment results
# ---------------------------
with open(IN_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# ---------------------------
# Build truth dict
# ---------------------------
truth_players = {}
for _, row in player_df.iterrows():
    truth_players[row['Player']] = {
        "goals": int(row.get('G') or 0),
        "assists": int(row.get('A') or 0),
        "points": int(row.get('Pts') or 0)
    }

# ---------------------------
# Validate claims
# ---------------------------
rows = []

for entry in data:
    player = entry['player']
    text = str(entry['response'])
    bias_type = entry['bias_type']

    # Simple regex heuristics for numeric claims
    claims = {
        "goals": re.findall(r"([0-9]{1,3})\s+goals", text, flags=re.I),
        "assists": re.findall(r"([0-9]{1,3})\s+assists", text, flags=re.I),
        "points": re.findall(r"([0-9]{1,3})\s+points", text, flags=re.I)
    }

    for stat, found in claims.items():
        for val in found:
            try:
                claimed_val = int(val)
                true_val = truth_players.get(player, {}).get(stat)
                if true_val is not None and claimed_val != true_val:
                    rows.append({
                        "player": player,
                        "bias_type": bias_type,
                        "stat": stat,
                        "claimed_value": claimed_val,
                        "true_value": true_val,
                        "response_snippet": text[:200]
                    })
            except:
                continue
# ---------------------------
# Write CSV
# ---------------------------
out_df = pd.DataFrame(rows)
if not out_df.empty:
    out_df.to_csv(OUT_FILE, index=False)
    print("Fabrications saved to", OUT_FILE)
else:
    # Create a placeholder CSV indicating no fabrications
    placeholder_df = pd.DataFrame([{
        "message": "No numeric fabrications detected (by simple heuristic)."
    }])
    placeholder_df.to_csv(OUT_FILE, index=False)
    print("No numeric fabrications detected; placeholder CSV created:", OUT_FILE)
