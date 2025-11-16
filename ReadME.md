# Task_08_Bias_Detection — LLM Bias Analysis on Syracuse Lacrosse Data

## Overview
This project investigates potential biases in large language model (LLM)-generated data narratives using Syracuse Women’s Lacrosse performance data.  
The experiment tests how **prompt framing**, **demographic context**, and **priming hypotheses** affect LLM interpretations of identical statistics.  

---

## Objectives
- Detect **framing, demographic, confirmation, and selection biases** in LLM outputs.
- Compare consistency and fairness across multiple LLMs (OpenAI GPT-4, Claude.ai, Gemini).
- Provide reproducible methodology for analyzing bias in LLM-generated narratives.

---

## Dataset
- **Source:** Syracuse Performance Data (anonymized)
- **Fields:** Period, Goals, Saves, Shots, Shots on Goal (for Syracuse and opponents)
- **Usage:** Neutral numeric dataset ideal for testing prompt-dependent narrative differences.

---

## Repository Structure
│
├─ OpenAI/ # OpenAI visualization charts
    └─ bias_sentiment_chart.png
    └─ experiment_design.py # Generates prompt variations
    └─ run_experiment.py # Executes LLM queries
    └─ analyze_bias.py # Quantitative analysis
    └─ validate_claims.py # Validates LLM outputs vs. data
├─ Gemini/ # Gemini visualization charts
    └─ bias_sentiment_barplot.png
    └─ experiment_design.py # Generates prompt variations
    └─ run_experiment.py # Executes LLM queries
    └─ analyze_bias.py # Quantitative analysis
    └─ validate_claims.py # Validates LLM outputs vs. data
├─ prompts/ # Prompt templates and variations
├─ results/ # Raw LLM responses (JSON/CSV)
├─ analysis/ # Statistical tests, visualizations
├─ REPORT.md # Final bias detection report
└─ .gitignore # Excludes sensitive files


## Files to run 

### Generate prompts:

```bash
python experiment_design.py
```

### Run experiments on LLMs:

```bash
python run_experiment.py
```

### Analyze bias:

```bash
python analyze_bias.py
```

### Validate LLM claims:

```bash
python validate_claims.py
```


