# “This app helps educators identify at-risk students, understand causes, and decide actions.”
# columns in final report
# Student_ID
# Class
# Study_Hours_Per_Day
# Attendance_Percentage
# Performance_Index
# Risk_Level
# Trend
# Key_Insight
# Recommendation
import streamlit as st
import pandas as pd


df=pd.read_csv(r"reports\\final_report.csv")

st.title("🎓  AI-Inspired Student Performance and Academic Risk Analyzer")
st.caption("Rule-Based | Explainable | Decision-Intelligence System")

st.sidebar.header("Filters")

risk_options=df["Risk_Level"].unique().tolist()
selected_risk=st.sidebar.multiselect(
    "Risk Level",
    options=risk_options,
    default=risk_options
)

trend_options=df["Trend"].unique().tolist()
selected_trend=st.sidebar.multiselect(
    "Trend",
    options=trend_options,
    default=trend_options
)

class_options=df["Class"].unique().tolist()
selected_class=st.sidebar.multiselect(
    "Class",
    options=class_options,
    default=class_options
)

sort_option=st.sidebar.selectbox(
    "Sort By Performance Index: ",
    options=["None","Ascending","Descending"]
)

selected_id=st.sidebar.text_input("Search By Student ID:")

filtered_data=df[
    (df["Risk_Level"].isin(selected_risk)) &
    (df["Trend"].isin(selected_trend)) &
    (df["Class"].isin(selected_class))
]

if selected_id:
    filtered_data=filtered_data[filtered_data["Student_ID"].astype(str).str.contains(selected_id)]

if sort_option=="Ascending":
    filtered_data=filtered_data.sort_values(by="Performance_Index",ascending=True)
elif sort_option=="Descending":
    filtered_data=filtered_data.sort_values(by="Performance_Index",ascending=False)

st.header("Student Dashboard")
st.write(f"Displaying {len(filtered_data)} students")
st.dataframe(filtered_data)
