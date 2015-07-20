from scipy.misc import imresize
from glob import glob
import h5py
import os

def create_weather(growth=3200):
    filenames = sorted(glob(os.path.join('data', 'weather-small', '*.hdf5')))

    if not os.path.exists(os.path.join('data', 'weather-big')):
        os.mkdir(os.path.join('data', 'weather-big'))

    for fn in filenames:
        with h5py.File(fn) as f:
            x = f['/t2m'][:]

        y = imresize(x, growth)

        out_fn = os.path.join('data', 'weather-big', os.path.split(fn)[-1])

        with h5py.File(out_fn) as f:
            f.create_dataset('/t2m', data=y)

if __name__ == '__main__':
    create_weather()
