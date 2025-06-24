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

#df["Population - 2023"]=df["Population - 2023"].apply(lambda x: float(x.reolace(",","")))


#fining the avg of continent
avg_iq_per_contry=df.groupby('Continent')["Average IQ"].mean()

avg_iq_per_contry=avg_iq_per_contry.sort_values(ascending=False)

print(avg_iq_per_contry)


#calculate nobel prizes by country nad show countries only with more than 1 nobel
# you have to use group by , sum and sort values

#nobel_per_contry=df.groupby('Country ')['Noble Prices'].count()
#print(nobel_per_contry)



