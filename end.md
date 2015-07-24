### Dask

Parallelism through blocked algorithms and dynamic task scheduling

<img src="http://dask.pydata.org/en/latest/_images/collections-schedulers.png">


### Dask

*  High Level Collections
    *  `dask.array`:  `NumPy` + `threading`
    *  `dask.bag`:  `map`, `filter`, `toolz` + `multiprocessing`
    *  `dask.dataframe`:  `Pandas` + `threading`
*  Dynamic Task Scheduling
    *  Messy problems need messy solutions
    *  Parallel execution with small memory footprint
    *  Low latency for numeric algorithms
*  Consider shared memory parallelism for <1TB problems


### Don't use dask

<hr>

### Most problems are small


### Don't use dask

<hr>

### Consider a Traditional Database


Many problems discussed today can be solved with a database

*  Postgres
*  ElasticSearch
*  MongoDB
*  ...

These provide efficient, indexed search on normal hardware


### Didn't talk about

*  `dask.distributed`
*  `dask.diagnostics`
*  Details of dynamic task scheduling
*  What breaks
*  ...


### Questions and Feedback

*   [`dask`](http://stackoverflow.com/questions/tagged/dask) tag on Stack Overflow
*   [github issues](https://github.com/ContinuumIO/dask/issues/new) for bug reports and feature requests
*   [blaze-dev](http://groups.google.com/a/continuum.io/forum/#!forum/blaze-dev)  mailing list for community discussion
*   Right here, right now.
