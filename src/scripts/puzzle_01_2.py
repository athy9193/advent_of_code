import numpy as np
import pandas as pd

df = pd.read_csv("inputs/puzzle_01_input.csv", header=None)  # path from root

arr = df.T.to_numpy()[0]

sum_3 = np.convolve(arr, np.ones(3, dtype=int), mode="valid")
# ref: https://stackoverflow.com/questions/42472104/finding-the-sum-of-3-consecutive-numbers-in-an-array/42472226

print("Number of sums that are larger than the previous sum is:")
print(np.sum(np.diff(sum_3) > 0))
