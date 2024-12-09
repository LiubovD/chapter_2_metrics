import matplotlib.pyplot as plt
import pandas as pd

# get data
df = pd.read_csv("data_table_03_31.csv")

df.plot.scatter('eve_prcnt','TreeMort_1')
plt.show()