from src.load_data import load_students
from src.analyse import get_topper, get_weak_students
from src.predict import get_prediction


import pandas as pd
import numpy as np

ls = load_students("./data/students.csv")
ls["Score"] = (ls["Math"] + ls["Physics"] + ls["Chemistry"] + ls["English"]) / 4
print("===== 📊 STUDENT PERFORMANCE REPORT =====\n")

toppers = get_topper(ls)

topper = ls.loc[ls["Score"].idxmax()]

name = topper["Name"]
score = topper["Score"]

print(f"Topper: {name} (Average Score: {score:.2f})")

weak_students = get_weak_students(ls)
print(f"Weak Students : {weak_students['Name'].tolist()}")

# ls["Prediction"]:
print(
    f"{ls['Name'].iloc[0]} may score : {int(get_prediction(ls.iloc[0]))} in Next Test"
)

# print(ls)
