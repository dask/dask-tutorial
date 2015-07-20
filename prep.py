import os
import numpy as np

def random_array():
    if not os.path.exists(os.path.join('data', 'random.hdf5')):

        import h5py

        with h5py.File(os.path.join('data', 'random.hdf5')) as f:
            dset = f.create_dataset('/x', shape=(1000000000,), dtype='f4')
            for i in range(0, 1000000000, 1000000):
                dset[i: i + 1000000] = np.random.exponential(size=1000000)
