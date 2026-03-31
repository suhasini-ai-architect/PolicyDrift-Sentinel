#  PolicyDrift-Sentinel: AI Regulatory Gap Analysis

[![Hugging Face Space](https://img.shields.io/badge/Live%20Demo-Hugging%20Face-orange?logo=huggingface)](YOUR_HF_SPACE_URL_HERE)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)

---

##  The Problem: Regulatory Drift

In enterprise environments, the gap between **Global Regulations** (GDPR, EU AI Act, RBI) and **Internal Corporate Policies** creates significant compliance and operational risk.

**PolicyDrift-Sentinel** automatically detects these gaps using private, local Small Language Models (SLMs).

---

##  Why This Matters

* Compliance failures lead to **financial penalties and reputational damage**
* Manual audits are **slow, inconsistent, and expensive**
* Enterprises need **automated, explainable compliance intelligence**

---

##  Architecture Overview

Built for **Data Sovereignty & Enterprise Security**:

* **Model:** Microsoft Phi-4-Mini (3.8B Parameters)
* **Inference:** Ollama (local SLM runtime)
* **Interface:** Streamlit
* **Domain:** Governance, Risk & Compliance (GRC)

###  Workflow

1. Upload internal policy document
2. System parses regulatory requirements
3. Detects compliance gaps (policy drift)
4. Generates remediation recommendations

---


## Architecture Diagram

![PolicyDrift Sentinel Screenshot](assets/PolicyDrift.png)


---


##  Demo Preview

![PolicyDrift Sentinel Screenshot](assets/PolicyDrift.gif)


---

##  Quick Start (Local Setup)

###  1. Prerequisites

Install Ollama and pull the model:

```bash
ollama pull phi4-mini
```

---

###  2. Installation

```bash
git clone https://github.com/suhasini-ai-architect/PolicyDrift-Sentinel.git
cd PolicyDrift-Sentinel

python -m venv venv

# Windows
.\\venv\\Scripts\\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

---

###  3. Run the App

```bash
streamlit run app.py
```


##  Sample Output

**Input Policy Clause:**
> "User data must be retained for 5 years."

**Regulation Reference (GDPR):**
> "Personal data should not be kept longer than necessary."

**Detected Gap:**
❌ Over-retention risk identified

**AI Recommendation:**
✔ Define retention justification  
✔ Implement auto-deletion after purpose completion  
✔ Add audit logging

---

##  Enterprise-Ready Features

*  **Zero Data Leakage** – 100% local inference
*  **Cross-Domain Compliance Audit** – GDPR, RBI, AI Act mapping
*  **AI-Powered Gap Detection** – semantic comparison of policies
*  **Remediation Engine** – actionable compliance fixes

---

## Future Roadmap

* Multi-model support (Mistral, Llama)
* API integration for enterprise systems
* Dashboard for compliance analytics
* Fine-tuned domain-specific models

---

##  Author

**Suhasini K.**
Senior Azure Solution Architect → AI Architect

---

## Support

If you find this useful, consider giving it a ⭐ on GitHub!
