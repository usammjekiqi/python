import pandas as pd
import matplotlib.pyplot as plt


#geting data from file
df=pd.read_csv("avgIQpercountry.csv")

avg_iq=df.groupby("Countinent")["Average IQ"].mean()

plt.figure(figsize=(10,6))
avg_iq.plot(kind="line",marker="o",color="skyblue")

plt.title("Average IQ by Country")
plt.xlabel("Country")
plt.ylabel("Average")
plt.show()