import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()

titles_soil_dt = pd.read_csv("D:\Luba\chapter2\project_deadtrees_factoring\MyProject6\dataset_09_26.csv")


titles_soil_dt.drop(["OID_"], axis=1, inplace=True)
#titles_soil_dt.drop( ['ID'], axis=1, inplace=True)
print(titles_soil_dt.head())
sns.set_theme(style="ticks", color_codes=True)

sns.catplot(data=titles_soil_dt, x="TreeMort_3", y="bedrock_pr", kind="box")
plt.show()

#titles_soil_dt.loc[:, 'TreeMortal'].plot.hist(bins=6)
#plt.show()

#null = pd.plotting.scatter_matrix(titles_soil_dt, figsize = [10,10])
#plt.show()

#sns.pairplot(titles_soil_dt, hue="ID", height = 2)
#plt.show()

