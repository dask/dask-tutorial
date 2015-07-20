import h5py
import numpy as np
import h5py
import os

f = h5py.File(os.path.join('data', 'tmp.hdf5'))
dset = f.create_dataset('/x', shape=(1000000000,), dtype='f4')
for i in range(0, 1000000000, 1000000):
    dset[i: i + 1000000] = np.random.exponential(size=1000000)
