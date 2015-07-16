# 1. Use the `head()` method to get the first ten rows
df.head()

# 2. Use the `drop_duplicates()` method to find all of the distinct names
df.names.drop_duplicates().compute()

# 3. Use selections `df[...]` to find how many positive and negative amounts
# there are
len(df[df.amount < 0])

# 3. Use selections `df[...]` to find how many positive and negative amounts
# there are
len(df[df.amount > 0])

# 4. Use groupby `df.groupby(df.A).B.func()` to get the average amount per user
# ID
df.groupby(df.names).amount.mean().compute()

# 5. Combine your answers to 3 and 4 to compute the average withdrawal
# (negative amount) per name
df2 = df[df.amount < 0]
df2.groupby(df2.names).amount.mean().compute()
