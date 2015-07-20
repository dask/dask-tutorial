import h5py
from glob import glob
import os

filenames = sorted(glob(os.path.join('data', 'weather-big', '*.hdf5')))
dsets = [h5py.File(filename)['/t2m'] for filename in filenames]

import dask.array as da
arrays = [da.from_array(dset, chunks=(1000, 1000)) for dset in dsets]

x = da.stack(arrays, axis=0)

result = x.mean(axis=0)

from matplotlib import pyplot as plt
plt.imshow(result, cmap='RdBu_r')
