#phase2
import pandas as pd
import numpy as np

df=pd.read_csv(r"data\Student_Performance_Dataset.csv")
print(df["Student_ID"].count())#5000
df.drop_duplicates(subset=["Student_ID"],keep="first",inplace=True)
df["Pass_Fail_Check"]=np.where(df["Final_Percentage"]<40,
                         "Fail", "Pass")
mismatch_count=(df["Pass_Fail_Check"]!=df["Pass_Fail"]).sum()
print(mismatch_count)#248
df["Pass_Fail_Mismatch"]=df["Pass_Fail_Check"]!=df["Pass_Fail"]
print(df["Pass_Fail_Mismatch"].sum())#248
print(df[df["Pass_Fail_Mismatch"]].head(20))
print(df["Student_ID"].count())#5000
df.to_csv(r"data/student_data_cleaned.csv",index=False)
print("Cleaned data is saved as student_data_cleaned.csv")