#phase3
import pandas as pd
import numpy as np
df=pd.read_csv(r"data\student_data_cleaned.csv")
#columns that will be used to calculate
# Study_Hours_Per_Day
# Attendance_Percentage
# Math_Score
# Science_Score
# English_Score
#only to explain the risk
# Internet_Access
# Internet_Access
# Extracurricular_Activities
#for reporting -Student_ID,Class
#for telling if the student is improving or not
# Previous_Year_Score

df["Study_Discipline_Score"]= np.where(
    df["Study_Hours_Per_Day"]<4,
    (df["Study_Hours_Per_Day"]/4*100),100
)
df["Study_Discipline_Score"]=df["Study_Discipline_Score"].clip(0,100)
df["Attendance_Score"]=df["Attendance_Percentage"]
df["Academic_Score"]=(df[["Math_Score" ,"Science_Score", "English_Score"]].mean(axis=1)).round(2)
df.to_csv(r"data/student_data_features.csv",index=False)
print('Featured data saved.')





