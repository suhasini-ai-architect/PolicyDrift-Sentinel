import streamlit as st
import requests

st.set_page_config(page_title="PolicyDrift Sentinel", layout="wide")

st.title("🛡️ PolicyDrift Sentinel")
st.subheader("Automated Regulatory Compliance & Drift Auditor")

# Detect Hugging Face environment
IS_HF_SPACE = "HF_SPACE" in st.secrets if hasattr(st, "secrets") else False

# Mode badge
if IS_HF_SPACE:
    st.success("🟢 Mode: Demo (Simulated)")
else:
    st.success("🟢 Mode: Live AI (Ollama)")

# Sample Data
sample_reg = "Personal data must not be retained longer than necessary (GDPR Article 5)."
sample_policy = "We retain user financial data for 7 years for audit purposes."

# Inputs
new_reg = st.text_area("📄 New Regulation (Source A)", value="")
old_policy = st.text_area("🏢 Internal Policy (Source B)", value="")

# Demo Button
if st.button("💡 Try Sample Compliance Audit"):
    new_reg = sample_reg
    old_policy = sample_policy

# Extract helper
def extract_section(text, section):
    try:
        part = text.split(section + ":")[1]
        return part.split("\n")[0].strip()
    except:
        return "Not found"

# Analysis
if st.button("🔍 Run Analysis") and new_reg and old_policy:

    if IS_HF_SPACE:
        # Demo output
        response_text = """
Detected Gap: Data Retention Policy Violation
Risk Level: HIGH
Regulation Reference: GDPR Article 5 – Storage Limitation Principle
Recommended Action:
- Define purpose-based retention policy
- Implement auto-deletion workflows
- Add audit logging
- Align retention with regulatory necessity
"""

        st.warning("⚠️ Demo Mode uses simulated output. Run locally with Ollama for real analysis.")

    else:
        # Real Ollama call
        try:
            prompt = f"""
You are an expert Regulatory Compliance Auditor.

Compare:

New Regulation:
{new_reg}

Internal Policy:
{old_policy}

Return STRICTLY in this format:

Detected Gap:
<one line>

Risk Level:
<LOW / MEDIUM / HIGH>

Regulation Reference:
<specific law>

Recommended Action:
- Action 1
- Action 2
- Action 3
"""

            res = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": "phi", "prompt": prompt, "stream": False}
            )

            response_text = res.json()["response"]

        except Exception as e:
            st.error("❌ Ollama not running. Please start Ollama.")
            st.stop()

    # Display structured output
    st.markdown("## 🔍 Analysis Result")

    st.markdown("### ⚠️ Detected Gap")
    st.write(extract_section(response_text, "Detected Gap"))

    st.markdown("### 📊 Risk Level")
    st.write(extract_section(response_text, "Risk Level"))

    st.markdown("### 📜 Regulation Reference")
    st.write(extract_section(response_text, "Regulation Reference"))

    st.markdown("### 🛠️ Recommended Action")
    actions = response_text.split("Recommended Action:")[-1].strip()
    st.write(actions)

# Footer
st.markdown("---")
st.caption("🔒 Privacy Guar