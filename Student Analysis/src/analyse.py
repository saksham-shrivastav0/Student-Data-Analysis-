import numpy as np
import pandas as pd


def get_topper(df):
    res = df[df["Score"] == df["Score"].max()]

    return res


def get_weak_students(df):
    Test_Avg = (df["Test1"] + df["Test2"] + df["Test3"]) / 3
    result = df[((df["Score"] <= 65) & (df["Attendance"] <= 75) & (Test_Avg <= 70))]
    return result
