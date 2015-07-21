@do
def total_chunk(nsamples):
    total = 0
    for i in range(nsamples):
        x = random()
        y = random()
        if x*x + y*y <= 1:
            total += 1
    return total

def parallel_estimate_pi(nsamples, npartitions):
    totals = [total_chunk(n) for n in partition(nsamples, npartitions)]
    return 4.*sum(totals)/nsamples
