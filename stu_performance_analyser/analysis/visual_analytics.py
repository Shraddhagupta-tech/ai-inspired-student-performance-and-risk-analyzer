#phase9
import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv(r'reports\\final_report.csv')

#risk distributionn chart
plt.figure(figsize=(6,4))
risk_counts=(df["Risk_Level"]).value_counts()
colors={'High Risk':'red', 'Low Risk':'green', 'Medium Risk':'yellow'}
plt.bar(risk_counts.index,risk_counts.values, color=[colors[i] for i in risk_counts.index])
plt.xlabel("Risk Level")
plt.ylabel("Number of Students")
plt.title("Risk Distribution Chart")
plt.tight_layout()
plt.savefig(r'visuals\\risk_distribution.png',dpi=300)

#trend distribution chart
plt.figure(figsize=(6,4))
trend_counts=(df["Trend"]).value_counts()
colors={'Declining':'red', 'Improving':'green', 'Stable':'yellow'}
plt.bar(trend_counts.index,trend_counts.values,color=[colors[i] for i in trend_counts.index])
plt.xlabel('Trend')
plt.ylabel('Number of Students')
plt.title("Trend Distribution Chart")
plt.tight_layout()
plt.savefig(r'visuals\\trend_distribution.png',dpi=300)

#performance index vs attendance
plt.figure(figsize=(6,4))
x=df["Attendance_Percentage"]
y=df["Performance_Index"]
colors={'High Risk':'red', 'Low Risk':'green', 'Medium Risk':'yellow'}
plt.scatter(x,y,c=df['Risk_Level'].map(colors),s=10,alpha=0.5)
plt.xlabel('attendance (%)')
plt.ylabel('Performance Index')
plt.title('Performance index vs Attendance(in %)')
plt.tight_layout()
plt.savefig(r'visuals\\performance index vs attendece.png',dpi=300)

#perfornmance index vs study hours per day
plt.figure(figsize=(6,4))
x=df['Study_Hours_Per_Day']
y=df["Performance_Index"]
plt.scatter(x,y,s=10,alpha=0.5)
plt.xlabel('Study Hours per Day')
plt.ylabel('Performance Index')
plt.title('Performance Index vs Study Hours per day')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(r'visuals\\performance index vs study hours.png',dpi=300)
