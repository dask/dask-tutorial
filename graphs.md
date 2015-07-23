## `dask.core`

Dead simple task scheduling

[dask.pydata.org](http://dask.pydata.org/en/latest/)


## We've seen `dask.array`

*  Turns Numpy-ish code

        (2*x + 1) ** 3

*  Into Graphs

![](images/embarrassing.png)


## We've seen `dask.array`

*  Turns Numpy-ish code

        (2*x + 1) ** 3

*  Then executes those graphs

![](images/embarrassing.gif)


### Q: What is a dask graph?


<img src="images/dask-simple.png"
     alt="A simple dask dictionary"
     width="18%"
     align="right">

    # Normal Python             # Dask

    def inc(i):
       return i + 1

    def add(a, b):
       return a + b

    x = 1                       d = {'x': 1,
    y = inc(x)                       'y': (inc, 'x'),
    z = add(y, 10)                   'z': (add, 'y', 10)}

<hr>

    >>> from dask.threaded import get
    >>> get(d, 'z')
    12

*  **Dask graph** is a dictionary of tasks
*  **Task** is a tuple with a callable first element
*  **Arguments** are keys in dictionary ('y') or literal values (10)


<img src="images/dask-simple.png"
     alt="A simple dask dictionary"
     width="18%"
     align="right">

    # Normal Python             # Dask

    def inc(i):
       return i + 1

    def add(a, b):
       return a + b

    x = 1                       d = {'x': 1,
    y = inc(x)                       'y': (inc, 'x'),
    z = add(y, 10)                   'z': (add, 'y', 10)}

<hr>

    >>> from dask.multiprocessing import get
    >>> get(d, 'z')
    12

*  **Dask graph** is a dictionary of tasks
*  **Task** is a tuple with a callable first element
*  **Arguments** are keys in dictionary ('y') or literal values (10)


### Thoughts on Graphs

    d = {'x': 1,
         'y': (inc, 'x'),
         'z': (add, 'y', 10)}

*  Simple representation
*  Normal Python code (no DSL)
*  Strange for some users


### Example - dask.array

    >>> x = da.arange(15, chunks=(5,))
    dask.array<x, shape=(15,), chunks=((5, 5, 5)), dtype=None>

    >>> x.dask
    {("x", 0): (np.arange,  0,  5),
     ("x", 1): (np.arange,  5, 10),
     ("x", 2): (np.arange, 10, 15)}

    >>> x.sum().dask
    {("x", 0): (np.arange,  0,  5),
     ("x", 1): (np.arange,  5, 10),
     ("x", 2): (np.arange, 10, 15),
     ("s", 0): (np.sum, ("x", 0)),
     ("s", 1): (np.sum, ("x", 1)),
     ("s", 2): (np.sum, ("x", 2)),
     ("s",):   (sum, [("s", 0), ("s", 1), ("s", 2)])}


### Dask.array is a convenient way to make dictionaries

<hr>

### Dask is a convenient way to make libraries like dask.array


### Or use dask in custom parallel workloads


### Python's options for Parallelism

Explicit control -- Fast but hard

*  Threads/Processes/MPI/ZeroMQ
*  Concurrent.futures/Joblib/...
*  .
*  .
*  .
*  IPython parallel
*  Luigi
*  PySpark
*  Hadoop (mrjob)
*  SQL: Hive, Pig, Impala

Implicit control -- Restrictive but easy


### Python's options for Parallelism

Explicit control -- Fast but hard

*  Threads/Processes/MPI/ZeroMQ
*  Concurrent.futures/Joblib/...
*  .
*  .  <-- dask core lives here
*  .
*  IPython parallel
*  Luigi
*  PySpark
*  Hadoop (mrjob)
*  SQL: Hive, Pig, Impala

Implicit control -- Restrictive but easy


### Example: Parallel, Out-of-core, SVD

    >>> import dask.array as da
    >>> x = da.ones((5000, 1000), chunks=(1000, 1000))
    >>> u, s, v = da.linalg.svd(x)

<a href="http://blaze.pydata.org/en/latest/_static/presentations/images/dask-svd.png">
  <img src="http://blaze.pydata.org/en/latest/_static/presentations/images/dask-svd.png" alt="Dask SVD graph" width="30%">
</a>

*Work by Mariano Tepper.  "Compressed Nonnegative Matrix Factorization is Fast
and Accurate" [arXiv](http://arxiv.org/abs/1505.04650)*


### SVD - Dict

    >>> s.dask
    {('x', 0, 0): (np.ones, (1000, 1000)),
     ('x', 1, 0): (np.ones, (1000, 1000)),
     ('x', 2, 0): (np.ones, (1000, 1000)),
     ('x', 3, 0): (np.ones, (1000, 1000)),
     ('x', 4, 0): (np.ones, (1000, 1000)),
     ('tsqr_2_QR_st1', 0, 0): (np.linalg.qr, ('x', 0, 0)),
     ('tsqr_2_QR_st1', 1, 0): (np.linalg.qr, ('x', 1, 0)),
     ('tsqr_2_QR_st1', 2, 0): (np.linalg.qr, ('x', 2, 0)),
     ('tsqr_2_QR_st1', 3, 0): (np.linalg.qr, ('x', 3, 0)),
     ('tsqr_2_QR_st1', 4, 0): (np.linalg.qr, ('x', 4, 0)),
     ('tsqr_2_R', 0, 0): (operator.getitem, ('tsqr_2_QR_st2', 0, 0), 1),
     ('tsqr_2_R_st1', 0, 0): (operator.getitem,('tsqr_2_QR_st1', 0, 0), 1),
     ('tsqr_2_R_st1', 1, 0): (operator.getitem, ('tsqr_2_QR_st1', 1, 0), 1),
     ('tsqr_2_R_st1', 2, 0): (operator.getitem, ('tsqr_2_QR_st1', 2, 0), 1),
     ('tsqr_2_R_st1', 3, 0): (operator.getitem, ('tsqr_2_QR_st1', 3, 0), 1),
     ('tsqr_2_R_st1', 4, 0): (operator.getitem, ('tsqr_2_QR_st1', 4, 0), 1),
     ('tsqr_2_R_st1_stacked', 0, 0): (np.vstack,
                                       [('tsqr_2_R_st1', 0, 0),
                                        ('tsqr_2_R_st1', 1, 0),
                                        ('tsqr_2_R_st1', 2, 0),
                                        ('tsqr_2_R_st1', 3, 0),
                                        ('tsqr_2_R_st1', 4, 0)])),
     ('tsqr_2_QR_st2', 0, 0): (np.linalg.qr, ('tsqr_2_R_st1_stacked', 0, 0)),
     ('tsqr_2_SVD_st2', 0, 0): (np.linalg.svd, ('tsqr_2_R', 0, 0)),
     ('tsqr_2_S', 0): (operator.getitem, ('tsqr_2_SVD_st2', 0, 0), 1)}


### SVD - Parallel Profile

<iframe src="http://blaze.pydata.org/en/latest/_static/presentations/svd.profile.html"
        marginwidth="0"
        marginheight="0" scrolling="no" width="800"
        height="300"></iframe>

*Bokeh profile tool by Jim Crist*


## Randomized Approximate Parallel Out-of-Core SVD

    >>> import dask.array as da
    >>> x = da.ones((5000, 1000), chunks=(1000, 1000))
    >>> u, s, v = da.linalg.svd_compressed(x, k=100, n_power_iter=2)

<a href="http://blaze.pydata.org/en/latest/_static/presentations/images/dask-svd-random.png">
<img src="http://blaze.pydata.org/en/latest/_static/presentations/images/dask-svd-random.png"
     alt="Dask graph for random SVD"
     width="10%" >
</a>

N. Halko, P. G. Martinsson, and J. A. Tropp.
*Finding structure with randomness: Probabilistic algorithms for
constructing approximate matrix decompositions.*

*Dask implementation by Mariano Tepper*
