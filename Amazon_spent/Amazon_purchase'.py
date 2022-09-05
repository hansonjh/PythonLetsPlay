# Link to edit more https://www.dataquest.io/blog/how-much-spent-amazon-data-analysis/ 

import pandas as pd
import matplotlib

df = pd.read_csv('Amazon_spent/amazon-orders.csv')
#df.head()
#df.shape
df = df.fillna(0)
#df.head()
#print(df)

df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)
df.head()
df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float)
df.head()
#df['Order Date'] = pd.to_datetime(df['Order Date'])
#df.head()

print(df)

df_tot = df["Total Charged"].sum()

df_tax = df["Tax Charged"].sum()

print("Total money spent", df_tot)
print("Total tax paid", df_tax)

#df.plot.bar(x='Order Date', y='Total Charged', rot=90)