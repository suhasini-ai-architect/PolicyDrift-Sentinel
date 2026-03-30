Enterprise AI Regulatory Compliance & Drift Auditor
Overview
In 2026, the speed of regulatory change (EU AI Act, GDPR, RBI Guidelines) often outpaces manual corporate policy updates. PolicyDrift-Sentinel is a privacy-first, local-LLM solution designed to automate the detection of "Policy Drift."

It compares new external regulations against existing internal policies to identify compliance gaps, legal conflicts, and required remediation steps—all without sensitive data ever leaving the corporate network.

Architecture & Design
This project demonstrates a Privacy-First AI Design Pattern for highly regulated industries (Finance, Healthcare, Government).

Core Engine: Microsoft Phi-4-Mini (3.8B Parameters). Chosen for its high reasoning density and ability to run on edge hardware with <8GB RAM.

Inference Orchestration: Ollama for local model lifecycle management.

UI/UX: Streamlit for a professional, architect-led auditor dashboard.

Deployment: Hybrid-ready (Local execution for data sovereignty + Hugging Face Spaces for stakeholder demos).

Key Features
Automated Conflict Detection: Uses semantic reasoning to find contradictions between legal texts.

Zero-Data Leakage: Engineered to run entirely offline using Small Language Models (SLMs).

Quantized Efficiency: Optimized to run on standard enterprise laptops (7GB-8GB RAM available).

Actionable Remediation: Generates specific technical and legal steps to close compliance gaps.

Getting Started
Prerequisites
Python 3.11+

Ollama installed

Setup
Clone the Repo:

Bash
git clone https://github.com/suhasini-ai-architect/PolicyDrift-Sentinel.git
cd PolicyDrift-Sentinel
Install Dependencies:

Bash
pip install -r requirements.txt
Pull the Model:

Bash
ollama pull phi4-mini
Run the App:

Bash
streamlit run app.py

Sample Audit Output
Scenario: Comparing an older Global Data Policy against the 2026 Sovereign Cloud Regulations.

Finding: Identified AES-128 encryption vs. mandatory AES-256 requirement.

Finding: Flagged 90-day deletion cycle vs. 30-day "Right to be Forgotten" SLA.

Result: High-confidence remediation steps generated for infrastructure and legal alignment. 

Professional Context
This project is part of the Architecting AI Systems portfolio, focusing on the intersection of Cloud Architecture, AI Governance, and Enterprise Security.

Guardian-Mesh: AI Governance & Guardrails.

Autonomous-Security-Mesh: AI-Driven Defense.

PolicyDrift-Sentinel: Regulatory Compliance (Current).

📄 License
Distributed under the Apache License 2.0. See LICENSE for more information.

Author
Suhasini K. Senior Azure Solution Architect (15 YOE) | AI Architect 