sums = []
for i in range(0, 1000000000, 1000000):
    chunk = dset[i: i + 1000000]  # pull out numpy array
    sums.append((chunk > 1).sum())

total = sum(sums)
print(total)
