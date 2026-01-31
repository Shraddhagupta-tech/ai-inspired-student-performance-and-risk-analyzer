#phase4
# columns tht will be used
# Study_Discipline_Score
# Attendence_Score
# Academic_Score
# for telling if the student is improving or not-Previous_Year_Score

import pandas as pd

df=pd.read_csv(r"data\student_data_features.csv")

study_weight=0.40
attendance_weight=0.20
academic_weight=0.40

df["Performance_Index"]=(df["Study_Discipline_Score"]*study_weight)+(df["Attendance_Score"]*attendance_weight)+(df["Academic_Score"]*academic_weight)
df["Performance_Index"]=df["Performance_Index"].round(2)
df.to_csv(r"data\student_data_indexed.csv", index=False)
print("Performeance index of each student is added to the dataframe.")
