import seaborn as sns 
import matplotlib .pyplot as plt
import pandas as pd 

tips = sns.load_dataset("tips")
print(tips.head())

sns.scatterplot(data = tips , x = "total_bill" , y = "tip")
plt.show()

# Line Plot

flights = sns.load_dataset("flights")
sns.lineplot(data = flights , x = "year" , y = "passengers")
plt.show()

# Bar Plot

sns.barplot(data= tips , x = "day" , y = "total_bill")
plt.show()

# Histogram / Distribution

sns.histplot(data=tips , x="total_bill" , bins=20 , kde = True)
plt.show()

# Box Plot
sns.boxplot(data = tips , x="day" , y="total_bill")
plt.show()

# Rang aur Style (hue aur style)
sns.scatterplot(data=tips , x="total_bill", y="tip" , hue="sex" , style="time")
plt.show()

# Multiple Plots ek sath (relplot with col)
sns.relplot(data=tips , x="total_bill", y="tip" , col="day", hue="sex")
plt.show()

# Pairplot (Sara Dataset Ek Nazar Mein)
sns.pairplot(tips, hue="sex")
plt.show()

#  Heatmap (Correlation Dekhne Ke Liye)
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True , cmap="coolwarm")
plt.show()

# Violin Plot

sns.violinplot(data=tips , x="day" , y = "total_bill")
plt.show

# Style aur Themes (Graph Khoobsurat Banana)
sns.set_style("darkgrid")
sns.set_palette("pastel")

# Countplot (Ginti Dikhane Ke Liye)
sns.countplot(data=tips , x="day")
plt.show()

# Jointplot (Do Graphs Ek Sath)

sns.jointplot(data=tips , x = "total_bill", y="tip", kind="scatter")
plt.show()

# Lesson 16: Catplot (Sab Category Plots Ek Function Mein)

sns.catplot(data=tips, x="day", y="total_bill", kind="swarm", col="sex")
plt.show() 

# Graph Ko Save Karna

sns.boxplot(data=tips, x='day', y='total_bill')
plt.savefig("boxplot.png" , dpi=300 , bbox_inches="tight")
plt.show()

# Subplots — Practice Se Samjho

fig , axes = plt.subplot(1,2,figsize = (12,5))

sns.boxplot(data=tips,x="day",y= "total_bill", ax = axes[0])
axes[0].set_title("Toatal Bill by Day")

sns.violinplot(data=tips , x="day" , y = "tip" , ax = axes[1])
axes[1].set_title("Tip by Day")

plt.tight_layout()
plt.show()

# Poori Figure Ka Title (Sab Graphs Ke Upar)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(data=tips, x="day", y="total_bill", ax=axes[0])
sns.violinplot(data=tips, x="day", y="tip", ax=axes[1])

fig.suptitle("Restaurant Tips Analysis", fontsize=16)
plt.tight_layout()
plt.show()

# FacetGrid (Detail Mein)

g = sns.FacetGrid(tips,col="day",row="sex")
g.map(sns.scatterplot, "total_bill" , "tip")
plt.show() 

