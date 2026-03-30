import streamlit as st
import os
import time

# 1. Environment Detection
IS_HF_SPACE = "SPACE_ID" in os.environ

try:
    import ollama
except ImportError:
    ollama = None

st.set_page_config(page_title="PolicyDrift Sentinel", page_icon="🛡️", layout="wide")

# --- UI Header ---
st.title("🛡️ PolicyDrift Sentinel")
st.markdown("### *Enterprise-Grade Regulatory Auditor*")

# --- Sidebar ---
with st.sidebar:
    st.header("System Status")
    if IS_HF_SPACE:
        st.success("🌐 Running on Hugging Face Cloud")
        st.info("Demo Mode: Uses synthetic audit logic.")
    else:
        st.success("💻 Running on Local Laptop")
        st.info("Live Mode: Powered by Phi-4-Mini (3.8B)")
    
    st.divider()
    st.write("**Architect:** Suhasini K.")
    st.write("**Experience:** 15 YOE Solutions Architect")

# --- Main App ---
col1, col2 = st.columns(2)
with col1:
    new_reg = st.text_area("📄 New Regulation (Source A):", placeholder="e.g., EU AI Act 2026...", height=250)
with col2:
    old_policy = st.text_area("🏢 Internal Policy (Source B):", placeholder="e.g., Corporate Data Policy v1.2...", height=250)

if st.button("🚀 Run Compliance Audit", use_container_width=True):
    if not new_reg or not old_policy:
        st.error("Please provide both documents to begin the audit.")
    else:
        with st.spinner("Phi-4-Mini is analyzing policy alignment..."):
            if IS_HF_SPACE or ollama is None:
                # --- DEMO MODE ---
                time.sleep(2) # Simulate processing
                st.subheader("🚩 Audit Findings (Demo)")
                st.error("**Finding 1:** Conflict detected in 'Data Retention' clause.")
                st.warning("**Finding 2:** Missing 'Model Transparency' requirements.")
            else:
                # --- LIVE MODE ---
                try:
                    prompt = f"""
                    Identify specific legal conflicts (Policy Drift) between these texts:
                    Regulation: {new_reg}
                    Internal Policy: {old_policy}
                    
                    Format as: 
                    1. Summary of Drift
                    2. Specific Non-Compliant Clauses
                    3. Recommended Remediation
                    """
                    response = ollama.generate(model='phi4-mini', prompt=prompt)
                    st.subheader("✅ Live Audit Result")
                    st.markdown(response['response'])
                except Exception as e:
                    st.error(f"Ollama Error: {e}")
                    st.info("Make sure 'ollama pull phi4-mini' is complete in your terminal.")

st.divider()
st.caption("🔒 Security Note: In Local Mode, all processing happens on your RAM. No enterprise data is sent to the cloud.")