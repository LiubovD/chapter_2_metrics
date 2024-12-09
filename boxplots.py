import pandas as pd
import matplotlib as plt
import seaborn as sns

# get data
df = pd.read_csv("points_NDVI.csv")

print(df.head())
print(df.columns)
list_columns = list(df.columns)
list_columns.remove('OID_')
list_columns.remove('Id')
print(list_columns)
dict = {}
for i in list_columns:
    dict[i] = []
print(dict)

for name in list_columns:
    if df["Id"] == 0:
        dict[name].append(df[name])
        print(dict[name])

    # if df["Id"] == 0:
    #     df[name]
    # elif df["Id"] == 1:
    #     df[name]
    # elif df["Id"] == 2:
    #     df[name]
    # elif df["Id"] == 3:
    #     df[name]