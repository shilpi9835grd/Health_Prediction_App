import streamlit as st
import pandas as pd

import database
from ai_prediction import *
from validation import *
from datetime import date

database.create_table()

###new
st.set_page_config(page_title="Health Prediction App",
                   page_icon="🩺",
                   layout="wide")

st.title("🩺 Health Prediction Application")
st.markdown("### AI Powered Blood Test Analysis System")
st.markdown("""
<style>
            
/* Main App Background */
.stApp {background-color: #F8FBFD;}
            
/* Sidebar */
section[data-testid="stSidebar"] {background-color: #D4EEF8;}
            
/* Main Title */
h1 {color: #1F4E79;
    text-align: center;}
            
/* Subtitle */
h3 {color: #2F6FA3;
    text-align: center;}
            
/* Buttons */
div.stButton > button {background-color: #00B4D8;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            border: none;}

/* Button Hover */
div.stButton > button:hover {
            background-color: #0096C7;
            color: white;}

/* Input Boxes */
div[data-baseweb="input"] input {border-radius: 8px;}
            
/* Number Input */
div[data-baseweb="base-input"] {border-radius: 8px;}
    
</style>
""", unsafe_allow_html=True)

menu = [
    "Add Patient",
    "View Patients",
    "Update Patient",
    "Delete Patient"
]

st.sidebar.title("📋Navigation")
choice = st.sidebar.selectbox(
    "Select Option",
    menu
)
st.sidebar.info("Powered by Python + Streamlit + Gemini AI")

# --------------- ADD --------------- #

if choice == "Add Patient":
    st.header("➕ Add New Patient")

    full_name = st.text_input(
        "Full Name"
    )

    dob = st.date_input(
        "Date of Birth",
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

    email = st.text_input(
        "Email"
    )

    glucose = st.number_input(
        "Glucose"
    )

    haemoglobin = st.number_input(
        "Haemoglobin"
    )

    cholesterol = st.number_input(
        "Cholesterol"
    )

    if st.button(
        "🔍 Predict and Save"
    ):

        if full_name.strip() == "":
            
            st.error("Enter Full Name")
        
        elif not validate_email(email):

            st.error(
                "Invalid Email"
            )

        elif not validate_dob(dob):

            st.error(
                "Invalid Date of Birth"
            )
        
        else:

            remarks = predict(
                glucose,
                haemoglobin,
                cholesterol
            )

            database.add_patient(
                full_name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success(
                "✅ Patient Saved Successfully"
            )

            st.info(
                remarks
            )

# ---------------- VIEW --------------- #

elif choice == "View Patients":

    st.header(
        "📄 Patient Records"
    )

    data = database.view_patients()

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Full Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(df)

# --------------- UPDATE --------------- #

elif choice == "Update Patient":

    st.header(
        "✏️ Update Patient Record"
    )

    id = st.number_input(
        "Patient ID",
        min_value=1,
        step=1
    )

    full_name = st.text_input(
        "Full Name"
    )

    dob = st.date_input(
        "Date of Birth",
        value=date(2000, 1, 1),
        min_value=date(1900, 1, 1),
        max_value=date.today()
    )

    email = st.text_input(
        "Email"
    )

    glucose = st.number_input(
        "Glucose"
    )

    haemoglobin = st.number_input(
        "Haemoglobin"
    )

    cholesterol = st.number_input(
        "Cholesterol"
    )

    if st.button(
        "🗳️ Update Record"
    ):
        if full_name.strip() == "":
            
            st.error(
                "Enter Full Name"
                )
        elif not validate_email(email):

            st.error(
                "Invalid Email"
            )

        elif not validate_dob(dob):

            st.error(
                "Invalid Date of Birth"
            )
        else:
            remarks = predict(
               glucose,
               haemoglobin,
               cholesterol)

            database.update_patient(
               id,
               full_name,
               str(dob),
               email,
               glucose,
               haemoglobin,
               cholesterol,
               remarks
        )
            st.success(
               "✅ Record Updated Successfully"
        )
            st.info(
                remarks
            )

# --------------- DELETE --------------- #

elif choice == "Delete Patient":

    st.header(
        "🗑️ Delete Patient"
    )

    id = st.number_input(
        "Enter Patient ID",
        min_value=1,
        step=1
    )

    if st.button(
        "❌ Delete"
    ):
        
        database.delete_patient(
            id
        )

        st.success(
            "✅ Record Deleted Successfully"
        )

