import pandas as pd

df=pd.read_csv(r"data\student_data_insight.csv")
df=df[["Student_ID","Class","Study_Hours_Per_Day", "Attendance_Percentage" ,"Performance_Index", "Risk_Level","Trend", "Key_Insight", "Recommendation"]]
df.to_csv(r"reports\\final_report.csv", index=False)
print("Final Report was saved.")