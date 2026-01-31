#phase1
import pandas as pd

df=pd.read_csv(r"data\Student_Performance_Dataset.csv")
print(df)
print(df.info())
print(df.head())
print(df.isnull().sum())
print((df["Student_ID"]).is_unique)
print((df["Age"]).max()) #19
print((df["Age"]).min()) #14
print((df["Class"]).max()) #12
print((df["Class"]).min()) #9
print((((df["Study_Hours_Per_Day"]<0) | (df["Study_Hours_Per_Day"]>12.0))  == True).sum())#0
print(((df["Attendance_Percentage"])>100).sum())#0
print((df[["Math_Score","Science_Score","English_Score","Previous_Year_Score","Final_Percentage"]]>100).sum())#0
print((((df["Gender"]=="Male") | (df["Gender"]=="Female"))==False).sum()) #0
print((((df["Internet_Access"]=="Yes") | (df["Internet_Access"]=="No"))==False).sum())#0
