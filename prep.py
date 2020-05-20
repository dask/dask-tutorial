import time
import sys
import argparse
import os
from glob import glob
import json
import gzip
import tarfile
import urllib.request

import h5py
import numpy as np
import pandas as pd
from skimage.transform import resize

from accounts import account_entries, account_params, json_entries

import sources

DATASETS = ["random", "weather", "accounts", "flights", "all"]
here = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(here, 'data'))


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Downloads, generates and prepares data for the Dask tutorial.')
    parser.add_argument('--no-ssl-verify', dest='no_ssl_verify', action='store_true',
                        default=False, help='Disables SSL verification.')
    parser.add_argument("--small", action="store_true", default=None,
                        help="Whether to use smaller example datasets. Checks DASK_TUTORIAL_SMALL environment variable if not specified.")
    parser.add_argument("-d", "--dataset", choices=DATASETS, help="Datasets to generate.", default="all")

    return parser.parse_args(args)



if not os.path.exists(data_dir):
    raise OSError('data/ directory not found, aborting data preparation. ' \
                  'Restore it with "git checkout data" from the base ' \
                  'directory.')


def flights(small=None):
    start = time.time()
    flights_raw = os.path.join(data_dir, 'nycflights.tar.gz')
    flightdir = os.path.join(data_dir, 'nycflights')
    jsondir = os.path.join(data_dir, 'flightjson')
    if small is None:
        small = bool(os.environ.get("DASK_TUTORIAL_SMALL", False))

    if small:
        N = 500
    else:
        N = 10_000

    if not os.path.exists(flights_raw):
        print("- Downloading NYC Flights dataset... ", end='', flush=True)
        url = sources.flights_url
        urllib.request.urlretrieve(url, flights_raw)
        print("done", flush=True)

    if not os.path.exists(flightdir):
        print("- Extracting flight data... ", end='', flush=True)
        tar_path = os.path.join(data_dir, 'nycflights.tar.gz')
        with tarfile.open(tar_path, mode='r:gz') as flights:
            flights.extractall('data/')

        if small:
            for path in glob(os.path.join(data_dir, "nycflights", "*.csv")):
                with open(path, 'r') as f:
                    lines = f.readlines()[:1000]

                with open(path, 'w') as f:
                    f.writelines(lines)

        print("done", flush=True)

    if not os.path.exists(jsondir):
        print("- Creating json data... ", end='', flush=True)
        os.mkdir(jsondir)
        for path in glob(os.path.join(data_dir, 'nycflights', '*.csv')):
            prefix = os.path.splitext(os.path.basename(path))[0]
            df = pd.read_csv(path, nrows=N)
            df.to_json(os.path.join(data_dir, 'flightjson', prefix + '.json'),
                       orient='records', lines=True)
        print("done", flush=True)
    else:
        return

    end = time.time()
    print("** Created flights dataset! in {:0.2f}s**".format(end - start))

def random_array(small=None):
    if small is None:
        small = bool(os.environ.get("DASK_TUTORIAL_SMALL", False))

    if small:
        blocksize = 5000
    else:
        blocksize = 1000000

    nblocks = 1000
    shape = nblocks * blocksize

    t0 = time.time()
    if os.path.exists(os.path.join(data_dir, 'random.hdf5')):
        return

    with h5py.File(os.path.join(data_dir, 'random.hdf5'), mode='w') as f:
        dset = f.create_dataset('/x', shape=(shape,), dtype='f4')
        for i in range(0, shape, blocksize):
            dset[i: i + blocksize] = np.random.exponential(size=blocksize)

    t1 = time.time()
    print("Created random data for array exercise in {:0.2f}s".format(t1 - t0))


def accounts_csvs(small=None):
    t0 = time.time()
    if small is None:
        small = bool(os.environ.get("DASK_TUTORIAL_SMALL", False))

    if small:
        num_files, n, k = 3, 10000, 100
    else:
        num_files, n, k = 3, 1000000, 500

    fn = os.path.join(data_dir, 'accounts.%d.csv' % (num_files - 1))

    if os.path.exists(fn):
        return

    args = account_params(k)

    for i in range(num_files):
        df = account_entries(n, *args)
        df.to_csv(os.path.join(data_dir, 'accounts.%d.csv' % i),
                  index=False)

    t1 = time.time()
    print("Created CSV acccouts in {:0.2f}s".format(t1 - t0))


def accounts_json(small=None):
    t0 = time.time()
    if small is None:
        small = bool(os.environ.get("DASK_TUTORIAL_SMALL", False))

    if small:
        num_files, n, k = 50, 10000, 250
    else:
        num_files, n, k = 50, 100000, 500
    fn = os.path.join(data_dir, 'accounts.%02d.json.gz' % (num_files - 1))
    if os.path.exists(fn):
        return

    args = account_params(k)

    for i in range(num_files):
        seq = json_entries(n, *args)
        fn = os.path.join(data_dir, 'accounts.%02d.json.gz' % i)
        with gzip.open(fn, 'wb') as f:
            f.write(os.linesep.join(map(json.dumps, seq)).encode())

    t1 = time.time()
    print("Created JSON acccouts in {:0.2f}s".format(t1 - t0))


def create_weather(small=None):
    t0 = time.time()
    if small is None:
        small = bool(os.environ.get("DASK_TUTORIAL_SMALL", False))

    if small:
        growth = 1
    else:
        growth = 32
    filenames = sorted(glob(os.path.join(data_dir, 'weather-small', '*.hdf5')))

    if not filenames:
        ws_dir = os.path.join(data_dir, 'weather-small')
        raise ValueError('Did not find any hdf5 files in {}'.format(ws_dir))

    if not os.path.exists(os.path.join(data_dir, 'weather-big')):
        os.mkdir(os.path.join(data_dir, 'weather-big'))

    if all(os.path.exists(fn.replace('small', 'big')) for fn in filenames):
        return

    for fn in filenames:
        with h5py.File(fn, mode='r') as f:
            x = f['/t2m'][:]

        if small:
             y = x
             chunks = (180, 180)
        else:
            y = resize(x, (x.shape[0] * growth, x.shape[1] * growth), mode='constant')
            chunks = (500, 500)

        out_fn = os.path.join(data_dir, 'weather-big', os.path.split(fn)[-1])

        with h5py.File(out_fn, mode='w') as f:
            f.create_dataset('/t2m', data=y, chunks=chunks)
    t1 = time.time()
    print("Created weather dataset in {:0.2f}s".format(t1 - t0))


def main(args=None):
    args = parse_args(args)

    if (args.no_ssl_verify):
        print("- Disabling SSL Verification... ", end='', flush=True)
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        print("done", flush=True)

    if args.dataset == "random" or args.dataset == "all":
        random_array(args.small)
    if args.dataset == "weather" or args.dataset == "all":
        create_weather(args.small)
    if args.dataset == "accounts" or args.dataset == "all":
        accounts_csvs(args.small)
        accounts_json(args.small)
    if args.dataset == "flights" or args.dataset == "all":
        flights(args.small)


if __name__ == '__main__':
    sys.exit(main())
