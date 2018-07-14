import os
import numpy as np
import pandas as pd
from glob import glob
import tarfile
import urllib.request
import zipfile

here = os.path.dirname(__file__)

data_dir = os.path.abspath(os.path.join(here, 'data'))
if not os.path.exists(data_dir):
    raise OSError('data/ directory not found, aborting data preparation. ' \
                  'Restore it with "git checkout data" from the base ' \
                  'directory.')


def flights():
    flights_raw = os.path.join(data_dir, 'nycflights.tar.gz')
    flightdir = os.path.join(data_dir, 'nycflights')
    jsondir = os.path.join(data_dir, 'flightjson')

    if not os.path.exists(flights_raw):
        print("- Downloading NYC Flights dataset... ", end='', flush=True)
        url = "https://storage.googleapis.com/dask-tutorial-data/nycflights.tar.gz"
        urllib.request.urlretrieve(url, flights_raw)
        print("done", flush=True)

    if not os.path.exists(flightdir):
        print("- Extracting flight data... ", end='', flush=True)
        tar_path = os.path.join(data_dir, 'nycflights.tar.gz')
        with tarfile.open(tar_path, mode='r:gz') as flights:
            flights.extractall('data/')
        print("done", flush=True)

    if not os.path.exists(jsondir):
        print("- Creating json data... ", end='', flush=True)
        os.mkdir(jsondir)
        for path in glob(os.path.join(data_dir, 'nycflights', '*.csv')):
            prefix = os.path.splitext(os.path.basename(path))[0]
            # Just take the first 10000 rows for the demo
            df = pd.read_csv(path).iloc[:10000]
            df.to_json(os.path.join(data_dir, 'flightjson', prefix + '.json'),
                       orient='records', lines=True)
        print("done", flush=True)

    print("** Finished! **")

def random_array():
    if os.path.exists(os.path.join(data_dir, 'random.hdf5')):
        return

    print("Create random data for array exercise")
    import h5py

    with h5py.File(os.path.join(data_dir, 'random.hdf5')) as f:
        dset = f.create_dataset('/x', shape=(1000000000,), dtype='f4')
        for i in range(0, 1000000000, 1000000):
            dset[i: i + 1000000] = np.random.exponential(size=1000000)


def accounts_csvs(num_files, n, k):
    from accounts import account_entries, account_params
    fn = os.path.join(data_dir, 'accounts.%d.csv' % (num_files - 1))

    if os.path.exists(fn):
        return

    print("Create CSV accounts for dataframe exercise")

    args = account_params(k)

    for i in range(num_files):
        df = account_entries(n, *args)
        df.to_csv(os.path.join(data_dir, 'accounts.%d.csv' % i),
                  index=False)


def accounts_json(num_files, n, k):
    from accounts import account_params, json_entries
    import json
    import gzip
    fn = os.path.join(data_dir, 'accounts.%02d.json.gz' % (num_files - 1))
    if os.path.exists(fn):
        return

    print("Create JSON accounts for bag exercise")

    args = account_params(k)

    for i in range(num_files):
        seq = json_entries(n, *args)
        fn = os.path.join(data_dir, 'accounts.%02d.json.gz' % i)
        with gzip.open(fn, 'wb') as f:
            f.write(os.linesep.join(map(json.dumps, seq)).encode())


def create_weather(growth=32):
    filenames = sorted(glob(os.path.join(data_dir, 'weather-small', '*.hdf5')))

    if not filenames:
        ws_dir = os.path.join(data_dir, 'weather-small')
        raise ValueError('Did not find any hdf5 files in {}'.format(ws_dir))

    if not os.path.exists(os.path.join(data_dir, 'weather-big')):
        os.mkdir(os.path.join(data_dir, 'weather-big'))

    if all(os.path.exists(fn.replace('small', 'big')) for fn in filenames):
        return

    from skimage.transform import resize
    import h5py

    print('Exploding weather data')
    for fn in filenames:
        with h5py.File(fn, mode='r') as f:
            x = f['/t2m'][:]

        y = resize(x, (x.shape[0] * 32, x.shape[1] * 32), mode='constant')

        out_fn = os.path.join(data_dir, 'weather-big', os.path.split(fn)[-1])

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
    flights()
