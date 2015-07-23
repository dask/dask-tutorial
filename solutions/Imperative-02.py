from dask import do

def parallel_estimate_pi(nsamples):
    points = [do(is_inside_circle)() for i in range(nsamples)]
    return 4. * do(sum)(points) / nsamples

print(parallel_estimate_pi(10000).compute())
