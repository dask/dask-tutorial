result = x[:, ::2, ::2]
da.to_hdf5(os.path.join('data', 'myfile.hdf5'), '/output', result)