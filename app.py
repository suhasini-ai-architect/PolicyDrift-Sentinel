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

# --- Styling ---
st.markdown("""
<style>
.main { background-color: #f5f7f9; }
.stTextArea textarea { font-size: 14px !important; }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ System Arch")

    if IS_HF_SPACE:
        st.success("🌐 Environment: Hugging Face")
        st.caption("Mode: Demo (Simulated)")
    else:
        st.success("💻 Environment: Local")
        st.caption("Mode: Live (Ollama)")

    st.divider()
    st.markdown("### Architect Profile")
    st.write("**Suhasini K.**")
    st.write("Senior Azure Solution Architect")
    st.write("15 YOE Enterprise Architecture")

    st.divider()
    st.info("SLM-powered regulatory gap detection")

    st.warning("⚠️ Demo Mode uses simulated output. Run locally with Ollama for real analysis.")

# --- Header ---
st.title("🛡️ PolicyDrift Sentinel")
st.subheader("Automated Regulatory Compliance & Drift Auditor")

st.info("💡 Tip: Click 'Try Sample Compliance Audit' for instant demo")

# --- Demo Button ---
if st.button("✨ Try Sample Compliance Audit"):
    st.session_state["new_reg"] = "Personal data must not be retained longer than necessary (GDPR Article 5)."
    st.session_state["old_policy"] = "We retain user financial data for 7 years for audit purposes."
    st.session_state["auto_run"] = True

# --- Inputs ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📄 New Regulation (Source A)")
    new_reg = st.text_area(
        "Paste regulation",
        value=st.session_state.get("new_reg", ""),
        height=250
    )

with col2:
    st.markdown("#### 🏢 Internal Policy (Source B)")
    old_policy = st.text_area(
        "Paste policy",
        value=st.session_state.get("old_policy", ""),
        height=250
    )

# --- Run Button ---
run_clicked = st.button("🚀 Analyze Policy Drift", use_container_width=True)

# --- Execution ---
if run_clicked or st.session_state.get("auto_run", False):

    if not new_reg or not old_policy:
        st.warning("Please provide both documents.")
    else:
        with st.spinner("🔄 Analyzing compliance drift..."):

            # --- DEMO MODE (HF or no ollama) ---
            if IS_HF_SPACE or ollama is None:
                time.sleep(1.5)

                st.markdown("## 🔍 Analysis Result")

                st.markdown("### ⚠️ Detected Gap")
                st.error("Data Retention Policy Violation")

                st.markdown("### 📊 Risk Level")
                st.write("HIGH")

                st.markdown("### 📜 Regulation Reference")
                st.write("GDPR Article 5 – Storage Limitation Principle")

                st.markdown("### 🛠️ Recommended Action")
                st.markdown("""
- Define purpose-based retention policy  
- Implement auto-deletion workflows  
- Add audit logging  
- Align retention with regulatory necessity  
                """)

                st.info("This is a simulated demo. Run locally with Ollama for real analysis.")

            # --- LIVE MODE ---
            else:
                try:
                    prompt = f"""
You are an expert Regulatory Compliance Auditor.

Compare the following:

New Regulation:
{new_reg}

Internal Policy:
{old_policy}

Return structured output:
- Detected Gap
- Risk Level
- Regulation Reference
- Recommended Action
"""

                    response = ollama.generate(
                        model='phi4-mini',
                        prompt=prompt
                    )

                    st.markdown("## 🔍 Live Analysis Result")
                    st.markdown(response['response'])

                except Exception as e:
                    st.error("⚠️ Local Model Not Running")

                    st.markdown("""
### 👉 To fix:
1. Install Ollama: https://ollama.com/download  
2. Run: `ollama serve`  
3. Run: `ollama pull phi4-mini`  
4. Restart this app  

### 💡 Note:
App will still work in demo mode on Hugging Face.
                    """)

                    st.caption(f"Debug info: {e}")

        # Reset autorun
        st.session_state["auto_run"] = False

# --- Footer ---
st.divider()
st.caption("🔒 Privacy Guard: In local mode, no data leaves your machine. Built for enterprise-grade compliance.")