#  PolicyDrift-Sentinel: AI Regulatory Gap Analysis

[![Hugging Face Space](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-orange?logo=huggingface)](YOUR_HF_SPACE_URL_HERE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)

###  The Problem: "Regulatory Drift"
In 15 years of architecting Azure solutions, I've observed that the gap between **Global Regulations** (GDPR, EU AI Act, RBI) and **Internal Corporate Policies** is a significant operational risk. **PolicyDrift-Sentinel** automates the detection of these discrepancies using private, localized Small Language Models (SLMs).

---

## Architecture Overview
This system is built for **Data Sovereignty**. Unlike standard LLMs, this Sentinel runs locally to ensure that sensitive internal policy documents never leave the enterprise perimeter.

* **Model:** Microsoft **Phi-4-Mini** (3.8B Parameters)
* **Inference:** [Ollama](https://ollama.ai/) (Local SLM Engine)
* **Interface:** Streamlit
* **Target:** Governance, Risk, and Compliance (GRC) automation.

## Demo Preview
![PolicyDrift Sentinel Screenshot](assets/money-shot.png)
*(Replace this with your "Money Shot" tomorrow!)*

---

##  Quick Start (Local Setup)

### 1. Prerequisites
Install [Ollama](https://ollama.ai/) and pull the Phi-4-Mini model:
```bash
ollama pull phi4-mini
