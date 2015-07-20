import os
import numpy as np
import pandas as pd

if not os.path.exists('data'):
    os.mkdir('data')

def random_array():
    if not os.path.exists(os.path.join('data', 'random.hdf5')):

        import h5py

        with h5py.File(os.path.join('data', 'random.hdf5')) as f:
            dset = f.create_dataset('/x', shape=(1000000000,), dtype='f4')
            for i in range(0, 1000000000, 1000000):
                dset[i: i + 1000000] = np.random.exponential(size=1000000)


def accounts_csvs(num_files, n, k):
    from accounts import account_entries, account_params
    fn = os.path.join('data', 'accounts.%d.csv' % (num_files - 1))

    if not os.path.exists(fn):
        args = account_params(k)

        for i in range(num_files):
            df = account_entries(n, *args)
            df.to_csv(os.path.join('data', 'accounts.%d.csv' % i),
                      index=False)
