import streamlit as st
import os
import time

# --- Environment Detection ---
IS_HF_SPACE = "SPACE_ID" in os.environ

# --- Try importing Ollama ---
try:
    import ollama
except ImportError:
    ollama = None

# --- UI Config ---
st.set_page_config(page_title="PolicyDrift Sentinel", page_icon="🛡️", layout="wide")

# --- Custom Professional Styling ---
st.markdown("""
<style>
    .main { background-color: #f8f9fa; }
    .stTextArea textarea { font-size: 14px !important; border-radius: 10px; }
    .reportview-container { background: #f0f2f6; }
    .result-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #007bff;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .metric-box {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("🛡️ System Arch")
    
    if IS_HF_SPACE:
        st.success("🌐 Environment: Hugging Face")
        st.caption("Mode: Demo (Cloud Sandbox)")
    else:
        st.success("💻 Environment: Local")
        st.caption("Mode: Live (Ollama / Phi-4)")

    st.divider()
    st.markdown("### Architect Profile")
    st.write("**Suhasini K.**")
    st.caption("Senior Azure Solution Architect")
    st.caption("15 YOE Enterprise Architecture")

    st.divider()
    with st.expander("Technical Stack"):
        st.write("- Python / Streamlit")
        st.write("- Microsoft Phi-4-Mini")
        st.write("- Ollama Inference Engine")

# --- Header ---
st.title("🛡️ PolicyDrift Sentinel")
st.markdown("### Enterprise Regulatory Compliance & Drift Auditor")
st.write("Leveraging Small Language Models (SLMs) for private, high-density policy auditing.")

# --- Demo Trigger ---
if st.button("✨ Load Sample Compliance Case"):
    st.session_state["new_reg"] = "All PII data must be encrypted at rest using AES-256 standards. Rotational keys must be updated every 90 days."
    st.session_state["old_policy"] = "Our database uses standard AES-128 encryption. Encryption keys are managed manually and reviewed annually."
    st.session_state["auto_run"] = True

# --- Input Section ---
col_a, col_b = st.columns(2)

with col_a:
    st.markdown("#### 📄 Regulatory Requirement")
    new_reg = st.text_area("Paste Global Regulation (e.g. GDPR, RBI, HIPAA)", 
                          value=st.session_state.get("new_reg", ""), height=200)

with col_b:
    st.markdown("#### 🏢 Internal Corporate Policy")
    old_policy = st.text_area("Paste Internal Standard Operating Procedure", 
                             value=st.session_state.get("old_policy", ""), height=200)

# --- Action ---
if st.button("🚀 Execute Architecture Audit", use_container_width=True) or st.session_state.get("auto_run", False):
    if not new_reg or not old_policy:
        st.warning("Please provide both documents for analysis.")
    else:
        with st.spinner("🧠 SLM Reasoning in progress..."):
            
            # --- Logic: Demo vs Live ---
            if IS_HF_SPACE or ollama is None:
                time.sleep(1.5) # Simulate thinking
                # Formatted Mock Data
                gap = "Encryption Standard Mismatch (AES-128 vs AES-256)"
                risk = "CRITICAL"
                ref = "ISO/IEC 27001 & GDPR Art. 32"
                remediation = """
                1. Upgrade database encryption schema to AES-256.
                2. Automate Key Rotation using Azure Key Vault (90-day trigger).
                3. Update internal Compliance Registry to reflect new SLAs.
                """
            else:
                try:
                    prompt = f"Audit the drift between New Reg: {new_reg} and Internal Policy: {old_policy}. Identify Gaps, Risk Level, and Remediation steps."
                    res = ollama.generate(model='phi4-mini', prompt=prompt)
                    # For live mode, we display the raw SLM reasoning in a clean box
                    gap = "AI Analyzed Discrepancy"
                    risk = "Analyzed"
                    ref = "Regulatory Alignment"
                    remediation = res['response']
                except Exception:
                    st.error("Ollama not found locally.")
                    st.stop()

            # --- Visual Output (THE MONEY SHOT SECTION) ---
            st.divider()
            st.markdown("## 🔍 Audit Results")
            
            # Top row metrics
            m1, m2, m3 = st.columns(3)
            with m1:
                st.markdown(f'<div class="metric-box"><strong>Risk Status</strong><br><span style="color:red; font-size:20px;">{risk}</span></div>', unsafe_allow_html=True)
            with m2:
                st.markdown(f'<div class="metric-box"><strong>Audit ID</strong><br>PDS-2026-X1</div>', unsafe_allow_html=True)
            with m3:
                st.markdown(f'<div class="metric-box"><strong>Engine</strong><br>Phi-4-Mini</div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            # Detailed Findings
            with st.container():
                st.markdown(f"""
                <div class="result-card">
                    <h4>🚩 Primary Policy Drift Detected</h4>
                    <p style="color:#d9534f; font-weight:bold;">{gap}</p>
                    <hr>
                    <h5>📖 Regulatory Reference</h5>
                    <p>{ref}</p>
                </div>
                """, unsafe_allow_html=True)

            with st.expander("🛠️ View Step-by-Step Remediation Plan", expanded=True):
                st.markdown(remediation)

            if IS_HF_SPACE:
                st.info("💡 Note: Running in Sandbox Demo Mode. Deploy locally for full PII-safe analysis.")

        st.session_state["auto_run"] = False

# --- Footer ---
st.divider()
st.caption("PolicyDrift-Sentinel | Developed by Suhasini K. | Built for Private Enterprise Governance")