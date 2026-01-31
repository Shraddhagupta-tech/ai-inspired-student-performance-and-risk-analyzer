#phase5
import pandas as pd
import numpy as np

df=pd.read_csv(r"data\student_data_indexed.csv")
df["Risk_Level"]=np.select(
    [df["Performance_Index"]<45,df["Performance_Index"]>=65],
    ["High Risk","Low Risk"],
    default="Medium Risk"
)

df=df.drop(['Age', 'Gender','Parental_Education', 'Final_Percentage',
       'Performance_Level', 'Pass_Fail', 'Pass_Fail_Check',
       'Pass_Fail_Mismatch'],axis=1)
print(df.columns)
df.to_csv(r"data\student_data_phase5_locked.csv",index=False)
print("Student data was saved sucessfully.")