import streamlit as st
import pandas as pd
import requests
from datetime import datetime
import urllib.parse

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="MedImperial Predictor", layout="centered")

# ---------- PREMIUM UI ----------
st.markdown("""
<style>
body {
    background-color: #f5f9ff;
}
h1 {
    text-align: center;
    color: #0a3d62;
    font-weight: bold;
}
.stButton>button {
    background-color: #0a3d62;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
}
.success-box {
    background-color: #d4edda;
    padding: 12px;
    border-radius: 8px;
    color: #155724;
}
.warning-box {
    background-color: #fff3cd;
    padding: 12px;
    border-radius: 8px;
    color: #856404;
}
</style>
""", unsafe_allow_html=True)

# ---------- LOGO ----------
st.image("logo.png", width=120)

# ---------- TITLE ----------
st.markdown("<h1>MedImperial NEET Predictor</h1>", unsafe_allow_html=True)
st.write("🎯 Predict your medical college instantly")

# ---------- INPUT ----------
rank = st.number_input("Enter your NEET Rank", min_value=1)
category = st.selectbox("Select Category", ["General", "OBC", "SC", "ST"])

# ---------- PREDICTION ----------
if st.button("🔍 Predict College"):
    if rank < 10000:
        st.success("🎓 Top Government College Possible")
    elif rank < 50000:
        st.success("🏥 Good Government College Possible")
    else:
        st.warning("⚠️ Private College Recommended")

    st.markdown('<div class="warning-box">⚠️ For accurate counseling, contact us below</div>', unsafe_allow_html=True)

# ---------- LEAD FORM ----------
st.markdown("## 📞 Get Personalized Counseling")

name = st.text_input("Your Name")
phone = st.text_input("WhatsApp Number")

# ---------- YOUR SHEETDB API ----------
url = "https://sheetdb.io/api/v1/1oz67ycjlmrr0"

if st.button("🚀 Submit Details"):
    if name and phone:

        # ---------- DATA ----------
        data = {
            "data": [{
                "name": name,
                "phone": phone,
                "rank": str(rank),
                "category": category,
                "time": str(datetime.now())
            }]
        }

        try:
            response = requests.post(url, json=data)

            # ---------- DEBUG ----------
            # st.write(response.text)

            if response.status_code == 201:
                st.success("✅ Details submitted successfully!")

                # ---------- WHATSAPP ----------
                whatsapp_number = "919232119055"

                message = f"""Hello MedImperial,
I am {name}.
My NEET Rank: {rank}
Category: {category}
I need counseling."""

                encoded_message = urllib.parse.quote(message)
                whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"

                # ---------- BUTTON ----------
                st.markdown(f"""
                <a href="{whatsapp_url}" target="_blank">
                    <button style="
                        background-color:#25D366;
                        color:white;
                        padding:12px 20px;
                        border:none;
                        border-radius:8px;
                        font-size:16px;
                        font-weight:bold;
                        cursor:pointer;">
                        📲 Continue to WhatsApp
                    </button>
                </a>
                """, unsafe_allow_html=True)

            else:
                st.error("❌ Error saving data")
                st.write(response.text)  # shows actual error

        except Exception as e:
            st.error("❌ Connection error")
            st.write(e)

    else:
        st.warning("⚠️ Please fill all details")

# ---------- FOOTER ----------
st.markdown("---")
st.write("📍 MedImperial Admission Services | 📞 9232119055")