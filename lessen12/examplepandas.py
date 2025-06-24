import pandas as pd

produktet=["appels","bananas","oramnges","grapes","pineappeles"]
seles=[150,200,180,90,60]

seles_perproduct=pd.Series(seles,index=produktet)
print(seles_perproduct)
#shitja e rrushit
print(seles_perproduct["grapes"])

best_selling_product=seles_perproduct.idxmax()
print(best_selling_product)

