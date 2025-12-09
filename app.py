import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Cognitively Overloaded – materials", page_icon="📊")

st.title("Cognitively Overloaded")
st.write(
    "On this page you can **download the presentation** "
    "and view selected **figures** used in the talk."
)

# -------------------------
# Download button
# -------------------------
pptx_path = Path("mist-orebro-2025-pres-FINAL-streamlit.pptx")

if pptx_path.exists():
    with open(pptx_path, "rb") as f:
        st.download_button(
            label="📥 Download presentation (.pptx)",
            data=f,
            file_name="cognitively-overloaded-orebro-2025.pptx",
            mime=(
                "application/"
                "vnd.openxmlformats-officedocument.presentationml.presentation"
            ),
        )
else:
    st.error("Presentation file not found on the server.")

st.markdown("---")

# -------------------------
# Figures
# -------------------------
st.header("Figures from the study")

# Cesty k obrázkům
fig1 = Path("east-europe-states-cases1.png")
fig2 = Path("east-europe-states-cases2.png")
fig3 = Path("israel-gaza-collocation-stability.png")
fig4 = Path("morphology.png")

# 1. řada – pády
col1, col2 = st.columns(2)

with col1:
    if fig1.exists():
        st.image(str(fig1), use_column_width=True)
        st.caption("Figure 1. Case profiles (NOM–GEN–DAT) of Eastern European states.")

with col2:
    if fig2.exists():
        st.image(str(fig2), use_column_width=True)
        st.caption("Figure 2. Case profiles (ACC–LOC–INST) of Eastern European states.")

# 2. řada – stability + PCA
col3, col4 = st.columns(2)

with col3:
    if fig3.exists():
        st.image(str(fig3), use_column_width=True)
        st.caption("Figure 3. Collocational vs. rank stability (Israel / Gaza).")

with col4:
    if fig4.exists():
        st.image(str(fig4), use_column_width=True)
        st.caption("Figure 4. PCA of morphology indexes (average & SD).")

