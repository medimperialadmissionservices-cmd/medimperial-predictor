import streamlit as st
import pandas as pd
import requests

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="MedImperial Predictor", layout="centered")

# -------------------------------
# LOAD DATASET
# -------------------------------
try:
    data = pd.read_csv("colleges.csv")
except:
    st.error("❌ colleges.csv file not found")
    data = pd.DataFrame()

# -------------------------------
# TITLE + LOGO
# -------------------------------
st.image("logo.png", width=120)
st.title("MedImperial NEET Predictor")
st.markdown("🎯 Predict your medical college instantly")

# -------------------------------
# INPUT SECTION
# -------------------------------
rank = st.number_input("Enter your NEET Rank", min_value=1, step=1)

category = st.selectbox(
    "Select Category",
    ["General", "OBC", "SC", "ST"]
)

# -------------------------------
# PREDICTION BUTTON
# -------------------------------
if st.button("🔍 Predict College"):

    if data.empty:
        st.error("Dataset not loaded")
    else:
        possible = data[
            (data["Category"] == category) &
            (data["ClosingRank"] >= rank)
        ]

        if not possible.empty:
            st.success("🎓 Possible Colleges:")

            for i in possible["College"].head(5):
                st.write("👉", i)

        else:
            st.warning("⚠️ Try private colleges or higher budget options")

# -------------------------------
# CTA MESSAGE
# -------------------------------
st.info("📞 For accurate counselling, contact us below")

# -------------------------------
# LEAD FORM
# -------------------------------
st.subheader("📞 Get Personalized Counseling")

name = st.text_input("Your Name")
phone = st.text_input("WhatsApp Number")

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
            response = requests.post(url, json=data_to_send)

            if response.status_code in [200, 201]:
                st.success("✅ Submitted! We will contact you soon")
            else:
                st.error(f"Error: {response.text}")

        except Exception as e:
            st.error(f"Error: {e}")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown("📍 MedImperial Admission Services | 📞 9232119055")