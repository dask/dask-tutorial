import os
import numpy as np
import pandas as pd
from glob import glob


if not os.path.exists('data'):
    os.mkdir('data')


def random_array():
    if os.path.exists(os.path.join('data', 'random.hdf5')):
        return

    print("Create random data for array exercise")
    import h5py

    with h5py.File(os.path.join('data', 'random.hdf5')) as f:
        dset = f.create_dataset('/x', shape=(1000000000,), dtype='f4')
        for i in range(0, 1000000000, 1000000):
            dset[i: i + 1000000] = np.random.exponential(size=1000000)


def accounts_csvs(num_files, n, k):
    from accounts import account_entries, account_params
    fn = os.path.join('data', 'accounts.%d.csv' % (num_files - 1))

    if os.path.exists(fn):
        return

    print("Create CSV accounts for dataframe exercise")

    args = account_params(k)

    for i in range(num_files):
        df = account_entries(n, *args)
        df.to_csv(os.path.join('data', 'accounts.%d.csv' % i),
                  index=False)


def accounts_json(num_files, n, k):
    from accounts import account_params, json_entries
    import json
    import gzip
    fn = os.path.join('data', 'accounts.%02d.json.gz' % (num_files - 1))
    if os.path.exists(fn):
        return

    print("Create JSON accounts for bag exercise")

    args = account_params(k)

    for i in range(num_files):
        seq = json_entries(n, *args)
        fn = os.path.join('data', 'accounts.%02d.json.gz' % i)
        with gzip.open(fn, 'wb') as f:
            f.write(os.linesep.join(map(json.dumps, seq)).encode())


def create_weather(growth=3200):
    filenames = sorted(glob(os.path.join('data', 'weather-small', '*.hdf5')))

    if not os.path.exists(os.path.join('data', 'weather-big')):
        os.mkdir(os.path.join('data', 'weather-big'))

    if all(os.path.exists(fn.replace('small', 'big')) for fn in filenames):
        return

    from scipy.misc import imresize
    import h5py

    for fn in filenames:
        with h5py.File(fn, mode='r') as f:
            x = f['/t2m'][:]

        y = imresize(x, growth)

        out_fn = os.path.join('data', 'weather-big', os.path.split(fn)[-1])

        try:
            with h5py.File(out_fn) as f:
                f.create_dataset('/t2m', data=y, chunks=(500, 500))
        except:
            pass


if __name__ == '__main__':
    random_array()
    create_weather()
    accounts_csvs(3, 1000000, 500)
    accounts_json(50, 100000, 500)
