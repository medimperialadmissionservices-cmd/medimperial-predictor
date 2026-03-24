import requests
import streamlit as st
import pandas as pd
import os

# Page config
st.set_page_config(page_title="MedImperial Predictor", layout="centered")

# Custom CSS (premium look)
st.markdown("""
<style>
body {
    background-color: #f5f9ff;
}
.main {
    background-color: #f5f9ff;
}
h1 {
    color: #0a3d62;
    text-align: center;
}
.stButton>button {
    background-color: #0a3d62;
    color: white;
    border-radius: 10px;
    height: 45px;
    width: 100%;
}
.stTextInput>div>div>input {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# Logo + Title (centered)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image("logo.png", width=120)
    st.markdown("<h1>MedImperial NEET Predictor</h1>", unsafe_allow_html=True)

st.markdown("### 🎯 Predict your medical college instantly")

# Input section
rank = st.number_input("Enter your NEET Rank", min_value=1)
category = st.selectbox("Select Category", ["General", "OBC", "SC", "ST"])

# Predict
if st.button("🔍 Predict College"):
    st.success("🎓 You may get a good medical college")
    st.warning("⚠️ For accurate counseling, contact us below")

# Lead form
st.markdown("## 📞 Get Personalized Counseling")

name = st.text_input("Your Name")
phone = st.text_input("WhatsApp Number")

if st.button("🚀 Submit Details"):

    if name == "" or phone == "":
        st.warning("Please fill all details")
    else:
        data = {
            "data": [{
                "Name": name,
                "Phone": phone,
                "Rank": rank,
                "Category": category
            }]
        }

        url = "https://sheetdb.io/api/v1/p8w5tq1ash2sh"

        try:
            response = requests.post(url, json=data)

            # 👇 IMPORTANT CHANGE
            if response.status_code in [200, 201]:
                st.success("✅ Submitted! We will contact you soon")
            else:
                st.error(f"Error: {response.text}")

        except Exception as e:
            st.error(f"Error: {e}")

url = "https://sheetdb.io/api/v1/p8w5tq1ash2sh"
# Footer
st.markdown("---")
st.markdown("📍 MedImperial Admission Services | 📞 9232119055")