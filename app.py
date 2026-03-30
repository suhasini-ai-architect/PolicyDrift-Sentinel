import streamlit as st
import os
import time

# 1. Environment Detection (Hugging Face vs. Local)
IS_HF_SPACE = "SPACE_ID" in os.environ

# 2. Local-Only Import for Ollama
try:
    import ollama
except ImportError:
    ollama = None

# --- UI Configuration ---
st.set_page_config(page_title="PolicyDrift Sentinel", page_icon="🛡️", layout="wide")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stTextArea textarea { font-size: 14px !format; }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar Architecture Info ---
with st.sidebar:
    st.title("⚙️ System Arch")
    if IS_HF_SPACE:
        st.success("🌐 Environment: Hugging Face Cloud")
        st.caption("Mode: Synthetic Demo (No Local GPU)")
    else:
        st.success("💻 Environment: Local Workstation")
        st.caption("Mode: Live Phi-4-Mini Inference")
    
    st.divider()
    st.markdown("### **Architect Profile**")
    st.write("**Suhasini K.**")
    st.write("Senior Azure Solution Architect")
    st.write("15 YOE Enterprise Architecture")
    st.divider()
    st.info("This Sentinel uses SLMs (Small Language Models) to perform high-density regulatory gap analysis.")

# --- Main App Interface ---
st.title("🛡️ PolicyDrift Sentinel")
st.subheader("Automated Regulatory Compliance & Drift Auditor")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📄 New Regulation (Source A)")
    new_reg = st.text_area("Paste the new law or regulatory update here:", 
                           placeholder="e.g., EU AI Act 2026, GDPR Update, RBI Master Circular...", 
                           height=300)

with col2:
    st.markdown("#### 🏢 Internal Policy (Source B)")
    old_policy = st.text_area("Paste your existing corporate policy here:", 
                              placeholder="e.g., Data Governance Policy v2.1, InfoSec Manual...", 
                              height=300)

# --- Audit Execution ---
if st.button("🚀 Run Compliance Audit", use_container_width=True):
    if not new_reg or not old_policy:
        st.warning("Please provide both documents to begin the cross-correlation audit.")
    else:
        with st.spinner("Phi-4-Mini is analyzing high-dimensional policy drift..."):
            
            # CASE 1: Running on Hugging Face (Demo Mode)
            if IS_HF_SPACE or ollama is None:
                time.sleep(1.5) # Simulate processing time
                st.subheader("✅ Compliance Audit Report (Demo Mode)")
                st.error("### 🚩 Critical Drift Detected")
                st.markdown("""
                **Summary of Drift:**
                The internal policy is non-compliant regarding **Data Encryption standards** (AES-128 vs AES-256), **Data Sovereignty** (Global Lake vs Region-Locked), and **Deletion SLAs** (90 days vs 30 days).
                
                **Recommended Remediation:**
                1. **Upgrade Encryption:** Transition from AES-128 to AES-256 immediately.
                2. **Regionalize Storage:** Move PII from the global lake to a region-locked sovereign cloud.
                3. **SLA Alignment:** Revise the 'Right to be Forgotten' workflow to a 30-day purge cycle.
                """)
                st.info("Note: To run this live on your own hardware with private data, clone the repo from GitHub.")

            # CASE 2: Running Locally (Live Mode)
            else:
                try:
                    # Professional Prompt Engineering
                    prompt = f"""
                    System: You are an expert Regulatory Compliance Auditor.
                    Task: Identify specific 'Policy Drift' (conflicts) between the New Regulation and the Internal Policy.
                    
                    New Regulation: {new_reg}
                    Internal Policy: {old_policy}
                    
                    Format your response with:
                    1. Summary of Drift
                    2. Specific Non-Compliant Clauses
                    3. Recommended Remediation (Technical and Operational)
                    """
                    
                    response = ollama.generate(model='phi4-mini', prompt=prompt)
                    
                    st.subheader("✅ Live Audit Report")
                    st.markdown(response['response'])
                
                except Exception as e:
                    st.error(f"Ollama Error: {e}")
                    st.info("Check if 'ollama run phi4-mini' is active in your terminal.")

# --- Footer ---
st.divider()
st.caption("🔒 Privacy Guard: In Local Mode, no data leaves your machine. Designed for Tier-1 Enterprise Security.")
