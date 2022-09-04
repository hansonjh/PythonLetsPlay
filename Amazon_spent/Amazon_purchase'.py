import pandas as pd

df = pd.read_csv('amazon-orders.csv')
df.head()
df.shape

df = df.fillna(0)
df.head()

#print(df)

df["Total Charged"] = df["Total Charged"].str.replace('$','').astype(float)

df["Tax Charged"] = df["Tax Charged"].str.replace('$','').astype(float)
df.head()

print(df)

df_tot = df["Total Charged"].sum()

df_tax = df["Tax Charged"].sum()

print("Total money spent", df_tot)
print("Total tax paid", df_tax)
