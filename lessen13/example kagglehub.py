import pandas as  dp
import pandas as pd

df=pd.read_csv("avgIQpercountry.csv")
print(df.info()) # we see the column of this dataset
print(df.head()) #we see the first 5 rows


country_data=df["Country"]
print(country_data)

subset=df[["Country","Average IQ"]]
filtered_DF=subset[subset["Average IQ"]>100]
print(filtered_DF)


#null_mask finding null rows
null_mask=df.isnull()
null_count=null_mask.sum()
print(null_count)


#rmuving dublicates
df.drop_duplicates(keep="first",inplace=True)

df["Population - 2023"]=df["Population - 2023"].apply(lambda x: float(x.reolace(",","")))