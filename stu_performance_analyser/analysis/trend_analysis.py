#phase6
#Performance_Index vs Previous_Year_Score

import pandas as pd
import numpy as np
df=pd.read_csv(r'data\student_data_phase5_locked.csv')
df["Difference"]=(((df["Performance_Index"])-(df["Previous_Year_Score"])).round(2))
df["Trend"]= np.select(
    [df["Difference"]>=5,df["Difference"]<=-5],
    ["Improving","Declining"],
    default="Stable"
)
df.to_csv(r"data\student_data_trends.csv",index=False)
print("Dataset was saved as student_data_trends.csv ")