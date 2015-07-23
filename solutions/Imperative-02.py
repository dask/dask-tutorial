@do
def point_chunk():
    """Generates a random x, y point, returns 1 if in circle, else returns 0."""
    x = random()
    y = random()
    if x*x + y*y <= 1:
        return 1
    else:
        return 0

def parallel_estimate_pi(nsamples):
    points = []
    for i in range(nsamples):
        points.append(point_chunk())
    total = do(sum)(points)
    result = 4.*total/nsamples
    return result.compute(get=get)
