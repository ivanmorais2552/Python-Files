import pandas as pd

park_info = pd.read_csv("InClassWork/national_parks_sample.csv")

print(park_info.at[10, "Park"])
