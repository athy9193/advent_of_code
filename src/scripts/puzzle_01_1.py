import numpy as np
import pandas as pd

df = pd.read_csv("inputs/puzzle_01_input.csv", header=None)  # path from root

df["diff"] = df[0].diff(periods=1)

print("Number of measurements are larger than the previous measurement:")

print(df.query("diff>0").shape[0])
