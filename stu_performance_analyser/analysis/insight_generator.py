#phase7

# Study_Discipline_Score < 60 → Study issue
# Attendence_Score < 65 → Attendance issue
# Academic_Score < 55 → Conceptual weakness
# Internet_Access = "Yes" AND Academic_Score < 55 → Possible distraction
# Extracurricular_Activities = "Yes" AND Study_Discipline_Score < 60 → Overcommitment risk

# If Academic_Score is lowest → “Academic weakness”
# If Attendance_Score is lowest → “Attendance-driven risk”
# If Study_Discipline_Score is lowest → “Poor study discipline”

# High Risk + Improving → “Recovery potential”
# Medium Risk + Declining → “Early warning”
# Low Risk + Declining → “Hidden risk”
# High Risk + Stable → “Chronic risk”

# Low attendance	Improve class attendance to >75%
# Low study discipline	Increase daily study to minimum 4 hours
# Academic weakness	Focus on core subject remediation

# Internet distraction	Limit non-academic internet usage
# Declining trend	Weekly performance monitoring

import pandas as pd
import numpy as np

df=pd.read_csv(r'data\student_data_trends.csv')

#risk driver,key insight,recommendation

def get_primary_driver(row):
    if row["Study_Discipline_Score"] < 80:
        return "Poor study discipline"
    elif row["Academic_Score"] < 70:
        return "Academic weakness"
    elif row["Attendance_Score"] < 75:
        return "Low attendance"
    else:
        return ""  # no driver if all scores are okay

df["Primary_Driver"] = df.apply(get_primary_driver, axis=1)


def generate_modifier(row):
    modifiers=[]
    if row["Internet_Access"]=="Yes" and row["Academic_Score"]<55:
        modifiers.append('Possible distraction')
    if row["Extracurricular_Activities"]=="Yes" and row["Study_Discipline_Score"]<60:
        modifiers.append('Overcommitment')
    return " and ".join(modifiers)
    
df["Modifiers"]=df.apply(generate_modifier,axis=1)

def generate_insight(row):
    text=f"{row['Primary_Driver']} is the primary cause of academic risk"
    if row["Trend"]=="Declining":
        text += " reinforced by declining performance trend"
    if row["Risk_Level"]=="High Risk":
        text=text.replace("academic risk","high academic risk")
    if "Possible distraction" in row["Modifiers"]:
            text += " and possible distraction from internet use"
    if "Overcommitment" in row["Modifiers"]:
            text += " and overcommitment to extracurricular activities"
    return text+"."

df["Key_Insight"]=df.apply(generate_insight,axis=1)


conditions1=[df["Primary_Driver"]=="Poor study discipline",
            df["Primary_Driver"]=="Academic weakness",
            df["Primary_Driver"]=="Low attendance"]
choices1=["Increase daily study to minimum 4 hours",
         "Focus on core subject remediation",
         "Improve class attendance to >75%"]
df["Primary_Recommendation"]=np.select(conditions1,choices1,default="")

conditions2=[df["Modifiers"].str.contains("Possible distraction", na=False ),
             df["Trend"]=="Declining",
             df["Modifiers"].str.contains("Overcommitment", na=False)]
choices2=["Limit non-academic internet usage",
          "Do weekly performance monitoring",
          "Reduce extracurricular load temporarily"]
df["Secondary_Recommendation"]=np.select(conditions2,choices2,default="")

df["Recommendation"] = np.where(
    (df["Primary_Recommendation"] == "") & (df["Secondary_Recommendation"] == ""),
    "Maintain Current Habits",
    np.where(
        df["Primary_Recommendation"] != "",
        "1. " + df["Primary_Recommendation"] + "." +
        np.where(
            df["Secondary_Recommendation"] != "",
            "\n2. " + df["Secondary_Recommendation"] + ".",
            ""
        ),
        "2. " + df["Secondary_Recommendation"] + "."  # only secondary exists
    )
)


lowrisk= df["Risk_Level"]=="Low Risk"
df.loc[lowrisk,"Primary_Driver"]=""
df.loc[lowrisk,"Key_Insight"]="Strong overall performance with no immediate academic risk."
df.loc[lowrisk,"Primary_Recommendation"]="Maintain current study and attendance habits."
df.loc[lowrisk,"Secondary_Recommendation"]=""
df.to_csv(r'data\student_data_insight.csv',index=False)
print("Data was saved as student_data_insight")