from dask import delayed

def how_many_inside_circle(k):
    return sum(is_inside_circle() for i in range(k))

def parallel_estimate_pi(nsamples, k):
    points = [delayed(how_many_inside_circle)(k)
              for i in range(int(nsamples / k))]
    if nsamples % k != 0:   # doesn't divide cleanly
        points.append(delayed(how_many_inside_circle(nsamples % k)))
    return 4. * delayed(sum)(points) / nsamples

print(parallel_estimate_pi(10000000, 100000).compute())
