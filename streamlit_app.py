import streamlit as st

st.set_page_config(page_title="Ad Split-Test Calculator", layout="centered")
st.title("🎯 Micro-Ad Copy A/B Split-Test Calculator")
st.write("Input your live campaign metrics to calculate the true mathematical winner.")

# Create clean side-by-side input columns
col1, col2 = st.columns(2)

with col1:
    st.header("Ad Creative A")
    clicks_a = st.number_input("Total Clicks (Ad A)", min_value=1, value=120)
    impr_a = st.number_input("Total Impressions (Ad A)", min_value=1, value=5000)
    ctr_a = (clicks_a / impr_a) * 100
    st.metric(label="Click-Through Rate (A)", value=f"{ctr_a:.3f}%")

with col2:
    st.header("Ad Creative B")
    clicks_b = st.number_input("Total Clicks (Ad B)", min_value=1, value=195)
    impr_b = st.number_input("Total Impressions (Ad B)", min_value=1, value=6200)
    ctr_b = (clicks_b / impr_b) * 100
    st.metric(label="Click-Through Rate (B)", value=f"{ctr_b:.3f}%")

st.divider()

# Instant Decision Engine Layout
if ctr_a == ctr_b:
    st.info("⚖️ STATISTICAL TIE: Both ad creatives are performing at identical efficiency metrics.")
elif ctr_a > ctr_b:
    improvement = ((ctr_a - ctr_b) / ctr_b) * 100
    st.success(f"🟢 WINNER: AD CREATIVE A — Outperforming Ad B by {improvement:.1f}% absolute scaling velocity. Scale budget here.")
else:
    improvement = ((ctr_b - ctr_a) / ctr_a) * 100
    st.error(f"🔴 WINNER: AD CREATIVE B — Outperforming Ad A by {improvement:.1f}% absolute scaling velocity. Terminate Ad A budget.")
