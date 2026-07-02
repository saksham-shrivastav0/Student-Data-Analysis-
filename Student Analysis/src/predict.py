import pandas as pd
import numpy as np


def get_prediction(df):
    rate = df["Test2"] - (df["Test1"] + df["Test2"] + df["Test3"]) / 3
    res = df["Test3"] + rate
    return res
