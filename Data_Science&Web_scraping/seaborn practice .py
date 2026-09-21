import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt 

sns.set_theme(style='whitegrid')

df = pd.read_csv('RealEstate-USA (1).csv', delimiter=',')

print(df.dtypes)
print(df.columns.tolist())

sns.lineplot(x="bed", y="bath", data=df)
plt.show()
input("wait for me...")

sns.scatterplot(data=df, x='price', y='bed')
plt.show()
input("wait for me...")

sns.histplot(data=df, x='price', bins=10)
plt.show()
