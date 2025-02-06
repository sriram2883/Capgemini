import pandas as pd

df = pd.read_csv("./Day12/customers-10000.csv")
df[df.Index<100].to_csv("./Day12/output.csv", index=False)
# print(df[df.Index<100].sort_values(by='Index', ascending=False)) sorting

print(df[df.Index<100].groupby('City').sum('Index'))# grouping by city

