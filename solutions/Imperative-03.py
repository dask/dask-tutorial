@do
def total_chunk(nsamples):
    """Generates `nsamples` random x, y points, returns number of 
    points that were in the circle.
    """
    total = 0
    for i in range(nsamples):
        x = random()
        y = random()
        if x*x + y*y <= 1:
            total += 1
    return total

def parallel_estimate_pi(nsamples, npartitions):
    totals = []
    for n in partition(nsamples, npartitions):
        totals.append(total_chunk(n))
    result = 4.*do(sum)(totals)/nsamples
    return result.compute(get=get)
