dsk = dict()

for i in range(3):
    dsk[('df', i)] = (pd.read_csv, filenames[i])
    dsk[('sum', i)] = (amount_sum, ('df', i))

dsk['total'] = (sum, [('sum', i) for i in range(3)])
