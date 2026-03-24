import urllib.parse
import streamlit as st
import pandas as pd
import requests

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="MedImperial Predictor", layout="centered")

# -------------------------------
# CUSTOM PREMIUM CSS
# -------------------------------
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
    height: 3em;
    width: 100%;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #3c6382;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.success-box {
    background-color: #d4edda;
    padding: 15px;
    border-radius: 10px;
}
.warning-box {
    background-color: #fff3cd;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD DATA
# -------------------------------
try:
    data = pd.read_csv("colleges.csv")
except:
    st.error("❌ colleges.csv file not found")
    data = pd.DataFrame()

# -------------------------------
# HEADER
# -------------------------------
st.image("logo.png", width=120)
st.markdown("<h1>MedImperial NEET Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>🎯 Predict your medical college instantly</p>", unsafe_allow_html=True)

# -------------------------------
# INPUT CARD
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

rank = st.number_input("Enter your NEET Rank", min_value=1, step=1)

category = st.selectbox(
    "Select Category",
    ["General", "OBC", "SC", "ST"]
)

if st.button("🔍 Predict College"):
    if data.empty:
        st.error("Dataset not loaded")
    else:
        possible = data[
            (data["Category"] == category) &
            (data["ClosingRank"] >= rank)
        ]

        if not possible.empty:
            st.markdown('<div class="success-box">🎓 Possible Colleges:</div>', unsafe_allow_html=True)
            for i in possible["College"].head(5):
                st.write("👉", i)
        else:
            st.markdown('<div class="warning-box">⚠️ Try private colleges or higher budget options</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# CTA
# -------------------------------
st.markdown("### 📞 Get Personalized Counseling")

st.markdown('<div class="card">', unsafe_allow_html=True)

name = st.text_input("Your Name")
phone = st.text_input("WhatsApp Number")

import urllib.parse

if st.button("🚀 Submit Details"):

    if name == "" or phone == "":
        st.warning("Please fill all details")
    else:
        url = "https://sheetdb.io/api/v1/p8w5tq1ash2sh"

        data_to_send = {
            "data": [{
                "Name": name,
                "Phone": phone,
                "Rank": rank,
                "Category": category
            }]
        }

        try:
            requests.post(url, json=data_to_send)

            message = f"""
Hi, I checked my NEET rank.

Name: {name}
Rank: {rank}
Category: {category}

I want full counselling (₹999).
"""

            encoded_message = urllib.parse.quote(message)

            whatsapp_number = "919232119055"

            whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"

            st.markdown(f"""
                <meta http-equiv="refresh" content="2;url={whatsapp_url}">
            """, unsafe_allow_html=True)

            st.success("Redirecting to WhatsApp...")

        except:
            st.error("Error")

                # -------------------------------
                # WHATSAPP AUTO MESSAGE
                # -------------------------------
                message = f"""
Hello MedImperial,

My Name: {name}
NEET Rank: {rank}
Category: {category}

Please guide me for admission.
"""

                encoded_message = urllib.parse.quote(message)

                whatsapp_number = "919232119055"  # your number (91 + number)

                whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"

                st.markdown(f"[👉 Click here to WhatsApp us](%s)" % whatsapp_url)

            else:
                st.error("Error saving data")

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("<center>📍 MedImperial Admission Services | 📞 9232119055</center>", unsafe_allow_html=True)