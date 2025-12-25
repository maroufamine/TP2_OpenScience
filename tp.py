import pandas as pd
df = pd.read_csv("data_biology.csv")
df
df.info()
df.describe()
df[["cell_count", "protein_level"]]
treated = df[df["group"] == "Treated"]
treated
import numpy as np
np.mean(df["cell_count"])
np.std(df["cell_count"])
df.groupby("group")["cell_count"].mean()
df["normalized_growth"] = df["growth_rate"] / df["growth_rate"].max()
df
high_protein = np.where(df["protein_level"] > 3.0, "High", "Normal")
df["protein_status"] = high_protein
df
import matplotlib.pyplot as plt
df.plot(kind="bar", x="sample", y="cell_count")
plt.show()
df.boxplot(column="cell_count", by="group")
plt.title("Cell count by group")
plt.suptitle("")
plt.show()
df.plot(kind="scatter", x="temperature", y="growth_rate")
plt.show()
data_np = df[["cell_count", "protein_level", "growth_rate"]].to_numpy()
data_np
df[["cell_count", "protein_level", "growth_rate"]].corr()
df.to_csv("results_biology.csv", index=False)