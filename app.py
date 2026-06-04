import streamlit as st
import pandas as pd
from database import addpatient
from database import getpatients
from database import updatepatient
from database import deletepatient
from validation import checkemail
from validation import checkdob

from google import genai

import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
def getremarks(disease, glucose, hemoglobin, cholestrol):

    prompt = f"""
    Disease Prediction: {disease}

    Glucose: {glucose}
    Hemoglobin: {hemoglobin}
    Cholestrol: {cholestrol}

    Write a short health remark.
    keep the remark short and concise.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text

import pickle


with open("healthmodel.pkl", "rb") as f:
    model = pickle.load(f)


def predictdisease(glucose, hemoglobin, cholestrol):

    result = model.predict(
        [[glucose, hemoglobin, cholestrol]]
    )

    return result[0]

st.set_page_config(
    page_title="Health Prediction App",
    layout="wide"
)

st.title("Health Prediction App")

fullname = st.text_input(
    "Full Name"
)

dob = st.date_input(
    "Date of Birth"
)

email = st.text_input(
    "Email"
)

glucose = st.number_input(
    "Glucose",
    min_value=0.0
)

hemoglobin = st.number_input(
    "Hemoglobin",
    min_value=0.0
)

cholestrol = st.number_input(
    "Cholestrol",
    min_value=0.0
)

savebtn = st.button("Predict & Save")

if savebtn:

    if not fullname.strip():

        st.error("Enter full name")

    elif not checkemail(email):

        st.error("Invalid email")

    elif not checkdob(str(dob)):

        st.error("Invalid date of birth")

    else:

        disease = predictdisease(
            glucose,
            hemoglobin,
            cholestrol
        )

        remark = getremarks(
            disease,
            glucose,
            hemoglobin,
            cholestrol
        )

        addpatient(
            fullname,
            str(dob),
            email,
            glucose,
            hemoglobin,
            cholestrol,
            disease,
            remark
        )

        st.success("Record saved")

        st.write("### Disease Prediction")

        st.write(disease)

        st.write("### AI Remark")

        st.write(remark)
        st.divider()

st.subheader("Saved Patient Records")

records = getpatients()

if records:

    df = pd.DataFrame(
        records,
        columns=[
            "ID",
            "Name",
            "DOB",
            "Email",
            "Glucose",
            "Hemoglobin",
            "Cholestrol",
            "Disease",
            "Remark"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )
st.divider()

st.subheader("Patient Records")

if st.button("Show Records"):

    records = getpatients()

    if records:

        df = pd.DataFrame(
            records,
            columns=[
                "ID",
                "Name",
                "DOB",
                "Email",
                "Glucose",
                "Hemoglobin",
                "Cholestrol",
                "Disease",
                "Remark"
            ]
        )

        st.dataframe(df, use_container_width=True)

    else:

        st.info("No records found")

        st.divider()

st.subheader("Update Record")

upid = st.number_input(
    "Patient ID to Update",
    min_value=1,
    step=1
)

upname = st.text_input("New Name")

upemail = st.text_input("New Email")

upglucose = st.number_input(
    "New Glucose",
    min_value=0.0,
    key="upg"
)

uphemo = st.number_input(
    "New Hemoglobin",
    min_value=0.0,
    key="uph"
)

upchol = st.number_input(
    "New Cholestrol",
    min_value=0.0,
    key="upc"
)

if st.button("Update Record"):

    disease = predictdisease(
        upglucose,
        uphemo,
        upchol
    )

    remark = getremarks(
        disease,
        upglucose,
        uphemo,
        upchol
    )

    updatepatient(
        upid,
        upname,
        str(dob),
        upemail,
        upglucose,
        uphemo,
        upchol,
        disease,
        remark
    )

    st.success("Record updated")
    st.divider()

st.subheader("Delete Record")

delid = st.number_input(
    "Patient ID to Delete",
    min_value=1,
    step=1,
    key="delid"
)

if st.button("Delete Record"):

    deletepatient(delid)

    st.success("Record deleted")