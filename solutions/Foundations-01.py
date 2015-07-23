dsk = {'a': (pd.read_csv, filenames[0]),
       'b': (pd.read_csv, filenames[1]),
       'c': (pd.read_csv, filenames[2]),
       'na': (len, 'a'),
       'nb': (len, 'b'),
       'nc': (len, 'c'),
       'total': (sum, ['na', 'nb', 'nc'])}
